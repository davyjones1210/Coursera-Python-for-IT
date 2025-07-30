#!/usr/bin/env python3

import sys
import subprocess

def replace_jane_with_jdoe(filename):
    """Replaces 'jane' with 'jdoe' in a filename using the mv command."""
    new_filename = filename.replace("jane", "jdoe")
    try:
        subprocess.run(["mv", filename, new_filename], check=True)
        print(f"Renamed '{filename}' to '{new_filename}'")
    except subprocess.CalledProcessError as e:
        print(f"Error renaming '{filename}': {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: changeJane.py oldFiles.txt")
        sys.exit(1)

    old_files_txt = sys.argv[1]

    try:
        with open(old_files_txt, "r") as f:
            for line in f:
                old_filename = line.strip()
                replace_jane_with_jdoe(old_filename)
    except FileNotFoundError:
        print(f"Error: File '{old_files_txt}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)