import random

print("Welcome to Menger’s puzzle game!")  # welcome words
print("In this game, you will be prompted to enter four different letters.")
print("These letters will represent the directions: left, right, up, and down.")
print("Your goal is to rearrange the numbers in ascending order by moving the empty space.")
print("Let's see if you can solve the puzzle!")

letters = input("Enter the four different letters used for left, right, up and down move(do not use separate) >")
long = len(letters)
while (long != 4 or letters.isalpha() == False
       or len(set(letters)) != 4 or not letters.islower()): # check the validity of the input
    letters = input("Enter four different letters! >")
l = letters[0]  # store the letter to control left
r = letters[1]  # store the letter to control right
u = letters[2]  # store the letter to control up
d = letters[3]  # store the letter to control down
line = ""  # store every line of the puzzle
move = ()  # Use tuple to store movable directions for easy output
able = []  # Use list to store movable directions
sites = {}  # Use a dictionary to store numbers and corresponding positions
ran = 0  # The number of times for disrupting

def run(move):  # change the site of the number by instruction
    """Declare the variables of row, column and step numbers as global variables"""
    global row_of_space
    global col_of_space
    global step_number
    """Swap positions"""
    if move == l:
        sites[row_of_space, col_of_space] = sites[row_of_space, col_of_space + 1]
        sites[row_of_space, col_of_space + 1] = " "
        row_of_space = row_of_space
        col_of_space = col_of_space + 1
    if move == r:
        sites[row_of_space, col_of_space] = sites[row_of_space, col_of_space - 1]
        sites[row_of_space, col_of_space - 1] = " "
        row_of_space = row_of_space
        col_of_space = col_of_space - 1
    if move == u:
        sites[row_of_space, col_of_space] = sites[row_of_space + 1, col_of_space]
        sites[row_of_space + 1, col_of_space] = " "
        row_of_space = row_of_space + 1
        col_of_space = col_of_space
    if move == d:
        sites[row_of_space, col_of_space] = sites[row_of_space - 1, col_of_space]
        sites[row_of_space - 1, col_of_space] = " "
        row_of_space = row_of_space - 1
        col_of_space = col_of_space
    if move != l and move != r and move != u and move != d:
        print("You entered a letter that wasn't defined, please enter again!")
        step_number -= 1

def check_complete():  # check whether the game is completed
    if size == "1":
        numbers = choice1
    elif size == "2":
        numbers = choice2
    n = 0
    for row in range(size_int):
        for col in range(size_int):
            """Check if all the sequences are correct, if not, jump out of the function"""
            if sites[row, col] != numbers[n]:
                return
            n += 1
    """All buttons are judged, then win the game"""
    print("Congratulations! You solved the puzzle in "+str(step_number)+" moves!")
    return True

def check_move():  # search every direction we can go next
    global move
    global able
    able = []   # clear the previous
    if col_of_space < (size_int-1):
        move = move + ("left-" + l,)
        able.append(l)
    if col_of_space > 0:
        move = move + ("right-" + r,)
        able.append(r)
    if row_of_space < (size_int - 1):
        move = move + ("up-" + u,)
        able.append(u)
    if row_of_space > 0:
        move = move + ("down-" + d,)
        able.append(d)

while True:
    """ list of all numeric literals"""
    choice1 = ['1', '2', '3', '4', '5', '6', '7', '8', ' ']
    choice2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', ' ']
    size = input('Enter “1” for 8-puzzle, “2” for 15-puzzle or “q” to end the game >')
    while size != "1" and size != "2" and size != "q":
        size = input('Please enter the correct choice! “1” for 8-puzzle, “2” for 15-puzzle or “q” to end the game >')
    if size == "1":
        numbers = choice1
    elif size == "2":
        numbers = choice2
    elif size == "q":
        print("You quit the game!")
        exit()
    size_int = int(size) + 2
    """Manufacture a feasible game"""
    row_of_space = 0  # store the row of space
    col_of_space = 0  # store the colum of space
    step_number = 0  # create the store of the number of space
    """Generating with the correct order first"""
    for row in range(size_int):
        for col in range(size_int):
            num = numbers[row * size_int + col]  # pop the number
            sites[row, col] = num  # store the site of number
            line = line + '{:<4}'.format(num)
            if num == ' ':  # judge whether it is a blank button
                row_of_space = row
                col_of_space = col
        line=""
    if size == "1":
        numbers = choice1    # restore the list of numbers
    elif size == "2":
        numbers = choice2    # restore the list of numbers
    """Randomly generating a feasible game"""
    while ran < 99:
        check_move()
        numb = random.randint(0,len(able)-1)
        random_move = able[numb]
        run(random_move)
        ran += 1

    for m in range(size_int):
        for n in range(size_int):
            line = line + '{:<4}'.format(sites[m,n])
        print(line)
        line=""

    move = ()
    ran = 0
    """Cycle through the game"""

    while check_complete() != True:
        check_move()
        your_move = input("Enter your move " + str(move) + " >")
        step_number += 1
        try:  # if enter the right letter, go on
            run(your_move)
            for m in range(size_int):
                for n in range(size_int):
                    line = line + '{:<4}'.format(sites[m, n])
                print(line)
                line = ""
            move = ()
        except:  # if enter the wrong letter, enter again
            print("Please think carefully and enter your move again!")
            move = ()
            step_number -= 1

    next = input("Congratulations! You solved the puzzle in " +
                 str(step_number) + " moves! Play again? (Enter 'n' for a new game or 'q' to quit) >")
    if next == "q":
        exit()
    elif next == "n":
        break

