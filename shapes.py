import turtle

turtle.Screen().bgcolor("#A6F5DB")

sc = turtle.Screen()
sc.setup(400, 300)

board = turtle.Turtle()


# triangle
board.forward(100)
board.left(120)

board.forward(100)

board.left(120)
board.forward(100)


# square
board.forward(100)
board.left(90)

board.forward(100)
board.left(90)

board.forward(100)
board.left(90)

board.forward(100)
board.left(90)

# star
board.forward(100)

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

board.penup()
board.right(90)
board.forward(100)

board.pendown()
board.right(90)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)
turtle.done()