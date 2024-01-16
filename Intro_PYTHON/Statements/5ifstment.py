# using boolean variables to remember
# if a condition is true
freeToaster = False

deposit = input("How much would you like it deposit? ")
if float(deposit) > 100:
    #set boolean variable freeToaster to true
    freeToaster = True

#if boolean variable freeToaster is true
#the print statement will execute
if freeToaster :
    # you can also use
    #if freeToaster == True:
    print("Enjoy your Toaster...")
print("Thank you for shopping with us. \
Have a good day.")

