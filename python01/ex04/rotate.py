from PIL import Image

img = Image.open("./landscape.jpg")
img = img.rotate(90)
img.resize(img.size * 2)

img.show()