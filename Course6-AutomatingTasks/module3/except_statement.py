# try:
#     # Try to open and write to the file
#     f = open("test_file.txt", "a+", encoding="utf-8")

try:
  # Try to append to a file that is normally not writable
  # for anyone other than root 
  f = open("test_file.txt", "a+")
  f.write("This is a test file.\n")
except IOError as ex:
  # The variable "ex" will hold details about the error
  # that occurred
  print("Error appending to file: " + str(ex))
else:
  # If there was no exception, close the file.
  f.close()