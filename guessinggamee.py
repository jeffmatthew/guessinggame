print('SIMPLE NUMBER GUESSING GAME')

import random
randomint = random.randint(1,100)
inp = 0

while inp != randomint:
    inp = eval(input("Pick a number from 1-100 : "))
    if inp < randomint:
        print('You guessed too low')
    elif inp > randomint:
        print('You guessed to high')
else:
    print('Congratulations! Your guess is correct')