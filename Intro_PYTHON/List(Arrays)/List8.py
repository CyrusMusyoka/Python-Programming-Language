# finding how many entries are in the list
# before printing output
# use of len() function to find out how many entries are in the list

# our guest list
guest = ['cyrus', 'alice', 'evans', 'thomas', 'mutua', 'mueni']

# Find out how many entries are in the list
nbrEntries = len(guest)

# create a loop that executes once for each entry
for steps in range(nbrEntries):
    print(guest[steps])
