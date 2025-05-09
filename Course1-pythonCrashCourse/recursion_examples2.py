# def get_members(group):
#   pass

# def is_group(member):
#   pass

# def count_users(group):
#   count = 0
#   for member in get_members(group):
#     count += 1
#     if is_group(member):
#       count += count_users(member)
#   return count


# print(count_users("sales")) # Should be 3
# print(count_users("engineering")) # Should be 8
# print(count_users("everyone")) # Should be 18


# for count in range(1, 6):
#     print(count+1)


for x in range(10):
    for y in range(x):
        print(y)