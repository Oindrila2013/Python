import turtle

turtle.Screen().bgcolor("#AEE5F4")

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

turtle.done()