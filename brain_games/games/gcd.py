from random import randint
import math
from brain_games.games.engine import run_game

RULES = 'Find the greatest common divisor of given numbers.'


def generate_question():
    a, b = randint(0, 101), randint(0, 101)
    question = f"{a} {b}"
    answer = str(math.gcd(a, b))
    return question, answer


def gcd_game():
    run_game(RULES, generate_question)
