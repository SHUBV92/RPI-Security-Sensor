import base64

def image_manipulate():

    with open("./app/assets/images/image.png", "rb") as image_file:

        img_data = image_file.read()
        encoded_img = base64.b64encode(img_data)

        decoded_img = base64.b64decode(encoded_img)
        second_encoded_img = base64.b64encode(decoded_img)
        print("Test")
        print (second_encoded_img == encoded_img)

