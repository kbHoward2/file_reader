import os
import sys

def open_file(filename):
    """Open contents of a file, return a buffer of content"""
    contents = []
    try:
        with open(filename, "r") as file:
            for lines in file:
                contents.append(lines.rstrip())
    except FileNotFoundError:
        print("File Not Found")
        pass
    return contents

def read_file(filepath):
    line_buffer = 10 
    current_index = 0
    contents = open_file(filepath)

    while (current_index < len(contents)):
        os.system('clear')
        for i in range(line_buffer):
            if (current_index >= len(contents)):
                break
            else:
                print(f"{current_index+1} {contents[current_index]}")
                current_index += 1
        user_input = input("Press Enter to Continue or q to quit: ")
        if user_input == 'q':
            break

filepath = None
if len(sys.argv) > 1:
    filepath = sys.argv[1] 
    read_file(filepath)
else:
    print("No File Input\n")
