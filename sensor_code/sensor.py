import requests
import os
from gpiozero import MotionSensor
from picamera import PiCamera
from encoded_img import (image)
from auth import (key)


def cam():
    camera = PiCamera()
    camera.capture('/home/pi/Desktop/motion_photos/pic.png')
    camera.close()


def pir(motion_sensor):
    pir = motion_sensor(4)
    pir.wait_for_motion()


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


if __name__ == '__main__':
    sensor()
