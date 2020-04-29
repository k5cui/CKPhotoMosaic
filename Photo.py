from PIL import Image
import os
import math

finalX, finalY = 500, 500
width, height = 50, 50
sectionWidth, sectionHeight = int(finalX / width), int(finalY / height)

def avgColour(imgRegion):
    r, g, b = [0, 0, 0]
    for i in range(0, sectionWidth):
        for j in range(0, sectionHeight):
            tempr, tempg, tempb = imgRegion.getpixel((i, j))
            # print(tempr,tempg,tempb)
            r = r + tempr
            g = g + tempg
            b = b + tempb
    r = int(r / (sectionWidth * sectionHeight))
    g = int(g / (sectionWidth * sectionHeight))
    b = int(b / (sectionWidth * sectionHeight))
    return r, g, b

def colourDist(tup1, tup2):
    dist = 0
    for i in range(0, 3):
        dist = dist + math.pow((tup1[i] - tup2[i]), 2)
    dist = math.sqrt(dist)
    return dist

def findBestPic(tupie, manytupie):
    shortest = 9999
    for i in range(0, len(manytupie)):
        if colourDist(tupie, manytupie[i]) < shortest:
            shortest = colourDist(tupie, manytupie[i])
            bestpic = i
            continue
    return bestpic

im = Image.open("assets/weeb.jpg")

im = im.resize((finalX, finalY))

colourArr = [[(0, 0, 0) for x in range(width)] for y in range(height)]

finalImage = Image.new('RGB', (finalX, finalY))

numpix = 32
pix = [0 for x in range(numpix)]
aveColorpix = [0 for y in range(numpix)]
counter = 0

for filename in os.listdir("assets/pewpix"):
    if filename.endswith(".jpg"):
        pix[counter] = Image.open("assets/pewpix/" + filename)
        temppix = pix[counter].convert("RGB")
        aveColorpix[counter] = avgColour(temppix)
        counter = counter + 1
        continue
    else:
        continue

for i in range(0, width):
    for j in range(0, height):
        box = (sectionWidth * i, sectionHeight * j, sectionWidth * (i + 1), sectionHeight * (j + 1))
        subsection = im.crop(box)
        sectionRGB = subsection.convert('RGB')
        colourArr[i][j] = avgColour(sectionRGB)
        finalImage.paste(pix[findBestPic(colourArr[i][j], aveColorpix)], (i * sectionWidth, j * sectionHeight))
        # tempImage = Image.new('RGB', (sectionWidth, sectionHeight), colourArr[i][j])
        # finalImage.paste(tempImage, (i * sectionWidth, j * sectionHeight))

finalImage.save('assets/result.jpg')