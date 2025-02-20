import os
import sys

def get_file_text(filename):
    """Open contents of a file, return a buffer of content"""
    content = []
    try:
        with open(filename, "r") as file:
            contents = file.readlines()
            return contents
    except FileNotFoundError:
        print(f"'{filename}' not found.")

def check_eof(curr_pos, incr, content):
    """ This function prevents accessing indexes beyond a list's range."""
    while (curr_pos + incr >= len(content)):
        incr = int(incr / 2)

    return incr

def cycle_lines(content):
    """
        Process lines read in by the file. Default increments each cycle by 10 lines.
    """
    incr = 1000
    curr_pos = 0 

    while input("Press Enter to Continue: ").lower() != "q":
    
        incr = check_eof(curr_pos, incr, content)
        for i in range(curr_pos, curr_pos+incr):
            print(f"{i} {content[i]}")
        
        curr_pos += incr
        if curr_pos == len(content) - 1:
            print(content[-1]) # Print the final line of the file.
            break
        
def main():
    filepath = None
    if len(sys.argv) > 1:
        filepath = sys.argv[1] 
        cycle_lines(get_file_text(filepath))
    else:
        print("No File Argument\n")

if __name__ == "__main__":
    main()