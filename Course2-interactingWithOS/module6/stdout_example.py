#!/usr/bin/env python3
# import sys
import glob

print(*glob.glob("*"), sep="\n")

print("Don't mind me, just a bit of text here...")

# with open("new_file.txt", "w") as f:
#     sys.stdout = f
#     print("Don't mind me, just a bit of text here...")
#     sys.stdout = sys.__stdout__