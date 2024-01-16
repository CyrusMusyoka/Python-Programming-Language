# Removing value from a list. we use name.remove(value)

guest = ['Alice', 'Evans', 'Cyrus', 'Thomas']

# remove cyrus from the list

guest.remove('Cyrus')
# display  values of the list

print(guest)

# alternative, use of delete command

guest = ['Alice', 'Evans', 'Cyrus', 'Thomas']
# print first item
print(guest[0])

# delete the first item in the list
del guest[0]

# print first item
print(guest[0])

# still pop can be used to remove an item from a list
guest = ['Alice', 'Evans', 'Cyrus', 'Thomas']
guest.pop(1)
print(guest)
