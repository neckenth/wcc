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


def play(minimum, maximum, tries):
    secret_number = random.randint(minimum, maximum)
    # print('TEMPORARY DEBUGGING HELPER -> The secret number is: ' + str(secret_number))

    print("\nI'm thinking of a number between " + str(minimum) + " and " + str(maximum) + "; what do you think it is?")

    for guess_count in range(tries):
        num_a = get_guess()
        num_b = secret_number
        compare(num_a, num_b)
        while compare(num_a, num_b) != 'equal':
            guess_count += 1
            if compare(num_a, num_b) == 'high':
                print('Too ' + compare(num_a, num_b) + '. You have ' + str(tries - guess_count) + ' guesses left.')
            elif compare(num_a, num_b) == 'low':
                print('Too ' + compare(num_a, num_b) + '. You have ' + str(tries - guess_count) + ' guesses left.')
            num_a = get_guess()
        if compare(num_a, num_b) == 'equal':
            print('You got it! The number was ' + str(secret_number) + '.')
            break
    print('Sorry, you ran out of turns! The correct number was ' + str(secret_number) + '.')

play(1, 20, 5)
