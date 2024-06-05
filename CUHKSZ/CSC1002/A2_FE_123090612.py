import turtle as t
import numpy as np
import random
import time

# Set window size.
t.setup(500, 500)

# Set brush speed.
t.speed(0)

t.colormode(255)

# Set brush color.
t.color("white")

# Set fill color.
t.fillcolor("blue")

# Set background color.
t.bgcolor("white")

# Set brush thickness.
t.pensize(4)

# Hide brush.
t.hideturtle()

# Prompt user to input game size.
n = int(t.numinput(
    "Puzzle Size", "Enter the size of the game (3, 4, or 5):",
    default=3, minval=3, maxval=5))

# Generate a random solvable puzzle.
numbers = list(range(1, n * n)) + [0]
puzzle = np.array(numbers)
puzzle = puzzle.reshape((n, n))

# No operation allowed during animation.
animationLock = False


# Draw puzzle.
def drawPuzzle(over=False):
    t.clear()
    for i in range(n):
        for j in range(n):
            drawTile(i, j, puzzle[i][j], False, over)

"""
# Draw puzzle piece.
def drawTile(i, j, number):
    t.tracer(False)
    t.penup()
    t.goto(int(j * 80 - n * 40), int(n * 40 - i * 80))
    t.pendown()
    if number != 0:
        t.begin_fill()
        for _ in range(4):
            t.forward(80)
            t.right(90)
        t.end_fill()
        t.penup()
        t.goto(j * 80 - n * 40 + 20, n * 40 - i * 80 - 60)
        t.pendown()
        t.write(number, align="left", font=("Arial", 24, "normal"))
"""

def drawTile(i, j, number, white=False, over=False):
    if white:
        t.fillcolor("#ffffff")
    else:
        t.fillcolor("#1780db")

    if over:
        t.fillcolor("red")

    t.tracer(False)
    t.penup()
    t.goto(int(j * 80 - n * 40), int(n * 40 - i * 80))
    t.pendown()
    if number != 0:
        t.begin_fill()
        for _ in range(4):
            t.forward(80)
            t.right(90)
        t.end_fill()
        if not white:
            t.penup()
            t.goto(int(j * 80 - n * 40 + 20), int(n * 40 - i * 80 - 60))
            t.pendown()
            t.write(number, align="left", font=("Arial", 24, "normal"))


def drawEveryFrame(i_from, j_from, i_to, j_to):
    old = (i_from, j_from)
    frames = 5
    allCount = (frames) * (frames + 1) * (2 * frames + 1) // 6
    nowSum = 0

    animationLock = True
    for x in range(frames):
        nowSum += (x + 1) * (x + 1)
        new = (i_from + (i_to - i_from) / allCount * nowSum, j_from + (j_to - j_from) / allCount * nowSum)
        drawTile(old[0], old[1], puzzle[i_to][j_to], True)
        drawTile(new[0], new[1], puzzle[i_to][j_to])
        old = new

        t.update()
        time.sleep(0.01)
    #drawPuzzle()
    animationLock = False

    """
    for x in range(1, 3):
        if i_from == i_to:
            posorneg = 1 if j_from < j_to else -1
            t.clear()
            for i in range(n):
                for j in range(n):
                    if i == i_to and j == j_to:
                        continue
                    if i != i_from or j != j_from:
                        drawTile(i, j, puzzle[i][j])
                    elif i == i_from and j == j_from:
                        drawTile(i, j + posorneg * x / 2, puzzle[i][j])
            t.update()
            time.sleep(0.01)
        elif j_from == j_to:
            posorneg = 1 if i_from < i_to else -1
            t.clear()
            for i in range(n):
                for j in range(n):
                    if i == i_to and j == j_to:
                        continue
                    if i != i_from or j != j_from:
                        drawTile(i, j, puzzle[i][j])
                    elif i == i_from and j == j_from:
                        drawTile(i + posorneg * x / 2, j, puzzle[i][j])
            t.update()
            time.sleep(0.01)
    """


# Check for restoration.
def ifRecovered(puzzle):
    return np.array_equal(puzzle, np.array(numbers).reshape(n, n))


# Wait for user click.
def onClick(x, y):
    if animationLock:
        return
    # Calculate the position of the clicked puzzle piece.
    row = int((n * 40 - y) // 80)
    col = int((x + n * 40) // 80)

    # Check if the clicked puzzle piece can be moved, if so, move it.
    if canMove(row, col):
        moveTile(row, col)

    # If the puzzle has been restored, display a congratulatory message.
    if ifRecovered(puzzle):
        drawPuzzle(True)
        t.update()
        time.sleep(1)
        t.clear()
        t.penup()
        t.goto(0, 0)
        t.color("red")
        t.write("Congratulations!",
                align="center",
                font=("Arial", 28, "normal"))


# Check if the puzzle piece can be moved.
def canMove(row, col):
    if row < 0 or row >= n or col < 0 or col >= n:
        return False
    empty_row, empty_col = findEmptyTile()
    if (row == empty_row and abs(col - empty_col) == 1) or \
            (col == empty_col and abs(row - empty_row) == 1):
        return True
    return False


# Move the puzzle piece.
def moveTile(row, col, auto=False):
    # Get the position of the blank puzzle piece.
    empty_row, empty_col = findEmptyTile()

    # Check if the clicked puzzle piece is adjacent to the blank puzzle piece.
    if isAdjacent(row, col, empty_row, empty_col):
        if canMove(row, col):
            # Swap the positions of the clicked puzzle piece and the blank puzzle piece.
            puzzle[row][col], puzzle[empty_row][empty_col] = (
                puzzle[empty_row][empty_col], puzzle[row][col]
            )
            # Redraw the puzzle.
            if not auto:
                drawEveryFrame(row, col, empty_row, empty_col)
                # drawPuzzle()


# Find the position of the blank puzzle piece.
def findEmptyTile():
    for i in range(n):
        for j in range(n):
            if puzzle[i][j] == 0:
                return i, j


# Check if two puzzle pieces are adjacent.
def isAdjacent(row1, col1, row2, col2):
    return abs(row1 - row2) + abs(col1 - col2) == 1


def shufflePuzzle():
    for _ in range(100):
        row, col = findEmptyTile()
        moveable = []
        if row > 0:
            moveable.append((row - 1, col))
        if row < n - 1:
            moveable.append((row + 1, col))
        if col > 0:
            moveable.append((row, col - 1))
        if col < n - 1:
            moveable.append((row, col + 1))
        move_row, move_col = random.choice(moveable)
        moveTile(move_row, move_col, True)
    drawPuzzle()


shufflePuzzle()

# Set the handler for mouse click events.
t.onscreenclick(onClick)

# Start drawing the puzzle.
drawPuzzle()

# Start the event loop.
t.mainloop()
