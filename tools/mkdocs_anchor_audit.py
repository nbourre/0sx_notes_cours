#!/usr/bin/env python3
"""
MkDocs Anchor Audit + Auto-fix (French-friendly)

- Scans Markdown files under docs/ (or given docs_dir)
- Builds "MkDocs-like" slugs from headings
- Finds internal links (#fragment) and cross-page links (file.md#fragment)
- Reports fragments that won't resolve (often due to accents / GitHub-vs-MkDocs differences)
- Supports explicit anchors: <a id="..."></a> or <span id="..."></span>

Auto-fix mode:
  --apply
    - Rewrites only links where a safe suggestion is found AND exists in target anchors.
    - Backs up original file by adding "_bk" to its extension: file.md -> file.md_bk

Exit code:
  0 = no issues (or fixed issues)
  1 = issues found (and not fixed), or fixed but still remaining if --fail-on-issues
  2 = runtime/config error
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
# Markdown links: [text](target)
MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
# Explicit HTML anchors
HTML_ID_RE = re.compile(r"""<(?:a|span)\s+[^>]*\bid\s*=\s*["']([^"']+)["'][^>]*>""", re.IGNORECASE)


@dataclass(frozen=True)
class AnchorIssue:
    src_file: Path
    line_no: int
    raw_target: str          # e.g. "#différence-..."
    target_file: Path        # resolved md file
    fragment: str            # fragment (without '#')
    suggested: Optional[str] # suggested fragment (without '#'), if any
    reason: str              # human readable


def mkdocs_slugify(text: str) -> str:
    """
    Approximate Python-Markdown's TOC slugify behavior (commonly used by MkDocs):
    - Normalize (NFKD)
    - Strip accents -> ASCII
    - Lowercase
    - Replace non-alnum with '-'
    - Collapse repeats, strip edges
    """
    text = text.strip()
    text = re.sub(r"\s+#*$", "", text).strip()
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    ascii_text = ascii_text.lower()
    ascii_text = re.sub(r"[^a-z0-9]+", "-", ascii_text)
    ascii_text = re.sub(r"-{2,}", "-", ascii_text).strip("-")
    return ascii_text


def iter_md_files(docs_dir: Path) -> Iterable[Path]:
    for p in docs_dir.rglob("*.md"):
        parts = {part.lower() for part in p.parts}
        if ".git" in parts or "site" in parts or "__pycache__" in parts:
            continue
        yield p


def resolve_md_target(docs_dir: Path, src_file: Path, link_path: str) -> Optional[Path]:
    link_path = link_path.split("?", 1)[0].strip()
    if not link_path:
        return src_file

    candidate = (src_file.parent / link_path).resolve()

    try:
        candidate.relative_to(docs_dir.resolve())
    except ValueError:
        return None

    if candidate.is_dir():
        idx = candidate / "index.md"
        return idx if idx.exists() else None

    if candidate.suffix.lower() != ".md":
        return None

    return candidate if candidate.exists() else None


def build_anchor_index(docs_dir: Path) -> Dict[Path, Set[str]]:
    index: Dict[Path, Set[str]] = {}

    for md in iter_md_files(docs_dir):
        anchors: Set[str] = set()
        try:
            content = md.read_text(encoding="utf-8", errors="replace").splitlines()
        except Exception:
            continue

        for line in content:
            m = HEADING_RE.match(line)
            if m:
                heading_text = m.group(2)
                slug = mkdocs_slugify(heading_text)
                if slug:
                    anchors.add(slug)

            for html_id in HTML_ID_RE.findall(line):
                html_id = html_id.strip()
                if html_id:
                    anchors.add(html_id)

        index[md.resolve()] = anchors

    return index


def compute_safe_replacement(
    docs_dir: Path,
    src_md: Path,
    raw_target: str,
    anchor_index: Dict[Path, Set[str]],
) -> Tuple[Optional[str], Optional[AnchorIssue]]:
    """
    If raw_target is a local/cross-page fragment link, compute a safe replacement.
    Returns (new_target, issue_if_any). new_target is raw_target if no change.
    Only returns a replacement when:
      - fragment does NOT exist as-is
      - slugified(fragment) DOES exist in target anchors
    """
    raw_target = raw_target.strip()

    # Skip schemes (http:, mailto:, etc.)
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", raw_target):
        return None, None

    if "#" not in raw_target:
        return None, None

    path_part, frag = raw_target.split("#", 1)
    path_part = path_part.strip()
    frag = frag.strip()
    if not frag:
        return None, None

    if path_part == "":
        target_md = src_md
    else:
        resolved = resolve_md_target(docs_dir, src_md, path_part)
        if resolved is None:
            issue = AnchorIssue(
                src_file=src_md,
                line_no=0,
                raw_target=raw_target,
                target_file=Path(path_part),
                fragment=frag,
                suggested=None,
                reason="Le fichier cible n'existe pas (ou est hors de docs/).",
            )
            return None, issue
        target_md = resolved.resolve()

    anchors = anchor_index.get(target_md, set())

    # OK already
    if frag in anchors:
        return None, None

    suggested = mkdocs_slugify(frag)
    if suggested and suggested in anchors:
        new_target = f"{path_part + '#' if path_part else '#'}{suggested}"
        issue = AnchorIssue(
            src_file=src_md,
            line_no=0,
            raw_target=raw_target,
            target_file=target_md,
            fragment=frag,
            suggested=suggested,
            reason="Fragment probablement GitHub-style (accents). MkDocs utilise une ancre normalisée.",
        )
        return new_target, issue

    issue = AnchorIssue(
        src_file=src_md,
        line_no=0,
        raw_target=raw_target,
        target_file=target_md,
        fragment=frag,
        suggested=suggested if suggested else None,
        reason="Ancre introuvable dans la page cible (titre ou id HTML).",
    )
    return None, issue


def audit_links(docs_dir: Path, anchor_index: Dict[Path, Set[str]]) -> List[AnchorIssue]:
    issues: List[AnchorIssue] = []

    for md in iter_md_files(docs_dir):
        md_abs = md.resolve()
        try:
            lines = md.read_text(encoding="utf-8", errors="replace").splitlines()
        except Exception as e:
            issues.append(
                AnchorIssue(
                    src_file=md_abs,
                    line_no=0,
                    raw_target="",
                    target_file=md_abs,
                    fragment="",
                    suggested=None,
                    reason=f"Impossible de lire le fichier: {e}",
                )
            )
            continue

        for i, line in enumerate(lines, start=1):
            for raw_target in MD_LINK_RE.findall(line):
                new_target, issue = compute_safe_replacement(docs_dir, md_abs, raw_target, anchor_index)
                if issue:
                    issues.append(
                        AnchorIssue(
                            src_file=md_abs,
                            line_no=i,
                            raw_target=issue.raw_target,
                            target_file=issue.target_file,
                            fragment=issue.fragment,
                            suggested=issue.suggested,
                            reason=issue.reason,
                        )
                    )
    return issues


def apply_fixes(docs_dir: Path, anchor_index: Dict[Path, Set[str]]) -> Tuple[int, List[AnchorIssue]]:
    """
    Applies safe fixes in-place with backups.
    Returns: (num_files_modified, remaining_issues_after_apply)
    """
    modified_files = 0

    for md in iter_md_files(docs_dir):
        md_abs = md.resolve()
        try:
            lines = md_abs.read_text(encoding="utf-8", errors="replace").splitlines()
        except Exception:
            continue

        changed = False
        new_lines: List[str] = []

        for line in lines:
            # Replace link targets inside this line
            def repl(match: re.Match) -> str:
                nonlocal changed
                original_target = match.group(1)
                new_target, issue = compute_safe_replacement(docs_dir, md_abs, original_target, anchor_index)
                if new_target and new_target != original_target:
                    changed = True
                    return match.group(0).replace(f"({original_target})", f"({new_target})", 1)
                return match.group(0)

            # We need to apply replacements for each link occurrence.
            # Since repl returns the whole [..](..) string, we use a regex to match full link patterns.
            # Simpler: do a manual replace per captured target.
            # We'll re-scan this line's targets and replace one by one safely.
            updated_line = line
            targets = MD_LINK_RE.findall(line)
            for t in targets:
                new_target, _ = compute_safe_replacement(docs_dir, md_abs, t, anchor_index)
                if new_target and new_target != t:
                    # replace only the first occurrence of "(t)" to avoid over-replacing if identical targets exist multiple times
                    updated_line = updated_line.replace(f"({t})", f"({new_target})", 1)
                    changed = True

            new_lines.append(updated_line)

        if changed:
            backup_path = md_abs.with_name(md_abs.name + "_bk")  # readme.md -> readme.md_bk
            if backup_path.exists():
                # avoid overwriting existing backup
                # readme.md_bk -> readme.md_bk2, etc.
                n = 2
                while True:
                    candidate = md_abs.with_name(md_abs.name + f"_bk{n}")
                    if not candidate.exists():
                        backup_path = candidate
                        break
                    n += 1

            md_abs.replace(backup_path)
            md_abs.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
            modified_files += 1

    # Re-audit after apply
    remaining = audit_links(docs_dir, anchor_index=build_anchor_index(docs_dir))
    return modified_files, remaining


def print_report(docs_dir: Path, issues: List[AnchorIssue], format_: str) -> None:
    if not issues:
        print(f"✅ Aucun problème d'ancre détecté dans {docs_dir}")
        return

    if format_ == "text":
        print(f"⚠️ Problèmes détectés ({len(issues)}) dans {docs_dir}\n")
        for it in issues:
            src_rel = it.src_file.resolve().relative_to(docs_dir.parent.resolve())
            tgt = it.target_file
            try:
                tgt_rel = tgt.resolve().relative_to(docs_dir.parent.resolve())
            except Exception:
                tgt_rel = tgt

            print(f"- {src_rel}:{it.line_no}")
            print(f"  lien: ({it.raw_target})")
            print(f"  cible: {tgt_rel}")
            print(f"  raison: {it.reason}")
            if it.suggested and it.suggested != it.fragment:
                print(f"  suggestion: remplace '#{it.fragment}' par '#{it.suggested}'")
            print()

        print("Conseil: pour une ancre stable sans extensions, ajoute:")
        print("  <a id=\"mon-id\"></a>")
        print("  ## Mon titre")
        print("et pointe vers (#mon-id)\n")

    elif format_ == "csv":
        # CSV header
        print("src_file,line,raw_target,target_file,fragment,suggested,reason")
        for it in issues:
            # Basic CSV escaping: wrap in quotes and escape quotes by doubling
            def esc(s: str) -> str:
                return '"' + s.replace('"', '""') + '"'

            print(
                ",".join(
                    [
                        esc(str(it.src_file)),
                        str(it.line_no),
                        esc(it.raw_target),
                        esc(str(it.target_file)),
                        esc(it.fragment),
                        esc(it.suggested or ""),
                        esc(it.reason),
                    ]
                )
            )
    else:
        raise ValueError("format invalide")


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit des ancres MkDocs (accents / liens internes) + auto-fix.")
    parser.add_argument("--docs-dir", default="docs", help="Dossier de documentation MkDocs (défaut: docs)")
    parser.add_argument("--format", choices=["text", "csv"], default="text", help="Format du rapport")
    parser.add_argument("--fail-on-issues", action="store_true", help="Retourne exit code 1 si problèmes détectés")
    parser.add_argument("--apply", action="store_true", help="Répare automatiquement les liens quand c'est sûr (avec backup .md_bk)")
    args = parser.parse_args()

    docs_dir = Path(args.docs_dir).resolve()
    if not docs_dir.exists() or not docs_dir.is_dir():
        print(f"❌ docs_dir introuvable: {docs_dir}", file=sys.stderr)
        return 2

    # Windows-friendly: ensure stdout/stderr can emit UTF-8 (accents)
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

    anchor_index = build_anchor_index(docs_dir)

    if args.apply:
        modified, remaining = apply_fixes(docs_dir, anchor_index)
        print(f"🛠️  Fichiers modifiés: {modified}")
        if remaining:
            print(f"⚠️  Problèmes restants: {len(remaining)}")
            print_report(docs_dir, remaining, args.format)
        else:
            print("✅ Tous les liens réparables ont été corrigés, aucun problème restant détecté.")

        if args.fail_on_issues and remaining:
            return 1
        return 0 if not remaining else 1

    issues = audit_links(docs_dir, anchor_index)
    print_report(docs_dir, issues, args.format)

    if args.fail_on_issues and issues:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
