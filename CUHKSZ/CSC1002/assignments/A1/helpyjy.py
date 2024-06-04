import turtle
import random
import time
import math

# Set canvas
screen = turtle.Screen()
screen.title("Snake by 123090747")
screen.bgcolor("white")
screen.setup(width=580, height=640)
screen.tracer(0)  # Turn off screen updates

# The boundaries of the play area
margin = turtle.Turtle()
margin.penup()
margin.goto(-250, 220)
margin.pendown()
margin.pensize(4)
margin.color("black")
for _ in range(4):
    margin.forward(500)
    margin.right(90)
margin.hideturtle()

# Status bar
status_bar = turtle.Turtle()
status_bar.penup()
status_bar.color("black")
status_bar.goto(-250, 220)
status_bar.pendown()
status_bar.pensize(4)
status_bar.left(90)
status_bar.forward(60)
status_bar.right(90)
status_bar.forward(500)
status_bar.right(90)
status_bar.forward(60)
status_bar.hideturtle()

status_content = turtle.Turtle()
status_content.penup()
status_content.color("black")
status_content.goto(-230, 240)


# Update status bar
def update_status_content(contact, time, motion):
    status_content.clear()
    status_content.write(f"Contact: {contact}  Time: {time}  Motion: {motion}", align="left", font=("Courier", 16, "normal"))
    status_content.hideturtle()


# Initializes the status bar
contact = 0
update_status_content(contact, 0, "Paused")

# Prompt message
message_turtle = turtle.Turtle()
message_turtle.penup()
message_turtle.goto(0, 30)
message_turtle.hideturtle()
message_turtle.write("Click anywhere to start, have fun!", align="center", font=("Arial", 16, "normal"))

# Start the game
game_start = False
start_time = 0


def start_game(x, y):
    global game_start, start_time
    if not game_start:
        game_start = True
        message_turtle.clear()
        start_time = time.time()


screen.onclick(start_game)

# snake
snake = turtle.Turtle()
snake.speed(0)
snake.penup()
snake.goto(0, 0)
snake.hideturtle()
snake.direction = "stop"

snake_segments = []

snake_head = turtle.Turtle()
snake_head.shape("square")
snake_head.color("red")
snake_head.penup()


# Snake's growth function
def grow():
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("black")
    new_segment.pencolor("blue")
    new_segment.penup()
    snake_segments.append(new_segment)


snake_segments.append(snake_head)


# Move the snake's body
def move_segments():
    for i in range(len(snake_segments) - 1, 0, -1):
        x = snake_segments[i - 1].xcor()
        y = snake_segments[i - 1].ycor()
        snake_segments[i].goto(x, y)
    x = snake.xcor()
    y = snake.ycor()
    snake_segments[0].goto(x, y)


food_list = {}


def draw_food():
    global food_list
    i = len(food_list) + 1
    x, y = random.randint(1, 23) * 20 - 250, random.randint(1, 23) * 20 - 250
    fix_x, fix_y = x + 5, y - 22
    food_i = turtle.Turtle()
    food_i.penup()
    food_i.goto(fix_x, fix_y)
    food_i.pendown()
    food_i.color("black")
    food_i.write(i, font=("Arial", 16, "normal"))
    food_i.penup()
    food_i.goto(x, y)
    food_i.hideturtle()
    food_list[i] = food_i


for _ in range(1, 6):
    draw_food()

eat_list = food_list.copy()

# monsters
monsters = []
for _ in range(4):
    while True:
        flag = False
        x, y = random.randint(-240, 240), random.randint(-270, 210)
        if -40 < x < 40 and -40 < y < 40:
            continue

        for _, food in food_list.items():
            if abs(x - food.xcor()) < 20 or abs(y - food.ycor()) < 20:
                flag = True
                break
        if not flag:
            break
    monster = turtle.Turtle()
    monster.penup()
    monster.goto(x, y)
    monster.pendown()
    monster.speed(0)
    monster.shape("square")
    monster.color("purple")
    monster.penup()
    monsters.append(monster)


def update_monsters():
    for monster in monsters:
        dx = snake.xcor() - monster.xcor()
        dy = snake.ycor() - monster.ycor()

        length = math.sqrt(dx ** 2 + dy ** 2)
        dx /= length
        dy /= length

        new_x = monster.xcor() + dx
        new_y = monster.ycor() + dy

        monster.goto(new_x, new_y)


# Game control
def go_up():
    snake.direction = "up"

def go_down():
    snake.direction = "down"

def go_left():
    snake.direction = "left"

def go_right():
    snake.direction = "right"


screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")


# Game over
def success_game():
    success = turtle.Turtle()
    success.color("red")
    success.write("Winner!!", align="center", font=("Arial", 24, "normal"))
    turtle.done()


def failure_game():
    failure = turtle.Turtle()
    failure.color("red")
    failure.write("Game Over!", align="center", font=("Arial", 24, "normal"))
    turtle.done()


def approx(a, b, tol=1):
    a, b = round(a), round(b)
    return abs(a - b) < tol


def is_overlap(square1, square2, side_length):
    x1, y1 = square1
    x2, y2 = square2
    
    # Calculate the projections of the squares on the x and y axes
    x1_min, x1_max = x1, x1 + side_length
    y1_min, y1_max = y1 - side_length, y1
    
    x2_min, x2_max = x2, x2 + side_length
    y2_min, y2_max = y2 - side_length, y2

    # Check overlap on x axis and y axis
    overlap_x = (x1_min <= x2_max) and (x2_min <= x1_max)
    overlap_y = (y1_min <= y2_max) and (y2_min <= y1_max)

    return overlap_x and overlap_y


score = 0
motion = "Paused"
to_be_grow = 0
move_flag = True
current_direction = None

while not game_start:
    screen.update()

while game_start:
    screen.update()
    update_monsters()

    contact_flag = False
    for segment in snake_segments[1:]:
        for monster in monsters:
            if segment.distance(monster) < 20:
                contact += 1
                update_status_content(contact, round(time.time() - start_time), motion)
                contact_flag = True
                break
        if contact_flag:
            break

    # move the snake
    if move_flag:
        if snake.direction == "up":
            y = snake.ycor()
            snake.sety(y + 20)
            motion = "Up"
        elif snake.direction == "down":
            y = snake.ycor()
            snake.sety(y - 20)
            motion = "Down"
        elif snake.direction == "left":
            x = snake.xcor()
            snake.setx(x - 20)
            motion = "Left"
        elif snake.direction == "right":
            x = snake.xcor()
            snake.setx(x + 20)
            motion = "Right"

    # Update status bar
    update_status_content(contact, round(time.time() - start_time), motion)

    # Border collision detection
    if (not -250 < snake.xcor() < 250) or (not -280 < snake.ycor() < 220):
        if move_flag:
            if snake.direction == "up":
                current_direction = "up"
            elif snake.direction == "down":
                current_direction = "down"
            elif snake.direction == "left":
                current_direction = "left"
            elif snake.direction == "right":
                current_direction = "right"
        move_flag = False

    if current_direction is not None:
        if current_direction == "up":
            if snake.direction == "down":
                move_flag = True
        elif current_direction == "down":
            if snake.direction == "up":
                move_flag = True
        elif current_direction == "left":
            if snake.direction == "right":
                move_flag = True
        elif current_direction == "right":
            if snake.direction == "left":
                move_flag = True

    # Food collision detection
    for i, food in food_list.items():   
        if approx(snake.xcor() - 10, food.xcor()) and approx(snake.ycor() + 10, food.ycor()):
            score += 1
            food.clear()
            food.hideturtle()
            try:
                eat_list.pop(i)
                to_be_grow += i
            except KeyError:
                pass

    if to_be_grow > 0:
        grow()
        to_be_grow -= 1

    # Monster collision detection
    for monster in monsters:
        monster_x, monster_y = monster.xcor() - 10, monster.ycor() + 10
        if motion == "Left":
            snake_x, snake_y = snake.xcor() + 10, snake.ycor() + 10
        elif motion == "Right":
            snake_x, snake_y = snake.xcor() - 30, snake.ycor() + 10
        elif motion == "Up":
            snake_x, snake_y = snake.xcor() - 10, snake.ycor() - 10
        elif motion == "Down":
            snake_x, snake_y = snake.xcor() - 10, snake.ycor() + 30
        elif motion == "Paused":
            snake_x, snake_y = snake.xcor() - 10, snake.ycor() + 10
        if is_overlap((snake_x, snake_y), (monster_x, monster_y), 19):

            time.sleep(1)
            failure_game()

    if len(eat_list) == 0 and to_be_grow == 0:
        move_segments()
        screen.update()  # To fully stretch the snake, need to refresh the canvas one last time
        success_game()

    # Control game speed
    time.sleep(0.1)
    if move_flag:
        move_segments()  # Move the snake's body
