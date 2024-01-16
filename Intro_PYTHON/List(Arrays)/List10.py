# challenge exercise

guests = []
name = " "

while name !=  "DONE" :
    name = input("Enter guest name (enter 'DONE' if no more names:) ")
    guests.append(name)

guests.sort()

for guest in guests:
    print(guest)
