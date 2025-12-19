from PIL import Image

img = Image.open("./animal.jpeg")
zoom = 2.0
print(img.width, img.height)
old_width =img.width
olg_height = img.height
img = img.resize((int(img.width * 2), int(img.height * 2)))
img = img.crop((400,400, 400, 400))
print(img.width, img.height)
img.show()