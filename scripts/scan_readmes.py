import os
import re
import argparse

def main():
    parser = argparse.ArgumentParser(description="Génère un index Markdown des fichiers .md dans les dossiers cXX.")
    parser.add_argument("-f", "--folder", type=str, default=".", help="Dossier de base à analyser (défaut: dossier courant).")
    args = parser.parse_args()

    base_path = args.folder
    output_file = os.path.join(base_path, "all_readmes.md")
    script_name = os.path.basename(__file__)

    pattern = re.compile(r"c(\d{2})")
    entries = []

    for folder in sorted(os.listdir(base_path)):
        match = pattern.fullmatch(folder)
        if match and os.path.isdir(os.path.join(base_path, folder)):
            folder_path = os.path.join(base_path, folder)

            main_readme = None
            sub_items = []

            # Recherche récursive
            for root, _, files in os.walk(folder_path):
                for file in sorted(files):
                    if file.lower().endswith(".md"):
                        full_path = os.path.join(root, file)
                        rel_path = os.path.relpath(full_path, start=base_path).replace(os.sep, '/')
                        relative_to_cxx = os.path.relpath(full_path, start=folder_path).replace(os.sep, '/')

                        if root == folder_path and file.lower() == "readme.md":
                            main_readme = f"- [Cours {match.group(1)}](./{rel_path})"
                        else:
                            display_name = f"{os.path.basename(os.path.dirname(full_path))}/{file}"
                            sub_items.append(f"  - [{display_name}](./{rel_path})")

            if main_readme:
                entry = [main_readme] + sub_items
            elif sub_items:
                # Fallback si aucun readme.md principal
                entry = [f"- Cours {match.group(1)}"] + sub_items
            else:
                continue

            entries.append("\n".join(entry))

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"<!-- Fichier généré automatiquement par le script {script_name} -->\n\n")
        f.write("\n".join(entries))

    print(f"Fichier '{output_file}' généré avec succès.")

if __name__ == "__main__":
    main()
