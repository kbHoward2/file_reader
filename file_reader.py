import os
import sys

def get_file_text(filename):
    """Open contents of a file, return a buffer of content"""
    contents = []
    try:
        with open(filename, "r") as file:
            contents = file.read().splitlines()
            return contents
    except FileNotFoundError:
        print(f"{filename} Not Found")
        return None

def cycle_lines(content):
    incr = 10
    curr_pos = 0 
    while input("Press Enter to Continue: ").lower() != "q":
        for i in range(curr_pos, curr_pos+incr):
            print(f"{content[i]}" )
            curr_pos += incr
        
def main():
    filepath = None

    if len(sys.argv) > 1:
        filepath = sys.argv[1] 

        cycle_lines(get_file_text(filepath))
    else:
        print("No File Input\n")

if __name__ == "__main__":
    main()