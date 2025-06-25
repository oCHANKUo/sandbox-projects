import turtle
import time
import random

rows = 60
cols = 60
cellSize = 5

#cell states
OFF = 0
ON = 1
DYING = 2

colors = {
    OFF: "black",
    ON: "white",
    DYING: "red"
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

def create2DArray(row1, col1):
    return [[0 for _ in range(col1)] for _ in range(row1)]

grid = create2DArray(rows, cols)

# Initialize random ON cells to start the simulation
for r in range(rows):
    for c in range(cols):
        if random.random() < 0.02:  # 1% of the grid will be ON initially. Change this parameter for fun patterns
            grid[r][c] = ON

def drawCell(x, y, state):
    pen.goto((x - cols // 2) * cellSize, (rows // 2 - y) * cellSize)
    pen.fillcolor(colors[state])
    pen.begin_fill()
    for _ in range(4):
        pen.forward(cellSize)
        pen.right(90)
    pen.end_fill()


def countNeighbours(r, c):
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
    time.sleep(1/60)
    
    newGrid = create2DArray(rows, cols)
    for r in range(rows):
        for c in range(cols):
            state = grid[r][c]
            if state == OFF:
                if countNeighbours(r, c) == 2:
                    newGrid[r][c] = ON
            elif state == ON:
                newGrid[r][c] = DYING
            elif state == DYING:
                newGrid[r][c] = OFF

    # Only draw cells that changed
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != newGrid[r][c]:
                drawCell(c, r, newGrid[r][c])

    grid = newGrid
    screen.update()
