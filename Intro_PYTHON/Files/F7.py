import csv

myFiles = "math.txt"
accessMode = "r"

with open(myFiles, accessMode) as mathFile:
    allRowList = csv.reader(mathFile)

    for currentRowList in allRowList:
     # print(currentRowList) # for each row
     print(';'.join(currentRowList))
     # for each row separating using commas
    for currentWordList in currentRowList:
          print(' '.join(currentWordList))
         # print(currentWordList) # each item in a row
