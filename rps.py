import random


def check_move(player_move):
    if player_move == 'rock':
        return True
    elif player_move == 'paper':
        return True
    elif player_move == 'scissors':
        return True
    else:
        return False


def get_player_move():
    player_move = raw_input('Pick your move: rock, paper, or scissors? ')
    while check_move(player_move) == False:
        print('Invalid move; pick again.')
        player_move = get_player_move()
    return player_move


def get_computer_move():
    moves = ['rock', 'paper', 'scissors']
    computer_move = random.choice(moves)
    print('The computer picked: ' + computer_move)
    return computer_move


def judge():
    move_a = get_player_move()
    move_b = get_computer_move()
    if move_a == 'rock' and move_b == 'paper':
        return False
    elif move_a == 'paper' and move_b == 'rock':
        return True
    elif move_a == 'rock' and move_b == 'scissors':
        return True
    elif move_a == 'scissors' and move_b == 'rock':
        return False
    elif move_a == 'paper' and move_b == 'scissors':
        return False
    elif move_a == 'scissors' and move_b == 'paper':
        return True
    elif move_a == move_b:
        print('Tie! Play again!')


def results():
    if judge() is True:
        print('You won!')
    elif judge() is False:
        print('The computer won!')


def play():
    print('\nWelcome to Rock, Paper, Scissors!')
    get_player_move()
    get_computer_move()
    judge()
    results()
    play_again = raw_input("\nPlay again? Type 'y' or 'n': ")
    if play_again == 'y':
        play()
    else:
        print('Thanks for playing!')

play()


