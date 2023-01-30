from Q3PartC import guessing_game
import unittest
import io
import sys

class TestGuessingGame(unittest.TestCase):
    def test_answer_lt_42(self):
        inputs = io.StringIO("20\n42\n")
        expected_output = "Too low\nYou got it!\n"
                
        sys.stdin = inputs
        captured_output = io.StringIO()
        sys.stdout = captured_output

        guessing_game()
                                                        
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)                                                                        
    def test_answer_eq_42(self):
        
        inputs = io.StringIO("42\n")
        expected_output = "You got it!\n"
                
        sys.stdin = inputs
        captured_output = io.StringIO()
        sys.stdout = captured_output

        guessing_game()
                                                        
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
    def test_answer_gt_42(self):
        
        inputs = io.StringIO("20\n42\n")
        expected_output = "Too low\nYou got it!\n"
                
        sys.stdin = inputs
        captured_output = io.StringIO()
        sys.stdout = captured_output

        guessing_game()
                                                        
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)                                                                        
if __name__ == '__main__':
    unittest.main()
