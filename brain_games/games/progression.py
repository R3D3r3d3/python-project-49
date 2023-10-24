from random import randint
from brain_games.games.engine import run_game

RULES = 'What number is missing in the progression?'


def generate_question():
    step = randint(1, 9)
    start = randint(1, 9)
    stop = start + step * 10
    progression = list(range(start, stop, step))
    hide_num_index = randint(0, 9)
    answer = str(progression[hide_num_index])
    progression[hide_num_index] = ".."
    question = " ".join(map(str, progression))
    return question, answer


def progression_game():
    run_game(RULES, generate_question)
