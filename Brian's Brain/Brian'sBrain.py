import turtle

#screen setup
screen = turtle.Screen()
screen.bgcolor('black')
# screen.screensize(1000,1000)

def create2DArray(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]





rows = 10
cols = 10

grid = create2DArray(rows, cols)


#Brain()
turtle.done() # keeps the window up