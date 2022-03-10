import os
from PIL import Image
import traceback

# This script is used to resize all your images, traits and bases to the dimensions you need.

# Can be edited to the dimensions you need.
size = 707, 1000


def resizer():
    for file in os.listdir('./traits'):
        for image in os.listdir(f'./traits/{file}'):
            try:
                fp = f'./traits/{file}/{image}'
                im = Image.open(fp)
                im2 = im.resize(size)
                im2.save(f'./traits/{file}/{image}', "PNG")
                print(f"Resized {image}")
            except IOError:
                traceback.print_exc()
                print("Cannot create thumbnail for '%s'" % image)


resizer()
