from random import randint, choice


GAME_MESSAGE = 'What number is missing in the progression?'


def game_settings():
    first_num = randint(1, 50)
    length = randint(7, 10)
    variants = (2, 3, 5)
    iter = choice(variants)
    prog = []
    total = length
    while total:
        prog.append(first_num)
        first_num += iter
        total -= 1
    dots = randint(0, length - 1)
    correct_answer = prog[dots]
    prog[dots] = '..'
    string = " ".join(map(str, prog))
    question = f'Question: {string}'
    return question, correct_answer
