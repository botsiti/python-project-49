from random import randint, choice


GAME_MESSAGE = 'What number is missing in the progression?'


def prog_setting(number):
    first_num = randint(1, 50)
    step = (2, 3, 5)
    iter = choice(step)
    prog = []
    total = number
    while total:
        prog.append(first_num)
        first_num += iter
        total -= 1
    return prog


def get_game():
    length = randint(7, 10)
    prog = prog_setting(length)
    random_index = randint(0, length - 1)
    correct_answer: str = prog[random_index]
    prog[random_index] = '..'
    str_progression = " ".join(map(str, prog))
    question = f'Question: {str_progression}'
    return question, correct_answer
