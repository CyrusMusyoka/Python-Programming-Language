# creation of a loan calculator
# loan amount
loanAmount=0
noYears=0
interestRate=0
noPayments=0
monthlyPay =0
#user entry
loanAmount = input("Please enter loan amount:")

#period for the loan in yearly
noYears = input("Enter amount of time for the loan:")

#payments in monthly for the loan in installments
noPayments = input("Enter no of payments:")

interestRate = input("Enter agreed Interest Rate for the loan:")
#Convert the strings into floating numbers so we can use them in teh formula
loanAmount = float(loanAmount)
monthlyPay = float(monthlyPay)
interestRate = float(interestRate)
noPayments = float(noPayments)

#Since payments are once per month, number of payments is number of years for the loan * 12
noPayments = noPayments*12

#monthlyPay = (loanAmount * interestRate * (1+interestRate) * noPayments / ((1+interestRate) * noPayments-1))/noPayments
monthlyPay = loanAmount * (interestRate/12)
#Calculate the monthly payment based on the formula
#monthlyPayment = loanAmount * interestRate * (1+ interestRate) * numberOfPayments \
 #   / ((1 + interestRate) * numberOfPayments -1)



print( loanAmount )
print("Duration: "+ noYears +" years")
print("Your monthly payment will be Ksh %.2f" % monthlyPay)