import os
def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, "w") as file:
    file.write(comments)
  filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))


import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  print(os.path.isdir(directory))
  if os.path.isdir(directory) == False:
    os.mkdir(directory)
  print(os.getcwd())
  # Create the new file inside of the new directory
  os.chdir(directory)
  print(os.getcwd())
  with open (filename, "w") as file:
    pass
  print(os.getcwd())
  print(os.listdir(directory))
  # Return the list of files in the new directory
  return os.listdir(directory)

print(new_directory("PythonPrograms", "script.py"))

import os
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
  relative_parent = os.path.join(os.getcwd(), '..')

  # Return the absolute path of the parent directory
  return relative_parent

print(parent_directory())



import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(directory)
    os.getcwd()
  # Create the new file inside of the new directory
  os.chdir(directory)
  with open (filename, "w") as file:
    pass
  # Return the list of files in the new directory
  return os.listdir(directory)

print(new_directory("PythonPrograms", "script.py"))