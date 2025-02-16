import os
import sys

buffer_size = 1024

def get_file_text(filename):
    """Open contents of a file, return a buffer of content"""
    contents = ''
    try:
        with open(filename, "r") as file:
            while True:
                buffer = file.read(buffer_size)
                if not buffer:
                    break
                contents +=  buffer
    except FileNotFoundError:
        print("File Not Found")
        pass
    return contents

filepath = None
if len(sys.argv) > 1:
    filepath = sys.argv[1] 
    get_file_text(filepath)
else:
    print("No File Input\n")
