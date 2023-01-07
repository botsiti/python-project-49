from random import randint


GAME_MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime_game(number):
    if number == 1:
        return False
    divider = number - 1
    while divider > 1:
        if number % divider == 0:
            return False
        divider -= 1
    return True


def get_game():
    number = randint(1, 100)
    question = f'Question: {number}'
    if prime_game(number):
        correct_answer: str = 'yes'
    else:
        correct_answer: str = 'no'
    return question, correct_answer
