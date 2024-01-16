import sys
first = input("Enter first number: ")
second = input("Enter second number: ")

firstNumber = float(first)
secondNumber = float(second)

try:
    result = firstNumber / secondNumber
    print(first + " / " + second + " = " + str(result))

except ZeroDivisionError:
    print("The answer is infinity")

except:
    error = sys.exc_info()[0]
    print("I am sorry, an error occurred")
    print(error)

finally:
    print('I will always run!!!!!!!!!!!')
