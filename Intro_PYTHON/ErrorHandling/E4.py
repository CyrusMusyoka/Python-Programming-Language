import sys

first = input("Enter first number: ")
second = input("Enter the second number: ")

firstNumber = float(first)
secondNumber = float(second)

try:
    result = firstNumber / secondNumber
    print(first + " / "+ second+ " = "+ str(result))
    errorFlag = False

except ZeroDivisionError:
    print("The answer is infinity...")
    errorFlag = True

if not errorFlag:
    print("This message is displayed if there is no error!!!!!!!!!!!")