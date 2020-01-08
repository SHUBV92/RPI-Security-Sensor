def pir():
    from gpiozero import MotionSensor
    pir = MotionSensor(4)
    pir.wait_for_motion()

def sensor():
    import requests
    from auth import (key)
    pir
    r = requests.post(key)
    print("Motion detected!")

sensor()
