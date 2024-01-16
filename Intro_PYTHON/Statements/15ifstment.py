#calculating total charge from an online store in CANADA
charge = 0
tax = 0
totalCharge = 0
taxProvince = 0

userCountry = input("What country are you from? ").upper()
charge = float(input("How much was your charges? "))
userProvince = input("What province are you from in CANADA? (if not from canada enter space)").upper()

if not userCountry == "CANADA":
    print("The order does not have tax charges.")

elif userCountry == "CANADA":
    if userProvince == "ALBERTA" :
        tax = (charge * 0.05)
    if userProvince == "ONTARIO" or userProvince == "NEW BRUNSWICK" or userProvince == "NOVA SCOTIA" :
        tax = (charge * 0.13)
    else:
     userProvince == "OtherProvince"
    tax = (charge * 0.06)+(charge * 0.05)

totalCharge = (charge +  tax )
print("totalCharge $%.2f " %totalCharge)
