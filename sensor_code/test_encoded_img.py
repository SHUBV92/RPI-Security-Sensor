import unittest
from encoded_img import *

class TestCase(unittest.TestCase):

    def test_encoded_img(self):
        self.assertIsInstance(image_manip(), str)

if __name__=='__main__':
    unittest.main()
