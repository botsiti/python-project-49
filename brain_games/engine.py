import prompt


def game_engine(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_MESSAGE)
    tries = 3
    while tries:
        question, correct_answer = game.get_game()
        print(question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(correct_answer):
            print('Correct')
            tries -= 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct "
                  f"answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return
    if tries == 0:
        print(f'Congratulations, {name}!')
