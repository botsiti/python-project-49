from random import randint


GAME_MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'


def random_number():
    return randint(1, 100)


def game_settings():
    number = random_number()
    question = f'Question: {number}'
    if number % 2 == 0:
        correct_answer = 'yes'
    if number % 2 != 0:
        correct_answer = 'no'
    return question, correct_answer

