import turtle

rows = 10
cols = 10
cellSize = 10

#screen setup
screen = turtle.Screen()
screen.bgcolor('black')
# screen.screensize(1000,1000)

def create2DArray(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]


def drawCell(x, y, state):
    if state == 0:
        grid.fillcolor('black')


def drawGrid():
    for row in range(rows):
        for col in range(cols):
            x = col * cellSize - (cols * cellSize // 2)
            y = row * cellSize - (rows * cellSize // 2)
            drawCell(x, y, grid[row][col])


grid = create2DArray(rows, cols)


#Brain()
turtle.done() # keeps the window up