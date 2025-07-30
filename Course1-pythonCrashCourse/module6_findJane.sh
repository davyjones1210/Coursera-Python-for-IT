#!/bin/bash

# Create an empty file named oldFiles.txt
> oldFiles.txt

# Store the file names containing "jane" into the 'files' variable
files=$(grep " jane " ~/data/list.txt | cut -d ' ' -f 3)

echo "Files containing 'jane': $files"

# Iterate over the files variable and add a test expression within the loop.
# If the item within the files variable passes the test, add/append it to the file oldFiles.txt.
for file in $files; do
  # Construct the full path using the home directory
  full_path="$HOME$file"

  # Debugging output: Print the full path we're testing
  echo "Testing path: $full_path"

  if test -e "$full_path"; then
    echo "File '$full_path' exists"
    echo "$full_path" >> oldFiles.txt  # Append the full path to oldFiles.txt
  else
    echo "File '$full_path' doesn't exist"
  fi
done

# Verify the contents of oldFiles.txt
echo "Contents of oldFiles.txt:"
cat oldFiles.txt