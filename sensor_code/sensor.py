from gpiozero import MotionSensor
from picamera import PiCamera
import requests
from auth import (key)

def pir(motion_sensor):
    pir = motion_sensor(4)
    pir.wait_for_motion()

def sensor(motion_sensor = MotionSensor):
    camera = PiCamera()
    pir(motion_sensor)
    camera.capture()
    camera.close
    r = requests.post(key)
    return "Motion detected!"

if __name__ == '__main__':
    sensor()
