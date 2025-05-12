import os
import shutil
import time
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

FILE_CATEGORIES = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "videos": [".mp4", ".avi", ".mov", ".mkv", ".flv"],
    "documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt"],
    "adobe": [".psd", ".ai", ".indd"],
    "other": []  
}


DOWNLOADS_FOLDER = os.path.expanduser("~/Downloads")


for folder in FILE_CATEGORIES:
    folder_path = os.path.join(DOWNLOADS_FOLDER, folder)
    os.makedirs(folder_path, exist_ok=True)

def get_destination_folder(file_extension):
    for folder, extensions in FILE_CATEGORIES.items():
        if file_extension.lower() in extensions:
            return folder
    return "other"

def is_file_ready(file_path):
    """Check if a file is ready to be moved (not being written to)."""
    try:
        if file_path.endswith(".tmp"):  
            print(f"Ignoring temporary file: {file_path}")
            return False
        initial_size = os.path.getsize(file_path)
        time.sleep(1)  
        return os.path.getsize(file_path) == initial_size
    except (FileNotFoundError, PermissionError):
        return False

def organize_file(file_path):
    """Organize a file by moving it to the appropriate folder."""
    if not os.path.isfile(file_path):
        print(f"Skipping {file_path}: Not a file.")
        return

    if not is_file_ready(file_path):
        print(f"Skipping {file_path}: File not ready.")
        return

    file_name, file_extension = os.path.splitext(os.path.basename(file_path))
    destination_folder = get_destination_folder(file_extension)
    

    download_date = datetime.fromtimestamp(os.path.getctime(file_path)).strftime("%Y-%m-%d")
    new_file_name = f"{download_date}_{file_name}{file_extension}"
    destination_path = os.path.join(DOWNLOADS_FOLDER, destination_folder, new_file_name)


    counter = 1
    while os.path.exists(destination_path):
        new_file_name = f"{download_date}_{file_name}_{counter}{file_extension}"
        destination_path = os.path.join(DOWNLOADS_FOLDER, destination_folder, new_file_name)
        counter += 1


    try:
        shutil.move(file_path, destination_path)
        print(f"Moved: {file_path} -> {destination_path}")
    except FileNotFoundError:
        print(f"File not found during move operation: {file_path}")

class DownloadsFolderHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"Detected new file: {event.src_path}")
       
            time.sleep(2)
            if not event.src_path.endswith(".tmp"):
                organize_file(event.src_path)
            else:
                print(f"Temporary file ignored: {event.src_path}")

def main():

    for file_name in os.listdir(DOWNLOADS_FOLDER):
        file_path = os.path.join(DOWNLOADS_FOLDER, file_name)
        organize_file(file_path)

    while True:

        event_handler = DownloadsFolderHandler()
        observer = Observer()
        observer.schedule(event_handler, DOWNLOADS_FOLDER, recursive=False)
        observer.start()
        print("Monitoring Downloads folder for new files...")

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            observer.join()

if __name__ == "__main__":
    main()
