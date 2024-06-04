import time
import turtle
import random

# set basic value for the game Area
areaM = [(-250, -290), (250, -290), (250, 210), (-250, 210)]
areaS = [(-250, 210), (250, 210), (250, 290), (-250, 290)]

# Set the original value for food
foodEaten = []
food_pos = []
food = [None] * 5
foodAppear = [True] * 5
change_time = 3

# Set the original value for snake
Last_direction = "pause"
Last_move = "pause"
snakebody_pos = []
snakeLength = 6      # The start length of snake is 5
snakeSpeed = 200         # The initial speed of a snake is 200
if_pause = False
if_running = True
pause_status = 1             # 1 is the initial value, meaning 'pause'

# Set the original value for monster
number_contact = 0

# Define a function to randomly change the visibility of the food every 5-10 seconds
def foodVisibility():
    global foodAppear, change_time, start_time
    if (time.time() - start_time) > change_time:
        change_time += random.randint(5, 10)
        if if_running:
            i = random.randint(0, 4)
            while i in foodEaten:
                i = random.randint(0, 4)
            foodAppear[i] = not foodAppear[i]
            changeVisibility(i)

# Define a function to randomly update food visibility
def changeVisibility(i):
    global foodAppear
    if foodAppear[i]:
        # If food is visible, reshow it
        food[i].goto(food_pos[i][0], food_pos[i][1] - 10)
        food[i].write(i + 1, font=("Arial", 14), align="center")
        food[i].turtlesize(0.00001)
    else:
        # If food is invisible, hide it
        food[i].clear()

# to run the game after click on the screen
def play(x,y):
    global t0
    game_intro.clear()
    # To record the initial time for the game
    t0 = int(time.perf_counter())
    # Create 5 random food in random position
    createFood(5)
    screen.onclick(None)
    screen.ontimer(snakeMove, snakeSpeed)
    screen.ontimer(monsterMove, 300)
    while len(snakeHead.stampItems) < 20:
        screen.update()
        screen.ontimer(foodVisibility)

# Create n foods with random distribution
def createFood(n):
    global food_pos
    while len(food_pos) != n:
        # Randomly choose the position of the food
        x = random.randint(-225, 225)
        y = random.randint(-265, 185)
        # Record the food position
        food_pos.append((x, y))
    screen_refresh()
    for n in range(n):
        food[n] = write(food_pos[n][0], food_pos[n][1]-10)
        food[n].write(n + 1, font=("Arial", 14), align="center")
        food[n].turtlesize(0.00001)
    screen_refresh()


# To check whether the given point is inside the motion area
def if_inarea(point):
    if (abs(point[0]) < 250) and (abs(point[1]+40) < 250):
        return True

# Move monster to chase the head of snake in a random pace
def monsterMove():
    global if_running
    def contact():
        global number_contact, monster, snakebody_pos
        for point in snakebody_pos:
            # Count the number of contact
            if abs(point[0] - monster.xcor()) + abs(point[1] - monster.ycor()) <= 20:
                number_contact += 1
                return

    # To change the position of monster in order to chase the snake
    def changeMdis(distance):
        dist = 20 * ((distance + 1) / abs(distance + 1))
        return dist

    # To approach the snakehead, determine the change needed in x and y
    change_x = monster.xcor() - snakeHead.xcor()
    change_y = monster.ycor() - snakeHead.ycor()
    dis_x = monster.xcor() - changeMdis(change_x)
    dis_y = monster.ycor() - changeMdis(change_y)
    ran_move = []
    # To add a choice of move in x
    if if_inarea((dis_x, monster.ycor())):
        ran_move.append((-changeMdis(change_x), 0))
    # To add a choice of move in y
    if if_inarea((monster.xcor(), dis_y)):
        ran_move.append((0, -changeMdis(change_y)))
    # Randomly choose a move direction
    change_x, change_y = random.choice(ran_move)
    # If the game ends, the monster stop moving
    if if_running is False:
        change_x = 0
        change_y = 0
    mon_x = monster.xcor() + change_x
    mon_y = monster.ycor() + change_y
    monster.goto((mon_x, mon_y))
    contact()
    screen.ontimer(monsterMove, 300)

# To move the snake according to the key
def snakeMove():
    # Eat the food when the distance is within 20
    def foodEaten():
        global foodEaten, snakeHead, snakeLength, snakeSpeed, foodAppear
        for n in range(5):
            # if the distance between food and head is less than 20 and the food is not eaten or hidden
            if n not in foodEaten and foodAppear[n] and abs(snakeHead.xcor() - food_pos[n][0]) + abs(snakeHead.ycor() - food_pos[n][1]) <= 20:
                # erase the food（consume）
                food[n].clear()
                food[n].hideturtle()
                snakeLength += n + 1
                foodEaten.append(n)
                snakeSpeed = snakeSpeed + n*5  # Slow down the snake speed according to the number of food

    # To update the snake body
    def snakeBodyMove():
        global snakebody_pos, snakeHead, snakeLength, snakeSpeed
        # append current snake's head position to the body
        snakebody_pos.append(snakeHead.position())
        snakeHead.color('blue', 'black')
        # stamp the snake's head at the current position to substitute the previous one
        snakeHead.stamp()
        snakeHead.color('red', 'red')

        if snakeLength <= len(snakeHead.stampItems):
            snakeHead.clearstamps(1)
            snakebody_pos = snakebody_pos[1:]

    # Create finish situation
    def finish(point, color, word):
        update = write(point[0], point[1] + 25)  # print word right up the head
        update.color(color)
        update.write(word, font=("Arial", 14, "bold"), align="center")
        update.hideturtle()

    def finalPosition(a,b):
        global if_running, snakeHead
        finish(snakeHead.position(), a, b)
        if_running = False  # To suggest the ending
        screen_refresh()
        turtle.done()

    def judgeMotion():
        # If pause
        if if_pause is True:
            motion_show.write("Motion: Paused", font=("Arial", 14, "normal"), align="center")
        # If move
        else:
            motion_show.write("Motion: " + str(Last_move).capitalize(), font=("Arial", 14, "normal"), align="center")

    def judgeTime():
        global t0
        time_show.write("Time: " + str(int(time.perf_counter()) - t0), font=("Arial", 14, "normal"), align="center")

    def judgeContact():
        global number_contact
        contact_show.write("Contact: " + str(number_contact), font=("Arial", 14, "normal"), align="center")

    # To renew the status
    def refresh_status():
        global foodEaten, monster, if_running, snakeHead, number_contact, t0
        # If every food is eaten up, then win!
        if len(snakeHead.stampItems) == 20:
            finalPosition('red', 'Winner!!')
        # If the head is chased by monster, then game over!
        elif snakeHead.distance(monster) <= 20:
            finalPosition('purple', 'Game over!!')

        # To clear the written sentence(initialize)
        contact_show.clear()
        motion_show.clear()
        time_show.clear()
        # To print out the update status, motion, time
        judgeContact()
        judgeMotion()
        judgeTime()

    global screen, snakeHead, Last_move
    screen_refresh()

    # If game is running and snake is still moving
    if if_running and not if_pause:
        # To determine the change_x and change_y according to the direction
        change_x, change_y = {"down": (0, -20), "left": (-20, 0), "right": (20, 0), "up": (0, 20), "pause": (0, 0)}[snakeHead.direction]
        # To calculate the next position
        next_pos = (snakeHead.xcor() + change_x, snakeHead.ycor() + change_y)
        # Prevent the snake crash with border and itself
        if if_inarea(next_pos) and next_pos not in snakebody_pos:
            Last_move = snakeHead.direction
            snakeBodyMove()
            snakeHead.goto(snakeHead.xcor() + change_x, snakeHead.ycor() + change_y)
        # Else, the snake will be stopped
        else:
            snakeHead.direction = Last_move
    # Update all the variables
    foodEaten()
    refresh_status()
    screen_refresh()
    screen.ontimer(snakeMove, snakeSpeed)


# To change the direction once have key control
def up():
    if not if_pause and Last_move not in ["down"]:
        snakeHead.direction = "up"

def down():
    if not if_pause and Last_move not in ["up"]:
        snakeHead.direction = "down"

def left():
    if not if_pause and Last_move not in ["right"]:
        snakeHead.direction = "left"

def right():
    if not if_pause and Last_move not in ["left"]:
        snakeHead.direction = "right"

# To change the pause state
def pausestate():
    # To change the pause state
    global Last_direction, if_pause
    if_pause ^= True
    if snakeHead.direction == "pause":
        snakeHead.direction = Last_direction
    else:
        Last_direction = snakeHead.direction
        snakeHead.direction = "pause"

# To renew the screen tracer
def screen_refresh():
    global pause_status
    pause_status = 1 - pause_status
    screen.tracer(pause_status)

# Create the original screen
def createScreen():
    win = turtle.Screen()
    win.tracer(0)
    win.title("Snake by Duyixuan")
    win.setup(620, 700)
    win.mode("standard")
    return win

def createPlayArea():
    # motion border
    motion = createTurtle(0, 0, "black", "")
    motion.shapesize(25, 25, 5)
    motion.goto(0, -40)

    # status border
    status = createTurtle(0, 0, "black", "")
    status.shapesize(4, 25, 5)
    status.goto(0, 250)

    # introduction
    intro = createTurtle(-150, 150)
    intro.hideturtle()
    intro.write("Snake by Duyixuan\nClick anywhere to start the game .....", font = ("Arial", 16, "normal"))

    return intro

# Create every square figure
def createTurtle(x, y, pen = "black", fill = "red"):
    t = turtle.Turtle("square")
    turtle.hideturtle()
    t.color(pen, fill)
    t.up()
    t.goto(x,y)
    return t

# Create the monster
def monsterShape():
    x = random.randint(-23, 25) * 10 - 10
    y = random.randint(-23, 21) * 10 - 10
    mon = createTurtle(x, y, fill='purple')
    return mon

# Set key control
def keyControl():
    screen.onkey(down, "Down")
    screen.onkey(left, "Left")
    screen.onkey(right, "Right")
    screen.onkey(up, "Up")
    screen.onkey(pausestate, "space")
    screen.listen()

def write(x,y):
    word = turtle.Turtle()
    word.penup()
    word.hideturtle()
    word.goto(x,y)
    return word

# The main game program
# Create the origin structure of the screen
screen = createScreen()
screen.title("Snake by DuYixuan")
game_intro = createPlayArea()
screen_refresh()
# Create the monster
monster = monsterShape()

# Create the head of the snake
snakeHead = createTurtle(0, 0, "", "red")
snakeHead.direction = "pause"

# Set key control
keyControl()

# Set update status
contact_show = write(-155, 245)
motion_show = write(155, 245)
time_show = write(0, 245)
screen_refresh()

# Click to start the play and began to record time
screen.onscreenclick(play)
start_time = time.time()
screen.mainloop()
