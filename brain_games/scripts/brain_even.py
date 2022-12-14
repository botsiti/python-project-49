#!/usr/bin/env python3

from random import randint
from  brain_games.engine import welcome_user


welcome_user()


print('Answer "yes" if the number is even, otherwise answer "no".')


def random_number():
    return randint(1, 200)


tries = 3
while tries:
    test = random_number()
    print(f'Question: {test}')
    answer = input()
    if answer == 'yes' and test % 2 == 0:
        print('Correct')
        tries -= 1
    elif answer == 'no' and test % 2 != 0:
        print('Correct')
        tries -= 1
    elif answer == 'no' and test % 2 == 0:
        print(f'''{answer} is wrong answer ;(. Correct answer was "yes"
Let's try again, Billy''')
        break
    elif answer == 'yes' and test % 2 != 0:
        print(f'''{answer} is wrong answer ;(. Correct answer was "no"
Let's try again, Billy''')
        break
    elif answer !=  'yes' or answer != 'no':
        print(f'''{answer} is wrong answer ;(. Correct answer was "no"
Let's try again, Billy''')
        break
if tries == 0:
    print('Congratulations, Bill!')                
