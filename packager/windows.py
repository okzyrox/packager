# Windows Utils

# cc: okzyrox

import os

def is_in_path(path):
    return path in os.environ["PATH"]

def add_to_path(path):
    if not path in os.environ["PATH"]:
        os.environ["PATH"] = path + ";" + os.environ["PATH"]
        print("Added to path: " + path)
    
def remove_from_path(path):
    if path in os.environ["PATH"]:
        os.environ["PATH"] = os.environ["PATH"].replace(path + ";", "")
        print("Removed from path: " + path)
