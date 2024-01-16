# calculating electricity bill program

amountPay = 0

units = int(input("Enter number of electric unit: "))

if units <100 :
    amountPay = "no charges"

if units >100 and units <= 200 :
    amountPay = (units - 100)*5

if units >200 :
    amountPay = 500 + (units - 100)*10

print("Amount pay Rs %.2f" %amountPay)