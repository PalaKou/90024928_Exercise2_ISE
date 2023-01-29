from Q3PartA import percentage
import unittest

class TestPercentage(unittest.TestCase):
    def test_valid_inputs(self):
        inputs = [(50, 100), (60, 120), (80, 100)]
        expected_outputs = [50.0, 50.0, 80.0]
        error_msgs = ["Error1", "Error2", "Error3"]

        for i in range(len(inputs)):
            self.assertAlmostEqual(percentage(*inputs[i]), expected_outputs[i], delta=0.01, msg=error_msgs[i])
    def test_invalid_inputs(self):
        inputs = [(0, 100), (100, 0), (100, 50), (-100, 50), (50, -100)]
        expected_outputs = [-1, -1, -1, -1, -1]
        error_msgs = ["Error4", "Error5", "Error6", "Error7", "Error8"]
                        
        for i in range(len(inputs)):
            self.assertEqual(percentage(*inputs[i]), expected_outputs[i], msg=error_msgs[i])
if __name__== '__main__':
    unittest.main()
