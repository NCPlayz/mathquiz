from calc_parse import calculate, create_question


def ask_for_sum():
    while True:
        user_input = input('Enter the sum (type "exit" to exit):\n> ')

        if user_input == 'exit':
            exit()
        else:
            try:
                print('The answer is:', calculate(user_input))
            except SyntaxError as e:
                print(e)

def quiz():
    difficulty = input('What is the difficulty you want easy, medium, or hard?\n> ').lower()
    score = 0
    tries_left = 5

    _sum = create_question(difficulty)
    real_ans = calculate(_sum)

    while True:
        print('Enter the answer of:', _sum)
        ans = float(input('> '))

        if ans == 'exit':
            print('You got a total score of:', score)
            exit()
        elif ans != real_ans:
            tries_left -= 1
            print('Incorrect!', tries_left, 'tries left!')
        elif tries_left <= 0:
            print('Out of tries! Generating new question...')
            _sum = create_question(difficulty)
            real_ans = calculate(_sum)
        else:
            print('Correct!')
            score += 1
            _sum = create_question(difficulty)
            real_ans = calculate(_sum)


def menu():
    user_input = input('Would you like to do a quiz (choice "A"), or use the calculator (choice "B")?\n> ').lower()

    if user_input == 'a':
        quiz()
    elif user_input == 'b':
        ask_for_sum()
    else:
        print('Not a valid choice.')
        return menu()


if __name__ == '__main__':
    menu()
