from random import randint
from brain_games.games.engine import run_game

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question():
    question = randint(0, 101)
    answer = "no" if bool(question % 2) else "yes"
    return question, answer


def even_game():
    run_game(RULES, generate_question)
