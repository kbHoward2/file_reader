import os
import sys

def get_file_text(filename):
    """Open contents of a file, return a buffer of content"""
    contents = []
    try:
        with open(filename, "r") as file:
            contents = file.readlines()
            return contents
    except FileNotFoundError:
        print(f"'{filename}' not found.")
        sys.exit(-1)

def cycle_lines(content):
    """Process lines read in by the file. Default increments each cycle by 10 lines."""
    incr = 10
    curr_pos = 0 

    while input("Press Enter to Continue: ").lower() != "q":
    
        # This while loop prevents accessing indexes beyond the list range.
        while (curr_pos + incr >= len(content)):
            incr = int(incr / 2)
        
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
        sys.exit(-1)

if __name__ == "__main__":
    main()