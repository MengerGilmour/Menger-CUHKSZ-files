import turtle
import time

# create the column trackers at the bottom of the board
def createColumnTrackers(x = -250, y = -290, cnt = 8, margin = 12):
    cols = []
    t = turtle.Turtle('square')
    t.up()
    t.shapesize(1,3,5) # 3-time wider, 5-pixel border
    sz = 60 + margin
    for i in range(cnt):
        t.goto(x + i*sz, y)
        cols.append(t)
        t = t.clone()
    return cols

# get the x position of mouse
def onMouseMotion(event):
    global pos_x
    x, y = event.x, event.y
    pos_x = x

# outline the trackers according to the x-position of the mouse
def checkcolumn():
    global turn
    for t in g_columns:
        pos = 300 + t.xcor()                  # center x position
        if abs(pos_x - pos) <= 30:
            if t.color()[0] == t.color()[1]:  # if not outlined
                if turn == 1:                 # outline blue for player1
                    t.color('blue', t.color()[1])
                else:                         # outline purple for player2
                    t.color('purple', t.color()[1])
        else:
            if t.color()[0] != t.color()[1]:  # if outlined
                t.color(t.color()[1])
    screen.ontimer(checkcolumn, 100)
    return

# draw the circle which could be filled with color
def draw_circle(x, y, r, color):
    turtle.speed(0)
    turtle.up()
    turtle.goto(x, y-r)
    turtle.seth(0)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(30, 360)
    turtle.end_fill()
    screen.update()

# this function is used to outline the circle when connect 4
def circle_outline(x,y,r,color):
    screen.tracer(0, 0)
    turtle.pencolor(color)
    turtle.pensize(5)
    turtle.speed(0)
    turtle.up()
    turtle.goto(x, y - r)
    turtle.seth(0)
    turtle.down()
    turtle.circle(30, 360)
    screen.update()

# this function is used to draw different color of the circle for each player
# example. player 1: blue, player 2: purple
def draw_pieces():
    global board
    row_gap = 72.5
    col_gap = 72.5
    for i in range(ROWS):
        Y = starty + (row_gap - 8) * i + row_gap / 2 + 8
        X = startx + col_gap / 2
        for j in range(COLS):
            if board[i][j] == 1:
                draw_circle(X, Y, 30, 'blue')
            else:
                draw_circle(X, Y, 30, 'purple')
            X += col_gap
        Y += row_gap

# 3 ways of success, end the game
def game_over(tt, turn, row, col):
    # check horizontals
    cnt = 1
    n = 4
    i = col + 1
    while i < COLS and tt[row][i] == turn:
        cnt, i = cnt + 1, i + 1

    i = col - 1
    while i >= 0 and tt[row][i] == turn:
        cnt, i = cnt + 1, i - 1

    if cnt >= 4:
        if i == col - 1:
            i = col + 3
            judge = -1
        else:
            i = i + 1
            judge = 1
        while n > 0:
            row_gap = 72.5
            col_gap = 72.5
            Y = starty + (row_gap - 8) * row + row_gap / 2 + 8
            X = startx + col_gap * i + col_gap / 2
            circle_outline(X, Y, 30, "red")
            X += col_gap
            i = i + judge
            n -= 1
        return turn

    # check vertical
    if row >= 3 and tt[row - 1][col] == turn and tt[row - 2][col] == turn and tt[row - 3][col] == turn:
        while n > 0:
            row_gap = 72.5
            col_gap = 72.5
            Y = starty + (row_gap - 8) * row + row_gap / 2 + 8
            X = startx + col_gap * col + col_gap / 2
            circle_outline(X, Y, 30, "red")
            row -= 1
            n -= 1
        return turn

    # check diag 1
    cnt = 1
    i = 1
    while row + i < ROWS and col + i < COLS and tt[row + i][col + i] == turn:
        cnt, i = cnt + 1, i + 1
    i = -1
    while row + i >= 0 and col + i >= 0 and tt[row + i][col + i] == turn:
        cnt, i = cnt + 1, i - 1
    if cnt >= 4:
        if i == -1:
            c = col + 3
            r = row + 3
            judge = -1
        else:
            c = col + i + 1
            r = row + i + 1
            judge = 1
        while n > 0:
            row_gap = 72.5
            col_gap = 72.5
            Y = starty + (row_gap - 8) * r + row_gap / 2 + 8
            X = startx + col_gap * c + col_gap / 2
            circle_outline(X, Y, 30, "red")
            r = r + judge
            c = c + judge
            n -= 1
        return turn

    # check diag 2
    cnt = 1
    i = 1
    while row + i < ROWS and col - i >= 0 and tt[row + i][col - i] == turn:
        cnt, i = cnt + 1, i + 1
    i = -1
    while row + i >= 0 and col - i < COLS and tt[row + i][col - i] == turn:
        cnt, i = cnt + 1, i - 1
    if cnt >= 4:
        if i == -1:
            c = col - 3
            r = row + 3
            cc = 1
            rr = -1
        else:
            c = col - i - 1
            r = row + i + 1
            cc = -1
            rr = 1
        while n > 0:
            row_gap = 72.5
            col_gap = 72.5
            Y = starty + (row_gap - 8) * r + row_gap / 2 + 8
            X = startx + col_gap * c + col_gap / 2
            circle_outline(X, Y, 30, "red")
            r = r + rr
            c = c + cc
            n -= 1
        return turn

    for i in range(COLS):
        if tt[ROWS - 1][i] == 0:
            return -2
    return 0

# place piece in col for every turn
def place_piece(tt, turn, col):
    for i in range(ROWS):
        if tt[i][col] == 0:
            tt[i][col] = turn
            return i

# create the array of x/y order to store the piece
def init_board():
    global board
    for i in range(8):
        row = []
        for j in range(8):
            row.append(0)
        board.append(row)

# connect the array to the specific position on board, can judge the player of this turn
def place_piece_and_draw(bb, turn, col):
    row = place_piece(bb, turn, col)
    row_gap = 72.5
    col_gap = 72.5
    Y = starty + (row_gap - 8) * row + row_gap / 2 + 8
    X = startx + col_gap * col + col_gap / 2 + 2
    i = row
    j = col

    if board[i][j] == 1:
        draw_circle(X, Y, 30, 'blue')
        screen.update()
        time.sleep(0.05)
        screen.title(" Connect 4 – Player 2 Turn")
    else:
        draw_circle(X, Y, 30, 'purple')
        screen.update()
        time.sleep(0.05)
        screen.title(" Connect 4 – Player 1 Turn")
    return row

# the whole process of the game, can judge the winner of the game
def play(x, y):
    global turn, working
    if working: return
    working = True
    cols = [-startx * 2 / 8 * i + startx - 2 * startx / 16 for i in range(8)]
    for i in range(len(cols)):
        if abs(x - cols[i]) < (-startx) / 16 * 2 / 3 and board[ROWS - 1][i] == 0:
            rn = place_piece_and_draw(board, turn, i)
            r = game_over(board, turn, rn, i)
            if r == 0:
                screen.title('tied')
            elif r == 1:
                screen.title('Winner ! Player 1')
                screen.exitonclick()
            elif r == -1:
                screen.title('Winner ! Player 2')
                screen.exitonclick()

            turn = -turn
    working = False

# the default data of the game
ROWS = 8
COLS = 8
startx = -290
starty = -290
WIDTH = 580
HEIGHT = 580
pos_x = -999
g_columns = []
screen = turtle.Screen()
screen.setup(600, 600)
screen.setworldcoordinates(-300, -300, 300, 300)
screen.title(" Connect 4 – Player 1 Turn")
g_columns = createColumnTrackers()
turtle.hideturtle()

c = screen.getcanvas()
c.bind('<Motion>', onMouseMotion)
screen.ontimer(checkcolumn, 10)
g_canvas = turtle.getcanvas()

board = []
init_board()
turn = 1
working = False
screen.onclick(play)
turtle.hideturtle()
screen.mainloop()

