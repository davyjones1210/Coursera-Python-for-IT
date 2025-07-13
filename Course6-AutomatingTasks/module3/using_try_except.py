try:
  print(x)
except NameError:
  print("Variable x is not defined")

# Another example below

try:
  f = open("test_file.txt", "a+")
  f.write("Success!")
except FileNotFoundError:
  print("Data file not found")
except Exception as ex:
  print("Error appending to file: " + str(ex))
else:
  f.close()