import time
from pathlib import Path
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

sorting_dict = {'Documents': ['.pdf', '.docx', '.txt', '.pptx', '.xlsx', '.csv'],
                'Images': ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.tiff'],
                'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.wmv'],
                'Software': ['.exe', '.msi', '.dmg', '.pkg'],
                'Compressed': ['.zip', '.rar', '.7z', '.tar', '.gz'],
                'Music': ['.mp3', '.m4a', '.flac', '.wav', '.aac'],
                }

home = Path.home()
download_folder = home / 'Downloads'

class MyHandler(FileSystemEventHandler):
    def on_modified(self,event):
        time.sleep(4)
        sort_files()


def check_for_folders():
    for folder_name in sorting_dict.keys():
        new_path = download_folder / folder_name

        new_path.mkdir(parents=True, exist_ok=True)

    (download_folder/'Misc').mkdir(parents=True, exist_ok=True)


def sort_files():
    for item in download_folder.iterdir():

        if item.is_dir() or item.name.startswith('.') or item.name == 'main.py':
            continue

        if item.is_file() and not item.name.startswith('.') and item.name != 'main.py':

            dest_folder = 'Misc'
            for folder_name, extensions in sorting_dict.items():
                if item.suffix.lower() in extensions:
                    dest_folder = folder_name
                    break

            temp_path = download_folder / dest_folder / item.name

            counter = 1

            while temp_path.exists():
                new_name = f'{item.stem}{counter}{item.suffix}'
                temp_path = download_folder / dest_folder / new_name
                counter += 1

            dir_path = temp_path

            try:
                shutil.move(item, dir_path)
            except PermissionError:
                print(f"Skipping {item.name}, Permission denied, File is open elsewhere...")
            except FileExistsError:
                print(f'Skipping {item.name}, File already exists...')
            except OSError:
                print(f"Could not move {item} to {dir_path}, OSError")

if __name__ == '__main__':

    check_for_folders()
    sort_files()

    handler = MyHandler()
    observer = Observer()
    observer.schedule(handler, path=download_folder, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
        print('Stopping organizer')
    observer.join()
    print('Process terminated.')