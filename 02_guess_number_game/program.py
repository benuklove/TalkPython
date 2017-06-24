"""

  Created on 6/24/2017 by Ben

  benuklove@gmail.com
  
  Guess a random number.

"""

import random

print('--------------------------------')
print('     GUESS THAT NUMBER GAME     ')
print('--------------------------------')
print()

the_number = random.randint(0, 100)
guess = -1

name = input("Player, what is your name? ")
lives = 7

while guess != the_number and lives > 0:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)
    if guess < the_number:
        print('Sorry {}, your guess of {} was too LOW.'.format(name, guess))
    elif guess > the_number:
        print('Sorry {}, your guess of {} was too HIGH.'.format(name, guess))
    else:
        print('Oh fine {}, {} was right, you win.  I\'m going home.'.format(name, guess))
    lives -= 1

if lives == 0:
    print('You\'re not a good guesser, are you?')

print('done')
