# writing into a file

fileName = "GuestList.txt"
accessMode = "w"
# WRITE = "w+" w+ means read/write

myFile = open(fileName, accessMode)
myFile.write("Hi there!\n")
myFile.write("How are you?\n")
myFile.write("Am Cyrus Musyoka, a software developer, are you hiring?")

print("File written successfully.")
# when your finished with writing your code use close() method
myFile.close()
