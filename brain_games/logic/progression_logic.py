from random import randint, choice

GAME_MESSAGE = 'What number is missing in the progression?'


numbers = (2, 3, 5)
progression = choice(numbers)


def prog_game(num):
    two = []
    total = 10
    while total:
        two.append(num)
        num += 2
        total -= 1
    three = []
    total = 10
    while total:
        three.append(num)
        num += 3
        total -= 1
    five = []
    total = 10
    while total:
        five.append(num)
        num += 5
        total -= 1
    numbers = (two, three, five)
    return choice(numbers)



def game_settings():
    num = randint(1, 50)
    items = prog_game(num)
    remove = randint(0, 9)
    correct_answer = items[remove] 
    items[remove] = '..'
    question = f'Question: {items}'
    return question, correct_answer