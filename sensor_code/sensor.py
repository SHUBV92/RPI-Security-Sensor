from gpiozero import MotionSensor
from picamera import PiCamera
import requests
from auth import (key)
from encoded_img import (image)

def cam():
    camera = PiCamera()
    camera.capture()
    camera.close

def pir(motion_sensor):
    pir = motion_sensor(4)
    pir.wait_for_motion()

def sensor(motion_sensor = MotionSensor):
    pir
    cam()
    r = requests.post(key, URL, params = image)
    return "Motion detected!"

if __name__ == '__main__':
    sensor()
