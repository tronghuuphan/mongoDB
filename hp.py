import base64

with open("cam.jpg", "rb") as imageFile:
    img = base64.b64encode(imageFile.read())


with open("new_image.png", "wb") as new_file:
    new_file.write(img.decode('utf-8'))
