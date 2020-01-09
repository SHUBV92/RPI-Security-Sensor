import unittest
from sensor import *

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
