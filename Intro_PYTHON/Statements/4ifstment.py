#if statement with numbers
print("Deposit more than 100 to get a free toaster:")
# added float datatype ahead of input to convert the
# datattype from string to be float
deposit = float(input("How much do want to deposit? "))

if deposit > 100 :
    print("enjoy your toaster!")
    print("Have a nice day ahead.")

#another way to convert the datatype
deposit = input("How much do want to deposit? ")

if float(deposit) > 100 :
    print("enjoy your toaster!")
    print("Have a nice day ahead.")

