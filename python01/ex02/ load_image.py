from PIL import Image
import numpy as np

def ft_load(path: str):
    try:
        img = Image.open(path)
        array = np.array(img)
        print("The shape of image is: ", array.shape)
        return array
    except:
        print("Error loading the image!")

print(ft_load("landscape.jpg"))