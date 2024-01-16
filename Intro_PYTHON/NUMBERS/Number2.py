area = 0.0
height = 20.0
width = 10.0

# calc area of a triangle
area = (height*width )/ 2.0
# printing formatted float value with 2 decimals places
print( "The area of the triangle will be %.2f" % area )

#printing with zero decimals
print( "The area of the triangle will be %03d" % area )

print("my favourate number is %d!!! " %10)
# print formatted decimal number with right justified to take up 6 spaces
#with leadind zeros
print("my favourate number is %06d!!! " %10)

# do .format syntax  on the same thing to include numbers in our output
print("the area of the triangle will be {0:f}".format(area))
print("the area of the triangle will be {0:d}".format(50))
print("My favourate number is {0:d}".format(19))

#
print("Here is this three numbers! " +
      "The first is {0:d} The second is {1:8d} The third is {2:d}".format(7,8,9))