import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
random.shuffle(cards)

# Round 1

player_card1 = cards.pop()
computer_card1 = cards.pop()

print('Player card first round: ' + str(player_card1))
print('Computer card first round:  ' + str(computer_card1))

# Round 2

decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')
if decision == 'h':
    player_card2 = cards.pop()
else:
    player_card2 = 0

computer_card2 = cards.pop()

print('Player cards second round: ' + str(player_card1) + ', ' + str(player_card2))
print('Computer cards second round:  ' + str(computer_card1) + ', ' + str(computer_card2))

# Round 3

decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')
if decision == 'h':
    player_card3 = cards.pop()
else:
    player_card3 = 0

if (computer_card1 + computer_card2) <= 16:
    computer_card3 = cards.pop()
else:
    computer_card3 = 0

print('Player cards third round: ' + str(player_card1) + ', ' + str(player_card2) + ', ' + str(player_card3))
print('Computer cards third round:  ' + str(computer_card1) + ', ' + str(computer_card2) + ', ' + str(computer_card3))

# Scoring

player_total = player_card1 + player_card2 + player_card3
computer_total = computer_card1 + computer_card2 + computer_card3

print('\nGame Over' + '\nPlayer Total: ' + str(player_total) + '\nComputer Total: ' + str(computer_total))

if player_total <= 21 and player_total > computer_total:
    print('Player wins with a total of ' + str(player_total) + '!')
elif computer_total > 21 and player_total <= 21:
    print('Player wins with a total of ' + str(player_total) + '!')
elif player_total > 21 and computer_total <= 21:
    print('Computer wins with a total of ' + str(computer_total) + '!')
elif computer_total <= 21 and computer_total > player_total:
    print('Computer wins with a total of ' + str(computer_total) + '!')
elif player_total == computer_total:
    print('Tie! Player and Computer have an equal number of points!')
elif player_total > 21 and computer_total > 21:
    print('Tie! Both Player and Computer have over 21!')

