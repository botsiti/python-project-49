from random import randint, choice


GAME_MESSAGE = 'What number is missing in the progression?'


def prog_settings(first_num):
    variants = (2, 3, 5)
    i = choice(variants)
    prog = []
    total = randint(7, 10)
    while total:
        prog.append(first_num)
        first_num += i
        total -= 1
    return prog


def game_settings():
    first_num = randint(1, 50)
    items = prog_settings(first_num)
    length = (len(items))
    remove = randint(0, length - 1)
    correct_answer = items[remove]
    items[remove] = '..'
    question = f'Question: {items}'
    return question, correct_answer
