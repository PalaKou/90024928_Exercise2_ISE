from Q3PartA import percentage
from Q3PartB import reactor_core_warning
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
class TestReactorCoreWarning(unittest.TestCase):
    def test_reactor_core_warning(self):
        inputs = [150, 500, 700, 925, 1050, 1200]
        expected_outputs = ["Danger! Core temp too low", "Warning! Core temp low. Decreased efficiency.",
                            "Reactor core operating at standard temperatures",
                            "Reactor core operating at increased temperatures",
                            "Warning! Core temp High. Deploy control rods.",
                            "Danger! Core temp too high"]
        error_msgs = ["Error1", "Error2", "Error3", "Error4", "Error5", "Error6"]

        for i in range(len(inputs)):
            self.assertEqual(reactor_core_warning(inputs[i]), expected_outputs[i], error_msgs[i])

if __name__== '__main__':
    unittest.main()
