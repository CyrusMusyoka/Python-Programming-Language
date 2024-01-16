# making functions dynamic
# creating a function that accepts data we use parameters
# i.e def printMessage(message)
# print(message)

# when using multiples parameters, makes a function dynamic
# simply add them in, separated by commas

def displayMessage(greeting, name):
    message = greeting + ',' + name
    print(message)
    return


displayMessage("Hi", "Cyrus Musyoka, you been selected for the scholarship")
