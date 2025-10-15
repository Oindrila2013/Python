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

board.penup()
board.forward(60)


# square
board.pendown()
board.forward(100)
board.left(90)

board.forward(100)
board.left(90)

board.forward(100)
board.left(90)

board.forward(100)
board.left(90)

board.penup()


# star
board.right(110)
board.forward(80)
board.pendown()
board.forward(100)

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)

board.pendown()
board.right(90)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)
turtle.done()