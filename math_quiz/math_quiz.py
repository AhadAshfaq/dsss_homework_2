import random

def get_random_integer(minimum, maximum):
    """
    Using random.randint function to get random integer between the specified limits.
    """
    return random.randint(minimum, maximum)


def random_operator():
    """
    Using random.randint function to get a random arithmetic operator (+, -, *).
    """
    return random.choice(['+', '-', '*'])


def equation_to_solve(number_1, number_2, operator):
    """
    A mathematical equation will be expressed based on two numbers and an operator.
    Returns the equation as a string and the correct answer is stored in result .
    """

    equation = f"{number_1} {operator} {number_2}"
    if operator == '+':
        result=number_1 + number_2
    elif operator == '-':
        result=number_1 - number_2
    else:
        result=number_1 * number_2
    return equation,result

def math_quiz():
    """
    A game will be played where user will be provided with 5 mathematical equations to solve.
    A variable count is created to keep tracking correct answers.
    """

    count = 0
    total_questions = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        number_1 = get_random_integer(1, 10)
        number_2 = get_random_integer(1, 5)
        operator = random_operator()

        question, answer = equation_to_solve(number_1, number_2, operator)
        print(f"\nQuestion: {question}")
        user_answer = input("Your answer: ")

        """
        Using try-except funciton to make sure user enters an integer value.
        """

        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if user_answer == answer:
            print("Correct! You earned a point.")
            count += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {count}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
