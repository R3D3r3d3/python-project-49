import prompt
from random import randint


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def is_even(num):
    return not bool(num % 2)


def play_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count != 3:
        num = randint(0, 101)
        print(f"Question: {num}")
        answer = prompt.string("Your answer: ")
        if (is_even(num) and answer == "yes") or (not is_even(num) and answer == "no"):
            count += 1
            print("Correct!")
            if count == 3:
                print(f"Congratulations, {name}!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was {('no', 'yes')[is_even(num)]}")
            print(f"Let's try again, {name}!")
            break


def main():
    name = welcome_user()
    play_game(name)

if __name__ == "__main__":
    main()
