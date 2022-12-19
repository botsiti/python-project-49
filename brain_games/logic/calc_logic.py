import prompt
from random import randint, choice


def calc_game():
    print('Welcome to the Brain Games')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression')
    tries = 3
    while tries:
        def random_number():
            return randint(1, 10)
        number1 = random_number()
        number2 = random_number()
        symbols = ('-', '+', '*')
        operator = choice(symbols)
        print(f'Question: {number1} {operator} {number2}')
            
        if operator == '-':
            correct_answer = number1 - number2
        elif operator == '+':
            correct_answer = number1 + number2
        elif operator == '*':
            correct_answer = number1 * number2
        
      

        user_answer = prompt.string('Your answer: ')
        if user_answer == str(correct_answer):
            print('Correct')
            tries -= 1
        else:
            print(f''''{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'
Let's try again, {name}''')
            break 
        if tries == 0:
            print(f'Congratulations, {name}!')
