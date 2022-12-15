from random import randint
from brain_games.engine import *

def even_game():
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    tries = 3
    while tries:
        def random_number():
            return randint(1, 100)
        number = random_number()
        print(f'Question: {number}')
        if number % 2 == 0:
            correct_answer = 'yes'
        if number % 2 != 0:
            correct_answer = 'no'


        user_answer = input()
        if user_answer == correct_answer:
            print('Correct')
            tries -= 1
        else:
            print(f'''{user_answer} is wrong answer ;(. Correct answer was "no"
Let's try again, WHAT TO ADD''')

