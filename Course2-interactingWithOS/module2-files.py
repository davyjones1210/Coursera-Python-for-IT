import os
import datetime
# # #Windows file directory
print(os.path.getsize("spider.txt"))
#This code will provide the file size

print(os.path.getmtime("spider.txt"))
#This code will provide a unix timestamp for the file


timestamp = os.path.getmtime("spider.txt")
print(datetime.datetime.fromtimestamp(timestamp))
#This code will provide the date and time for the file in an 
#easy-to-understand format


print(os.path.abspath("spider.txt"))
#This code takes the file name and turns it into an absolute path


# Create a directory and move a file from one directory to another
# using low-level OS functions.

# import os

# Check to see if a directory named "test1" exists under the current
# directory. If not, create it:
dest_dir = os.path.join(os.getcwd(), "test1")
src_dir = os.path.join(os.getcwd(), "sample_data")
if not os.path.exists(src_dir):
    os.mkdir(src_dir)
if not os.path.exists(dest_dir):
 os.mkdir(dest_dir)


# Construct source and destination paths:
src_file = os.path.join(os.getcwd(), "sample_data", "README.md")
dest_file = os.path.join(os.getcwd(), "test1", "README.md")


# Move the file from its original location to the destination:
os.rename(src_file, dest_file)

# Create a directory and move a file from one directory to another
# using Pathlib.

from pathlib import Path

# Check to see if the "test1" subdirectory exists. If not, create it:
dest_dir = Path("./test1/")
if not dest_dir.exists():
  dest_dir.mkdir()

# Construct source and destination paths:
src_file = Path("./sample_data/README.md")
dest_file = dest_dir / "README.md"

# Move the file from its original location to the destination:
src_file.rename(dest_file)
