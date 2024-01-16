import turtle

counter = 0
#angel = int(input("Enter size of angle to be used  "))

while counter < 4:
    # python starts counting from zero hence it will count
    # three, 0,1,2,3 since counter is initialized at 0
    turtle.color("red")
    turtle.forward(90)
    turtle.right(90)

    counter = counter + 1
    # is same has counter +=1
