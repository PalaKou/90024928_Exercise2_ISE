from Q3PartA import percentage
import unittest

class TestPercentage(unittest.TestCase):
    def test_valid_inputs(self):
        inputs = [(40, 100), (60, 100), (80, 100)]
        expected_outputs = [40.0, 60.0, 80.0]
        error_msgs = ["Error1", "Error2", "Error3"]

        for i in range(len(inputs)):
            self.assertAlmostEqual(percentage(*inputs[i]), expected_outputs[i], delta=0.01, msg=error_msgs[i])
    def test_invalid_inputs(self):
        inputs = [(0, 30), (10, 0), (100, 5), (-10, 5), (5, -10)]
        expected_outputs = [-1, -1, -1, -1, -1]
        error_msgs = ["Error4", "Error5", "Error6", "Error7", "Error8"]
                        
        for i in range(len(inputs)):
            self.assertEqual(percentage(*inputs[i]), expected_outputs[i], msg=error_msgs[i])
if __name__== '__main__':
    unittest.main()
