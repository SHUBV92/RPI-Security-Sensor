import base64

with open(image, "rb") as image_file:
    my_string = base64.b64encode(image_file.read())
    image = my_string.decode('utf-8')
