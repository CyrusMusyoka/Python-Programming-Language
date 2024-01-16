# using elif as it allows to check for different
# values in one condition after being checked
country = input("Where are you from ? ").upper()
if country == "CANADA" :
    print("Hello!")
# elif statement is not indented and
# it's short form of else if
elif country == "GERMANY" :
    print("Guten Tag!")
elif country == "FRANCE" :
    print("Bonjour!")
else:
    print("Have a nice day ahead.")