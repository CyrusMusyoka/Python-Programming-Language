# writing information to a file with code, use
# open function() and create open file
# myFile = open(fileName, accessMode) whereby you must
# specify fileName and accessMode
# fileName  is the name of your file including extension
# data.txt or mytimes.csv and
# accessMode specifies what you will do with the file
# after you open it as follows 'r' = Read the file
# 'w' = Write to the file 'a' = append to the existing file content
# 'b' = open a binary file such as images, audio files and video files

fileName = 'demo.txt'

# when we use WRITE acessMode ,it writes files, and
# it overrates even if you add files in the backend to initial written file
# WRITE = 'w'
APPEND = 'a'
# APPEND access mode it adds content in the file ,doesn't overwrite when code is ran again
file = open(fileName, mode=APPEND)
# mode = WRITE