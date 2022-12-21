from random import randint, choice




def calc_elements(operator: str, number1: int, number2: int):
    if operator == '-':
        correct_answer = number1 - number2
    elif operator == '+':
        correct_answer = number1 + number2
    elif operator == '*':
        correct_answer = number1 * number2
    return str(correct_answer)

def random_number():
        return randint(1, 10)

GAME_MESSAGE = 'What is the result of the expression?'



def game_settings():
    number1 = random_number()
    number2 = random_number()
    symbols = ('-', '+', '*')
    operator = choice(symbols)
    question = f'Question: {number1} {operator} {number2}'
    correct_answer: str = calc_elements(operator, number1, number2)
    return question, correct_answer


