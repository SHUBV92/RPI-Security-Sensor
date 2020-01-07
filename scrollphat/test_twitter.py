import unittest
from twitter import display_tweet

class TwitterTestCase(unittest.TestCase):

    def test_screen_message(self):
        result = display_tweet()
        self.assertEqual(result, "Tweet posted")

if __name__ == '__main__':
    unittest.main()
