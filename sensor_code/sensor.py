import requests
import os
<<<<<<< HEAD
from gpiozero import MotionSensor
from picamera import PiCamera
from encoded_img import (image)
from auth import (key)


def cam():
    camera = PiCamera()
    camera.capture('/home/pi/Desktop/motion_photos/pic.png')
    camera.close()

=======
import base64
from gpiozero import MotionSensor
from picamera import PiCamera
from encoded_img import image_manip
from auth import (key)
from url import (URL)
from led import lights_and_sound

def cam():
    camera = PiCamera()
    camera.resolution = (500, 375)
    camera.capture()
    camera.close()
>>>>>>> f92c9bd0f224bd98ced16c3c32dcc7cb3e202c64

def pir(motion_sensor):
    pir = motion_sensor(17)
    pir.wait_for_motion()

<<<<<<< HEAD

def sensor(motion_sensor=MotionSensor):
    testing = os.getenv('TESTING', 'False')
    if testing == 'FALSE':
        while True:
        pir
        cam()
        # r1 = requests.post(URL, {'image': image})
        r2 = requests.post(key)
        print(r2.text)
    else:
        print('testing')
        return "Motion detected"

=======
def sensor(motion_sensor = MotionSensor):
    testing = os.getenv('TESTING', 'False')
    if testing == 'False':
        while True:
            pir
            lights_and_sound()
            cam()
            image = image_manip()
            r1 = requests.post(key, URL, params = image)
            r2 = requests.post(key)
            print(r1)
            print(r2)
            print('done')
        else:
            print('testing')
            return "Motion detected"
    time.sleep(30)
>>>>>>> f92c9bd0f224bd98ced16c3c32dcc7cb3e202c64

if __name__ == '__main__':
    sensor()
