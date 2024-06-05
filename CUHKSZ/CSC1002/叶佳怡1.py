import random


def main_puzzle_game():
    # Welcome message
    print('Welcome to the puzzle game')

    # Define the correct solution
    correct_solution = [[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, ' ']]

    # Generate a random puzzle
    puzzle = generate_random_puzzle()

    # Input correct directions for movement
    left_move, right_move, up_move, down_move = detect_correct_input()

    # Print the initial puzzle
    print_puzzle_state(puzzle)

    # Initialize move count
    move_counter = 0

    # Loop for player moves
    while puzzle != correct_solution:
        # Perform a move
        puzzle = execute_move(puzzle, left_move, right_move, up_move, down_move)

        # Increment move count
        move_counter += 1

        # Print the current puzzle
        print_puzzle_state(puzzle)

    # Print congratulations message
    print(f'Congratulations! You solved the puzzle in {move_counter} moves!')


def print_puzzle_state(puzzle):
    # Print the puzzle grid
    for row in puzzle:
        for item in row:
            print(item, end=' ')
        print()

def detect_correct_input():
    # Function to detect and validate correct input directions
    while True:
        # Input directions
        input_string = input('Enter the four letters used for left, right, up, and down move: ')
        unique_count = 0
        input_list = []
        for char in input_string:
            # Check if character is alphabet and unique
            if char.isalpha() and char not in input_list:
                char = char.lower()
                input_list.append(char)
            if char.isalpha():
                unique_count += 1
        # Ensure exactly four unique alphabets are entered
        if unique_count != 4 or len(input_list) != 4:
            print('You must enter four different alphabets!')
            continue
        else:
            return input_list

def generate_random_puzzle():
    # Function to generate a random puzzle
    numbers_list = random.sample(range(1, 10), 9)
    puzzle = [numbers_list[i:i + 3] for i in range(0, 9, 3)]
    puzzle = [[' ' if x == 9 else x for x in sublist] for sublist in puzzle]
    return puzzle

def execute_move(puzzle, left, right, up, down):
    # Function to perform a move in the puzzle
    selected_move, coordinates = detect_move_input(puzzle, left, right, up, down)
    x_coord, y_coord = int(coordinates[0]), int(coordinates[1])

    if selected_move == right:
        puzzle[y_coord][x_coord], puzzle[y_coord][x_coord - 1] = puzzle[y_coord][x_coord - 1], puzzle[y_coord][x_coord]
    elif selected_move == left:
        puzzle[y_coord][x_coord], puzzle[y_coord][x_coord + 1] = puzzle[y_coord][x_coord + 1], puzzle[y_coord][x_coord]
    elif selected_move == down:
        puzzle[y_coord][x_coord], puzzle[y_coord - 1][x_coord] = puzzle[y_coord - 1][x_coord], puzzle[y_coord][x_coord]
    elif selected_move == up:
        puzzle[y_coord][x_coord], puzzle[y_coord + 1][x_coord] = puzzle[y_coord + 1][x_coord], puzzle[y_coord][x_coord]
    return puzzle

def detect_move_input(puzzle, left, right, up, down):
    # Function to detect and validate move input
    while True:
        empty_space_coord = find_empty_space(puzzle)
        possible_moves = []

        if empty_space_coord[0] > 0:
            possible_moves.append(right)
        if empty_space_coord[0] < 2:
            possible_moves.append(left)
        if empty_space_coord[1] > 0:
            possible_moves.append(down)
        if empty_space_coord[1] < 2:
            possible_moves.append(up)

        # Create prompt for available moves
        moves = {'left': left, 'right': right, 'up': up, 'down': down}
        moves_prompt = ', '.join([f'{move}-{moves[move]}' for move in moves if moves[move] is not None])
        # Adjust prompt based on empty space coordinates
        if empty_space_coord[0] == 2:
            moves_prompt = moves_prompt.replace('left-', '')
        elif empty_space_coord[0] == 0:
            moves_prompt = moves_prompt.replace('right-', '')
        if empty_space_coord[1] == 2:
            moves_prompt = moves_prompt.replace('up-', '')
        elif empty_space_coord[1] == 0:
            moves_prompt = moves_prompt.replace('down-', '')
        # Remove any trailing or leading commas or spaces
        moves_prompt = moves_prompt.strip(', ')


        # Input move
        player_move = input('Enter your move ('+ moves_prompt + ')' + ' > ')
        # Validate move input
        player_move = player_move.lower()
        for move in player_move:
            if move.isalpha():
                if move in possible_moves and len(player_move) == 1:
                    return move, empty_space_coord
        print('You must enter one of the allowed letters!')
        continue

def find_empty_space(puzzle):
    # Function to find the coordinate of the empty space in the puzzle
    return next((x, y) for y, row in enumerate(puzzle) for x, item in enumerate(row) if item == ' ')


main_puzzle_game()
