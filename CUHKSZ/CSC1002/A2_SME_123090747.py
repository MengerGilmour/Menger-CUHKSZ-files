import turtle as t
import numpy as np
import random
import time

# Setup the game window and turtle
def setup_game():
    t.setup(500, 500)
    t.speed(0)
    t.colormode(255)
    t.color("white")
    t.fillcolor("blue")
    t.bgcolor("white")
    t.pensize(4)
    t.hideturtle()

# Draw a single puzzle tile
def draw_tile(i, j, number, white=False, over=False):
    # Set fill color based on parameters
    if white:
        t.fillcolor("#ffffff")
    else:
        t.fillcolor("#1780db")

    if over:
        t.fillcolor("red")

    # Draw the tile
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

# Draw animation frames for tile movement
def draw_every_frame(i_from, j_from, i_to, j_to):
    old = (i_from, j_from)
    frames = 5
    all_count = (frames) * (frames + 1) * (2 * frames + 1) // 6
    now_sum = 0

    # Global variables that control the animation state
    global animation_lock
    animation_lock = True

    for x in range(frames):
        now_sum += (x + 1) * (x + 1)
        new = (i_from + (i_to - i_from) / all_count * now_sum, j_from + (j_to - j_from) / all_count * now_sum)
        draw_tile(old[0], old[1], puzzle[i_to][j_to], True)
        draw_tile(new[0], new[1], puzzle[i_to][j_to])
        old = new

        t.update()
        time.sleep(0.01)

    animation_lock = False

# Find the position of the empty tile
def find_empty_tile():
    return next((i, j) for i in range(n) for j in range(n) if puzzle[i][j] == 0)


# Check if two tiles are adjacent
def is_adjacent(row1, col1, row2, col2):
    return abs(row1 - row2) + abs(col1 - col2) == 1

# Shuffle the puzzle tiles
import random

def shuffle_puzzle():
    for _ in range(100):
        row, col = find_empty_tile()  # Find the empty tile's current position
        moveable = []  # List to store possible moves

        # Potential moves: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Check each possible move's validity and add it to 'moveable' if valid
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < n and 0 <= new_col < n:  # Ensure move is within bounds
                moveable.append((new_row, new_col))

        # Randomly select a valid move and execute it
        move_row, move_col = random.choice(moveable)
        move_tile(move_row, move_col, True)

    draw_puzzle()  # Redraw the puzzle after shuffling


# Draw the entire puzzle
def draw_puzzle(over=False):
    t.clear()
    for i in range(n):
        for j in range(n):
            draw_tile(i, j, puzzle[i][j], False, over)

# Move a tile
def move_tile(row, col, auto=False):
    empty_row, empty_col = find_empty_tile()

    if is_adjacent(row, col, empty_row, empty_col) and can_move(row, col):
            puzzle[row][col], puzzle[empty_row][empty_col] = (
                puzzle[empty_row][empty_col], puzzle[row][col]
            )
            if not auto:
                draw_every_frame(row, col, empty_row, empty_col)

# Check if a tile can be moved
def can_move(row, col):
    if row < 0 or row >= n or col < 0 or col >= n:
        return False
    empty_row, empty_col = find_empty_tile()
    return (row == empty_row and abs(col - empty_col) == 1) or \
           (col == empty_col and abs(row - empty_row) == 1)

# Check if the puzzle is solved
def if_recovered(puzzle):
    return np.array_equal(puzzle, np.array(numbers).reshape(n, n))

# Handle click events
def on_click(x, y):
    if animation_lock:  # Do nothing if animations are currently locked
        return

    # Calculate the row and column from the click coordinates
    row, col = calculate_grid_position(x, y)

    # Move the tile if it's movable
    if can_move(row, col):
        move_tile(row, col)

    # Check if the puzzle is solved and display a congratulatory message
    if if_recovered(puzzle):
        display_congratulations()

def calculate_grid_position(x, y):
    row = int((n * 40 - y) // 80)
    col = int((x + n * 40) // 80)
    return row, col

def display_congratulations():
    draw_puzzle(True)  # Draw the final state of the puzzle
    t.update()
    time.sleep(1)  # Pause to let the user see the completed puzzle
    t.clear()  # Clear the puzzle for the message
    t.penup()
    t.goto(0, 0)
    t.color("red")
    t.write("Congratulations!", align="center", font=("Arial", 28, "normal"))


# Initialize the game
setup_game()

# Prompt user for puzzle size
n = int(t.numinput(
    "Puzzle Size", "Enter the size of the game (3, 4, or 5):",
    default=3, minval=3, maxval=5))

# Generate initial puzzle layout
numbers = list(range(1, n * n)) + [0]
puzzle = np.array(numbers)
puzzle = puzzle.reshape((n, n))

# Global variables that control the animation state
animation_lock = False

# Shuffle the puzzle
shuffle_puzzle()

# Set the handler for mouse click events
t.onscreenclick(on_click)

# Draw the initial puzzle
draw_puzzle()

# Start the event loop
t.mainloop()
