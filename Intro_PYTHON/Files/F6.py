# find the file location
myCont = "TESTpage.txt.txt"
accessMode = "r"

myFile = open(myCont, accessMode)
# myFile = open("TESTpage.txt.txt", "r")

# read all the content of the file
# allFileContent = myFile.read()
firstallFileContent = myFile.readline()
secondallFileContent = myFile.readline()

# print all file content
print(firstallFileContent)
print(secondallFileContent)