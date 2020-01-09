from gpiozero import MotionSensor


def motionDetected():

    pir = MotionSensor(4)
    pir.wait_for_motion()
    return "Motion detected!"