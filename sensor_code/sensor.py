def sensor():
    from gpiozero import MotionSensor
    from auth import (key)
    pir = MotionSensor(4)
    pir.wait_for_motion()
    r = requests.post(key)
    print("Motion detected!")

sensor()
