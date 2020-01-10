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

    if __name__ == '__main__':
        unittest.main()
