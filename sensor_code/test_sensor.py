import unittest
from sensor import sensor

class SensorTestCase(unittest.TestCase):

    def test_sensor_activated(self):
        
        self.assertEqual(1, "Motion detected!")


    if __name__ == '__main__':
        unittest.main()
