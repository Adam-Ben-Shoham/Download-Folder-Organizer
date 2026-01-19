from pathlib import Path
import shutil

sorting_dict = {'Documents': ['.pdf', '.docx', '.txt', '.pptx', '.xlsx', '.csv'],
                'Images': ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.tiff'],
                'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.wmv'],
                'Software': ['.exe', '.msi', '.dmg', '.pkg'],
                'Compressed': ['.zip', '.rar', '.7z', '.tar', '.gz'],
                'Music': ['.mp3', '.m4a', '.flac', '.wav', '.aac'],
                'Misc': []
                }

home = Path.home()
download_folder = home / 'Downloads'


def check_for_folders():
    for folder_name in sorting_dict.keys():
        new_path = download_folder / folder_name

        new_path.mkdir(parents=True, exist_ok=True)


        if item.is_file() and not item.name.startswith('.') and item.name != 'main.py':

            dest_folder = 'Misc'
            for folder_name, extensions in sorting_dict.items():
                if item.suffix.lower() in extensions:
                    dest_folder = folder_name
                    break

            dir_path = download_folder / dest_folder / item.name

            try:
                shutil.move(item, dir_path)
            except PermissionError:
                print(f"Skipping {item.name}, Permission denied, File is open elsewhere...")
            except FileExistsError:
                print(f"File already exists in folder, renaming file to {item.stem}1{item.suffix}")
            except OSError:
                print(f"Could not move {item} to {dir_path}, OSError")
