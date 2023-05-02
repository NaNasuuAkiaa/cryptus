from PIL import Image
import random

imagen = Image.open("image.png")
x, y = imagen.size
for i in range(x):
    for j in range(y):
        imagen.putpixel((i, j), (int(random.randint(0, 67)*3), int(random.randint(0, 67)*3), int(random.randint(0, 67)*3)))
imagen.save("image.png")