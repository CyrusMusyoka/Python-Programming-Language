# using  "OR" in statements
#means either way it will work as long as one condition is met
#declare two variables

saturday = True
sunday = False

#declare user input
comingDay = input("Which day are you coming over? ")

if comingDay == "saturday" or comingDay== "sunday" :
 print("you can sleep in.")
else:
    print("I wont be around")
