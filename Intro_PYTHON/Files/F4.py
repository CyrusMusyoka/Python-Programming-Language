# writing into file reading from user

fileIn = "userInfo.txt"
WRITE = "w"

data = input("Please enter your user input: ")

fileName = open(fileIn, WRITE)
fileName.write(data)
fileName.close()