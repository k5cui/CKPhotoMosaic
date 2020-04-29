from PIL import Image
import os
numpix = 32
pix = [0 for x in range(numpix)]
counter = 0
for filename in os.listdir("assets/example_square_images"):
    if filename.endswith(".jpg"):
        pix[counter] = Image.open("assets/example_square_images/" + filename)
        pix[counter] = pix[counter].resize((10, 10))
        pix[counter].save("assets/pewpix/" + filename)
        counter = counter + 1
        continue
    else:
        continue