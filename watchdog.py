import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/debanjana/Downloads"
to_dir = "C:/Users/debanjana/OneDrive/Desktop/Document_Files"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")

        name,extensions = os.path.splitext(event.src_path)
        for key, vlaue in dir_tree.items():
            file_name = os.path.basename(event.src_path)

            path1 = from_dir + "/" + file_name
            path2 = from_dir + "/" + key
            path3 = to_dir + "/" + key + "/" + file_name

            if os.path.exists(path2):
                print("Directory exists..")
                print("Moving" + file_name + ".....")
                shutil.move(path1,path3)
                time.sleep(1)
            else:
                print("Maling Directory")
                os.makedirs(path2)
                print("Moving" + file_name + "......")
                shutil.move(path2,path3)
                time.sleep(1)
            print(event)
            print(event.src_path)

    def on_deleted(self, event):
        print(f"Ooops!Someone deleted {event.src_path}!")

        name,extensions = os.path.splitext(event.src_path)
        for key, value in dir_tree.items():
            file_name = os.path.splitext(event.src_path)

            path1 = from_dir + "/" + file_name
            path2 = from_dir + "/" + key
            path3 = to_dir + "/" + key + "/" + file_name

            if os.path.exists(path2):
                print("Directory exists...")
                print("Moving" + file_name + "......")
                shutil.move(path2,path3)
                time.sleep(1)
            print(event)
            print(event.src_path)

    def on_modified(self, event):
        print(f" {event.src_path} has been modified!")

        name,extensions = os.path.splitext(event.src_path)
        for key, value in dir_tree.items():
            file_name = os.path.splitext(event.src_path)

            path1 = from_dir + "/" + file_name
            path2 = from_dir + "/" + key
            path3 = to_dir + "/" + key + "/" + file_name

            if os.path.exists(path2):
                print("Directory exists...")
                print("Moving" + file_name + "......")
                shutil.move(path2,path3)
                time.sleep(1)
            print(event)
            print(event.src_path)

    def on_moved(self, event):
        print(f"Someone has moved {event.src_path}!")

        name,extensions = os.path.splitext(event.src_path)
        for key, value in dir_tree.items():
            file_name = os.path.splitext(event.src_path)

            path1 = from_dir + "/" + file_name
            path2 = from_dir + "/" + key
            path3 = to_dir + "/" + key + "/" + file_name

            if os.path.exists(path2):
                print("Directory exists...")
                print("Moving" + file_name + "......")
                shutil.move(path2,path3)
                time.sleep(1)
            print(event)
            print(event.src_path)


#initialize observer
event_handler = FileEventHandler()

#initialize observer
observer = Observer()

#schedule the observer
observer.schedule(event_handler,from_dir,recursive=True)

#start the observer 
observer.start()


try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()