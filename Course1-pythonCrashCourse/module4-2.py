# # Create a list of tuples where each tuple contains the numbers 1, 2, and 3.
# numbers = [(1, 2, 3) for _ in range(5)]
# print(numbers)


# Create a dictionary to demonstrate the functionality
my_dict = {
    "fruits": ["apple", "banana"],
    "vegetables": ["carrot", "broccoli"]
}

# Create a dictionary to demonstrate the functionality
my_dict = {
    "fruits": ["apple", "banana"],
    "vegetables": ["carrot", "broccoli"]
}

# Add values to keys, adding a new key if it does not exist
key = "fruits"
value = "orange"
if key in my_dict:
    my_dict[key].append(value)
else:
    my_dict[key] = [value]  # Create a new key with the value as a list

key = "vegetables"
value = "spinach"
if key in my_dict:
    my_dict[key].append(value)
else:
    my_dict[key] = [value]  # Create a new key with the value as a list

key = "meats"
value = "chicken"
if key in my_dict:
    my_dict[key].append(value)
else:
    my_dict[key] = [value]  # Create a new key with the value as a list

print(my_dict)