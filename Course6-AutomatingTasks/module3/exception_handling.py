# instead of doing this:

if isinstance(user, dict) and "first_name" in user:
  first_name = user["first_name"]

# Do this instead:
try:
  first_name = user["first_name"]
except KeyError:
  print("User does not have a first_name field")