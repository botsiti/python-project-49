import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_engine(game):
    name = welcome_user()
    print(game.GAME_MESSAGE)
    tries = 3
    while tries:
        question, correct_answer = game.game_settings()
        print(question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(correct_answer):
            print('Correct')
            tries -= 1
        else:
            correct_answ = f"Correct answer was '{correct_answer}'"
            print(f"'{user_answer}' is wrong answer ;( {correct_answ}")
            print(f"Let's try again, {name}")

            break
        if tries == 0:
            print(f'Congratulations, {name}!')
