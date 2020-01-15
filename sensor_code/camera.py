from picamera import PiCamera

def cam():
    camera = PiCamera()
    camera.resolution = (500, 375)
    camera.capture(file_name)
    camera.close()
