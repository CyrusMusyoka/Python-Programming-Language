# creating a CSV file (character/comma separated values)

fileName = "marks.csv"
accessMode = "w"

myFile = open(fileName, accessMode)
myFile.write("Cyrus Musyoka, 70\n")
myFile.write("Alice Malwa, 57\n")
myFile.write("Evans Mulingata, 76\n")
myFile.write("Thomas Mutua, 63")

myFile.close()
print("File written successfully")