# Script that scales image up
# Will take all png giles from "currentDir"\OriginalSize
# And scale them up + output them to "currentDir" with the same file name

import os
from PIL import Image

path = os.path.dirname(os.path.abspath(__file__)) + "\OriginalSize"
print("Getting all .png from ", path)
for file in os.listdir(path):
    if file.endswith(".png"):
        scaling = 4  # 4 time image size
        img = Image.open(path + "\\" + file)
        img = img.resize((img.size[0] * scaling, img.size[1] * scaling), Image.NEAREST)
        img.save(file)
