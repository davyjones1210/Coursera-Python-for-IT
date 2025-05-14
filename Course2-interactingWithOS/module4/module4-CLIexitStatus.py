# cat parameters.py 
# #!/usr/bin/env python3
# import sys
# print(sys.argv)

# ./parameters.py
# ['./parameters.py'] 

# ./parameters.py one two three
# ['./parameters.py', 'one', 'two', 'three']


# wc variables.py
# 7 19 174 variables.py 	
# echo $?
# 0

# wc notpresent.sh
# wc: notpresent.sh: No such file or directory
# echo $?
# 1

#!/usr/bin/env python3

import os
import sys

filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("New file created\n")
else:
    print("Error, the file {} already exists!".format(filename))
    sys.exit(1)

# ./create_file.py example
# echo $?
# 0

# cat example 
# New file created
# ./create_file.py example
# Error, the file example already exists!
# echo $?
# 1