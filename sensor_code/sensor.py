import requests
import os
import base64
from time import sleep
from gpiozero import MotionSensor
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
            blue_on()
            pir
            system_on()
            cam()
            image = image_manip()
            r1 = requests.post(URL, {'image' : image })
            r2 = requests.post(key)
            system_off()
            #blue_off()
            sleep(15)
        else:
            print('testing')
            return "Motion detected"

if __name__ == '__main__':
    sensor()
