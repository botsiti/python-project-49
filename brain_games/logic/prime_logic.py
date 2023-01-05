from random import randint


GAME_MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def even_game(number):
    divider = number - 1
    while divider > 1:
        if number % divider == 0:
            return "no"
        divider -= 1
    return "yes"



def game_settings():
    number = randint(1, 100)
    question = f'Qestion: {number}'
    correct_answer = even_game(number)
    return question, correct_answer

