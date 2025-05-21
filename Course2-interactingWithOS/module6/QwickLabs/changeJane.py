import sys
import subprocess
import os
# Get the filename from the first command line argument
filename = sys.argv[1]

# Open the file and read all lines
with open(filename, "r") as f:
    for line in f.readlines():
        old_name = "/home/student"+ line.strip()
        new_name = old_name.replace("jane", "jdoe")
        print("old_name: ", old_name)
        print("new_name: ", new_name)
        # Check if the file exists before renaming
        if os.path.exists(old_name):
            subprocess.run(["mv", old_name, new_name])
        else:
            print(f"File does not exist: {old_name}")
# ls /data/jane_profile_07272018.doc

# ls /student/data/jane_profile_07272018.doc

# ls /home/student/data/jane_profile_07272018.doc

# ls /home/student/data/jane_profile_07272018.doc

# if test -e ~/data/jane_profile_07272018.doc; then echo "File exists"; else echo "File doesn't exist"; fi

# #!/usr/bin/env python3
# import sys
# import subprocess
# with open(sys.argv[1]) as file:
#     lines = file.readlines()
#     for line in lines:
#         oldvalue = line.strip()
#         newvalue = oldvalue.replace("jane", "jdoe")
#         subprocess.run(["mv", oldvalue, newvalue])
# file.close()
