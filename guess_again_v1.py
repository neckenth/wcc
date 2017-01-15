import random


def get_guess():
    # Get initial guess
    guess = raw_input('Enter your guess: ')

    # Assume it's not valid, until it's proven otherwise
    valid = False

    while valid != True:
        try:
            # Try and convert this number to an integer
            # If it fails, the exception will occur
            guess = int(guess)
        except Exception:
            # Exception was thrown when trying to convert to number,
            # Report the issue and ask again
            print('Invalid input; please enter a whole number.')
            valid = False
            guess = get_guess()

        # If they get here, it means the number must have been valid
        # Set valid to be true to break out of the while loop
        valid = True

    return guess


def compare(num_a, num_b):
    if num_a > num_b:
        return 'high'
    elif num_a < num_b:
        return 'low'
    elif num_a == num_b:
        return 'equal'

# Guess Again - final
def play():
    # pick a secret number
    secret_number = random.randint(1, 100)
    # print('TEMPORARY DEBUGGING HELPER -> The secret number is: ' + str(secret_number))

    print("\nI'm thinking of a number between 1 and 100; what do you think it is?")

    num_a = get_guess()
    num_b = secret_number
    compare(num_a, num_b)
    while compare(num_a, num_b) != 'equal':
        if compare(num_a, num_b) == 'high':
            print('Too ' + compare(num_a, num_b) + '. Guess again.')
        elif compare(num_a, num_b) == 'low':
            print('Too ' + compare(num_a, num_b) + '. Guess again.')
        num_a = get_guess()
    if compare(num_a, num_b) == 'equal':
        print('You got it! The number was ' + str(secret_number))

play()

# Bonus feature #1: Update your game so that it can be played with numbers other than 1 and 100

def play(min, max):
    # pick a secret number

    secret_number = random.randint(min, max)
    # print('TEMPORARY DEBUGGING HELPER -> The secret number is: ' + str(secret_number))

    print("\nI'm thinking of a number between " + str(min) + " and " + str(max) + "; what do you think it is?")

    num_a = get_guess()
    num_b = secret_number
    compare(num_a, num_b)
    while compare(num_a, num_b) != 'equal':
        if compare(num_a, num_b) == 'high':
            print('Too ' + compare(num_a, num_b) + '. Guess again.')
        elif compare(num_a, num_b) == 'low':
            print('Too ' + compare(num_a, num_b) + '. Guess again.')
        num_a = get_guess()
    if compare(num_a, num_b) == 'equal':
        print('You got it! The number was ' + str(secret_number))

play(54, 1003)

# Bonus feature #2: Update your game so that it keeps track of how many guesses the user has made.

def play(min, max):
    # pick a secret number

    secret_number = random.randint(min, max)
    # print('TEMPORARY DEBUGGING HELPER -> The secret number is: ' + str(secret_number))

    print("\nI'm thinking of a number between " + str(min) + " and " + str(max) + "; what do you think it is?")
    counter = 0
    num_a = get_guess()
    num_b = secret_number
    compare(num_a, num_b)
    while compare(num_a, num_b) != 'equal':
        if compare(num_a, num_b) == 'high':
            print('Too ' + compare(num_a, num_b) + '. Guess again.')
        elif compare(num_a, num_b) == 'low':
            print('Too ' + compare(num_a, num_b) + '. Guess again.')
        num_a = get_guess()
        counter += 1
    if compare(num_a, num_b) == 'equal':
        print('You got it! The number was ' + str(secret_number))
        print('It took you ' + str(counter + 1) + ' tries.')

play(54, 1003)