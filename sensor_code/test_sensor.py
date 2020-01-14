import unittest
import os
import requests
from sensor import *

os.environ['TESTING'] = 'True'


class mockMotionSensor:
    def __init__(number):
        pass

    def wait_for_motion(self):
        sleep(1)

class SensorTestCase(unittest.TestCase):
    def test_sensor_activated(self):
        self.assertEqual(sensor(mockMotionSensor), "Motion detected!")

<<<<<<< HEAD
    if __name__ == '__main__':
        unittest.main()
=======
if __name__ == '__main__':
    unittest.main()
>>>>>>> f92c9bd0f224bd98ced16c3c32dcc7cb3e202c64
