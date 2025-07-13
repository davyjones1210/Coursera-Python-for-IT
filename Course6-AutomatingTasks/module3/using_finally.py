try:
  f = open("test_file.txt", "a+")
  f.write("\nSuccess!")
except Exception as ex:
  print("Error appending to file: " + str(ex))
finally:
  f.close()  # causes error if the file could not be opened