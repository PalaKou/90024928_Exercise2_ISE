from Q3PartC import guessing_game 
import unittest
import io
import sys

class TestGuessingGame(unittest.TestCase):

    def test_guess_lower_than_answer(self):
        sys.stdin = io.StringIO("20")
        captured_output = io.StringIO()
        sys.stdout = captured_output

        guessing_game()
        output = captured_output.getvalue()

        self.assertIn("Too low", output)

    def test_guess_equal_to_answer(self):
        sys.stdin = io.StringIO("42")
        captured_output = io.StringIO()
        sys.stdout = captured_output

        guessing_game()
        output = captured_output.getvalue()

        self.assertIn("You got it!", output)

    def test_guess_greater_than_answer(self):
        sys.stdin = io.StringIO("60")
        captured_output = io.StringIO()
        sys.stdout = captured_output

        guessing_game()
        output = captured_output.getvalue()

        self.assertIn("Too high", output)

if __name__ == '__main__':
    unittest.main()
