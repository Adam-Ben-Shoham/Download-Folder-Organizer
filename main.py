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


