import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = {}

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created")

    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}!")

    def on_modified(self, event):
        print(f"Look Out {event.src_path} has been modified")

    def on_moved(self, event):
        print(f"Oh!, {event.src_path} has been moved")