import turtle

noSides = int(input("Enter number of sides to draw: "))
for sides in range(noSides):
    turtle.forward(100)
    turtle.right(360/noSides)
    for sides in range(noSides):
        turtle.forward(50)
        turtle.right(360/noSides)