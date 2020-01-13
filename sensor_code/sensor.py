import requests
import os
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

def pir(motion_sensor):
    pir = motion_sensor(17)
    pir.wait_for_motion()

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

if __name__ == '__main__':
    sensor()
