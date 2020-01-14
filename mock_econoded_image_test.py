import unittest 
import base64 
import image_manipulate from encoded_img

class Base64TestCase(unittest.TestCase):

 def test_image_manipulate(self):
    img = image_manipulate()
    self.assertTrue(img, True)

    if __name__ == '__main__':
        unittest.main()
