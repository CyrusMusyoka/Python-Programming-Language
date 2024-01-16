# easier way to print items in a list

# our list
guests = ['alice', 'cyrus', 'evans', 'thomas', 'jenifer']

# sorting the list names in alphabetical order
guests.sort()


# specify the name of your list and a variable name
# to  hold each entry as you go through the loop
for guest in guests:
    # variable guest will contain values of the list guests
    # as we go through the loop
    print(guest)