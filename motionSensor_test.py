import unittest 
from motionSensor import motionDetected

class NameTestCase(unittest.TestCase):

    def test_motion_has_been_detected(self):
        result = motionDetected()
        self.assertEqual(result, "Motion detected!")

    # def test_first_last_middle_name(self):
    #     result = formatted_name("chris", "topher", "barnet")
    #     self.assertEqual(result, "Chris Topher Barnet")