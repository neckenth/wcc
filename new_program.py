'''
I'd like to build a program to help me decide what to eat for dinner depending on specific ingredients input by the user

User is prompted for a list of 4 ingredients they have on-hand - raw_input into a list of strings
Scrape a food site (TBD) for string matches for the word 'dinner' as well as for the strings in the list of ingredients
Pull all of these meal choices into a list, and pull out a random choice to present to user (.pop)
Each meal is presented to the user, one by one
User can choose to eat the presented meal or make another choice
User can only choose to make another choice up to 3 times
Loop ends on the 3rd execution - print('Just eat this one...it will be good.')
'''