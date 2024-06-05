# Windows Utils

# cc: okzyrox

import os

def add_to_path(path):
    """
    Adds a directory to the windows path
    """
    if not path in os.environ["PATH"]:
        os.environ["PATH"] = path + ";" + os.environ["PATH"]
        print("Added to path: " + path)
    
def remove_from_path(path):
    """
    Removes a directory from the windows path
    """
    if path in os.environ["PATH"]:
        os.environ["PATH"] = os.environ["PATH"].replace(path + ";", "")
        print("Removed from path: " + path)
