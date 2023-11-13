import unittest
from math_quiz import get_random_integer, random_operator, equation_to_solve

class TestMathGame(unittest.TestCase):

    def test_get_random_integer(self):
        # Test if random numbers generated are within the specified range
        minimum = 1
        maximum = 10
        for _ in range(1000):  # Test a large number of random values
            random_number = get_random_integer(minimum, maximum)
            self.assertTrue(minimum <= random_number <= maximum)

    def test_random_operator(self):
        result = random_operator()
        self.assertIsInstance(result, str)
        self.assertTrue(result, ['+', '-', '*'])

    def test_equation_to_solve(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (-6, 1, '+', '-6 + 1', -5),
                (20, 3, '-', '20 - 3', 17),
                (12, 5, '*', '12 * 5', 60),
                (8, 3, '-', '8 - 3', 5),
                (5, 7, '*', '5 * 7', 35)
            ]

            for number_1, number_2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = equation_to_solve(number_1, number_2, operator)
                self.assertTrue(problem, expected_problem)
                self.assertTrue(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
