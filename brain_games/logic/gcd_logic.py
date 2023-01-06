from random import randint


GAME_MESSAGE = 'Find the greatest common divisor of given numbers.'


def random_number():
    return randint(1, 100)


def gcdgame(num1: int, num2: int):
    list = [1]
    lowest_num = min(num1, num2)
    for i in range(1, lowest_num + 1):
        if num1 % i == 0 and num2 % i == 0:
            list.append(i)
        i += 1
    return max(list)


def get_game():
    num1 = random_number()
    num2 = random_number()
    question = f'Question: {num1} {num2}'
    correct_answer: str = gcdgame(num1, num2)
    return question, correct_answer
