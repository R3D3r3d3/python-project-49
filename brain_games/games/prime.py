from random import randint
from brain_games.games.engine import run_game

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question():
    num = randint(1, 101)
    question = str(num)
    answer = "yes" if num > 1 else "no"
    for i in range(2, (num//2)+1):
        if num % i == 0:
            answer = "no"
    return question, answer


def prime_game():
    run_game(RULES, generate_question)
