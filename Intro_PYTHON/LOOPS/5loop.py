# nested loops = all about having
# another loop inside another  loop
import turtle

for steps in range(4):
    turtle.forward(100)
    turtle.right(90)
    # inner loop will run 16 times (4*4)
    # when outer loop runs ,inner loop runs 4 times
    # hence it will run 16 times after each 4 times in one time outer loop run
    for moresteps in range(4):
        turtle.forward(50)
        turtle.right(90)