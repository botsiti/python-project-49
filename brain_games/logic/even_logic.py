from random import randint


GAME_MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True


def get_game():
    number = randint(1, 100)
    question = f'Question: {number}'
    if is_even(number) is True:
        correct_answer: str = 'yes'
    else:
        correct_answer: str = 'no'
    return question, correct_answer
