from random import randint, choice
from brain_games.games.engine import run_game

RULES = 'What is the result of the expression?'


def generate_question():
    a, b = randint(0, 101), randint(0, 101)
    sign = choice(["+", "-", "*"])
    question = f"{a} {sign} {b}"
    answer = eval(question)
    return question, answer


def calc_game():
    run_game(RULES, generate_question)
