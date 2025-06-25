import turtle

rows = 100
cols = 100
cellSize = 10

#cell states
OFF = 0
ON = 1
DYING = 2

colors = {
    OFF: "black",
    ON: "white",
    DYING: "reds"
}


# screen setup
screen = turtle.Screen()
screen.bgcolor('black')
screen.tracer(0)
# screen.screensize(1000,1000)

# pen to draw the grid
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)

def create2DArray(rows, cols):
    return [[OFF for _ in range(cols)] for _ in range(rows)]

grid = create2DArray(rows, cols)


def drawCell(x, y, state):
    pen.goto((x - cols // 2) * cellSize, (rows // 2 - y) * cellSize)
    pen.fillcolor(colors[state])
    pen.begin_fill()
    for _ in range(4):
        pen.forward(cellSize)
        pen.right(90)
    pen.end_fill()


def coutNeighbours(r, c):
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr = r + dr
            nc = c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == ON:
                    count += 1
    return count

# main loop
while True:
    pen.clear()
    for r in range(rows):
        for c in range(cols):
            drawCell(c, r, grid[r][c])
    screen.update()

    newGrid = create2DArray()
    for r in range(rows):
        for c in range(cols):
            state = grid[r][c]
            if state == OFF:
                if countNeighbours(r, c) == 2:
                    newGrid[r][c] = ON # set state to ON
            elif state == ON:
                newGrid[r][c] = DYING
            elif state == OFF:
                newGrid[r][c] = OFF
    grid = newGrid

#Brain()
turtle.done() # keeps the window up