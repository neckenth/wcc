import random


def get_guess():
    guess = raw_input('Enter your guess: ')

    valid = False

    while valid != True:
        try:
            guess = int(guess)
        except Exception:
            print('Invalid input; please enter a whole number.')
            valid = False
            guess = get_guess()

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
    #print('TEMPORARY DEBUGGING HELPER -> The secret number is: ' + str(secret_number))

    print("\nI'm thinking of a number between " + str(minimum) + " and " + str(maximum) + "; what do you think it is?")

    for guess_count in range(tries):
        num_a = get_guess()
        num_b = secret_number
        results = compare(num_a, num_b)
        if results == 'equal':
            print('You got it! The number was ' + str(secret_number) + '.')
            break
        elif results == 'high':
            print('Too ' + results + '. You have ' + str(tries - (guess_count + 1)) + ' guesses left.')
        else:
            print('Too ' + results + '. You have ' + str(tries - (guess_count + 1)) + ' guesses left.')
    if results != 'equal':
        print('Sorry, you ran out of turns! The correct number was ' + str(secret_number))

play(1, 20, 5)