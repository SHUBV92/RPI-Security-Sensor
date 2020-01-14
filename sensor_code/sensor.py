import requests
import os
import base64
from time import sleep
from gpiozero import MotionSensor, LED, Buzzer
from camera import cam
from led_buzzer import *
from encoded_img import image_manip
from registration import (key)
from url import (URL)

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
