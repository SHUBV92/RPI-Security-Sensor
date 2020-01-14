import base64

def image_manip():
    with open(image, "rb") as image_file:
        my_string = base64.b64encode(image_file.read())
        image = my_string.decode('utf-8')
    return image
