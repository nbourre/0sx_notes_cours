import os
import re
import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser(description="Script pour gérer les fichiers .md dans les dossiers cXX et les convertir en PDF.")
    parser.add_argument("-f", "--folder", type=str, default=".", help="Dossier de base à analyser (défaut: dossier courant).")
    args = parser.parse_args()

    base_path = args.folder
    output_file = os.path.join(base_path, "all_readmes.md")
    script_name = os.path.basename(__file__)

    while True:
        print("\nOptions :")
        print("1. Générer l'index Markdown")
        print("2. Convertir chaque .md en PDF")
        print("3. Fusionner tous les .md en un seul PDF")
        print("4. Quitter")
        choice = input("Choisissez une option : ")

        if choice == "1":
            generate_index(base_path, output_file, script_name)
        elif choice == "2":
            convert_md_to_pdf(base_path)
        elif choice == "3":
            merge_pdfs(base_path)
        elif choice == "4":
            break
        else:
            print("Option invalide. Veuillez réessayer.")


def generate_index(base_path, output_file, script_name):
    pattern = re.compile(r"c(\d{2})")
    entries = []

    for folder in sorted(os.listdir(base_path)):
        match = pattern.fullmatch(folder)
        if match and os.path.isdir(os.path.join(base_path, folder)):
            folder_path = os.path.join(base_path, folder)

            main_readme = None
            sub_items = []

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
                entry = [f"- Cours {match.group(1)}"] + sub_items
            else:
                continue

            entries.append("\n".join(entry))

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"<!-- Fichier généré automatiquement par le script {script_name} -->\n\n")
        f.write("\n".join(entries))

    print(f"Fichier '{output_file}' généré avec succès.")


def convert_md_to_pdf(base_path):
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.lower().endswith(".md"):
                md_path = os.path.join(root, file)
                pdf_path = os.path.splitext(md_path)[0] + ".pdf"
                print(f"Conversion de {md_path} en {pdf_path}")
                subprocess.run(["pandoc", md_path, "-o", pdf_path])


def merge_pdfs(base_path):
    pdf_files = []
    for root, _, files in os.walk(base_path):
        for file in sorted(files):
            if file.lower().endswith(".pdf"):
                pdf_files.append(os.path.join(root, file))

    if not pdf_files:
        print("Aucun fichier PDF trouvé pour la fusion.")
        return

    output_pdf = os.path.join(base_path, "merged.pdf")
    print("Fusion des fichiers PDF...")
    subprocess.run(["pdfunite"] + pdf_files + [output_pdf])
    print(f"PDF fusionné créé : {output_pdf}")


if __name__ == "__main__":
    main()
