#shipping charges for a shopper
orderTotal = 0
shippingCost = 0
totalWithShopping = 0

#user amount input
orderTotal = float(input("What was your total for the order? "))
if orderTotal >= 50 :
    shippingCost = 0

else:
    shippingCost = 10

#calculate the total including shopping cost
totalWithShopping = orderTotal + shippingCost

print("Your total including shipping fee, will be: $%.2f " %totalWithShopping)


