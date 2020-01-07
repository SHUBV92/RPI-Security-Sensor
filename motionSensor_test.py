import unittest 
from motionSensor import motionDetected

class NameTestCase(unittest.TestCase):

    def test_motion_has_been_detected(self):
        result = motionDetected()
        self.assertEqual(result, "Motion detected!")

  