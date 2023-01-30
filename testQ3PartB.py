from Q3PartB import reactor_core_warning
import unittest

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
if __name__ == '__main__':
    unittest.main()
