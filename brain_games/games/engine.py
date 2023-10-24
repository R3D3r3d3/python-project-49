import prompt


def run_game(rules, generate_question):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(rules)
    count = 0
    while count != 3:
        question, result = generate_question()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        if answer == result:
            count += 1
            print("Correct!")
            if count == 3:
                print(f"Congratulations, {name}!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'")
            print(f"Let's try again, {name}!")
            break
