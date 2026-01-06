import os
import shutil
import datetime

BACKUP_FOLDER = r"C:\_data\backup_cle"


def is_text_file(file_path):
    allowed_extensions = ['.txt', '.md', '.ino', '.cpp', '.h']
    ext = os.path.splitext(file_path)[1].lower()
    if ext in allowed_extensions:
        return True
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            f.read()
        return True
    except Exception:
        return False



def validate_usb_contents(usb_path):
    errors = []
    for root, dirs, files in os.walk(usb_path):
        if '.git' in dirs:
            dirs.remove('.git')
        for file in files:
            file_path = os.path.join(root, file)
            if not is_text_file(file_path):
                errors.append(f"Non-text file found: {file_path}")
    return errors


def get_student_name(usb_path):
    for root, _, files in os.walk(usb_path):
        for file in files:
            if file.endswith(".txt") :
                student_name = os.path.splitext(file)[0]
                return student_name
    return None


def backup_usb(usb_path):
    student_name = get_student_name(usb_path)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_folder_name = student_name if student_name else timestamp
    backup_path = os.path.join(BACKUP_FOLDER, backup_folder_name)
    os.makedirs(backup_path, exist_ok=True)
    shutil.copytree(usb_path, backup_path, dirs_exist_ok=True)
    return backup_path


def main():
    while True:
        usb_path = input("Enter the path to the USB drive: ")

        errors = validate_usb_contents(usb_path)

        if errors:
            print("Errors found:")
            for error in errors:
                print(error)
            print("Backup will not be created.")
        else:
            backup_path = backup_usb(usb_path)
            print(f"Backup created at {backup_path}")

        print("\n1. Continue to next USB\n2. Quit")
        choice = input("Choose an option: ")
        if choice == '2':
            break


if __name__ == "__main__":
    main()
