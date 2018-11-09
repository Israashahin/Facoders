 # This is a guess the number game
Game = ('Guess number from 1 to 10')
print(Game +  ",I am thinking of a number between 1 and 10. Can you guess what it is??")

yourguesses = int(input('Enter a number: '))
number = 8

while yourguesses != number:
    yourguesses = int(input('Enter a number: '))

else:
    print('Great you did it')
