 # This is a guess the number game

yourgusses = 0

number = 8


Game = ('Guess number from 1 to 10')

print(Game + ", I am thinking of a number between 1 and 10. Can you guess what it is")

while yourgusses !=  8:
    guess = input('Enter a number: ')
    guess = int(guess)

    yourgusses = yourgusses + 1;

    if guess == number:
        break

if guess == number:
    yourgusses = str(yourgusses)

    print('Great you did it ')
