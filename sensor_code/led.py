import RPi.GPIO as GPIO
import time

def lights_and_sound():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)

    GPIO.output(18, GPIO.HIGH)
    time.sleep(1)

    GPIO.output(18, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(18, GPIO.HIGH)

    time.sleep(1)

    GPIO.output(24, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(18, GPIO.HIGH)

    time.sleep(1)
