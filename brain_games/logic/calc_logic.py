from random import randint, choice


GAME_MESSAGE = 'What is the result of the expression?'
SYMBOLS = ('-', '+', '*')


def calc_expression(operator: str, number1: int, number2: int):
    if operator == '-':
        correct_answer = number1 - number2
    elif operator == '+':
        correct_answer = number1 + number2
    elif operator == '*':
        correct_answer = number1 * number2
    return str(correct_answer)


def get_game():
    number1 = randint(1, 10)
    number2 = randint(1, 10)
    operator = choice(SYMBOLS)
    question = f'Question: {number1} {operator} {number2}'
    correct_answer: str = calc_expression(operator, number1, number2)
    return question, correct_answer
