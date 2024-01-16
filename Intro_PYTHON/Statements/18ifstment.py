# finding the last digit of a number is divisible by three or not

Num = int(input("Enter an integer: "))

idNum = Num % 10
#display last number
print("The last digit is %.1f" %idNum)

#finding if its divisible by 3
if idNum %3 == 0:
    print("The number is divisible by 3")
else:
    print("The number is not divisible by 3")

print("The number is: %.1f" %Num)