from PIL import Image

finalX, finalY = 520, 520
width, height = 40, 40
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
            # r,g,b = r,g,b + tempr,tempg,tempb
    # r,g,b = r,g,b/2500
    r = int(r / (sectionWidth * sectionHeight))
    g = int(g / (sectionWidth * sectionHeight))
    b = int(b / (sectionWidth * sectionHeight))
    return r, g, b
    # r, g, b = imgregion.getpixel((1,1))
    # print(r, g, b)

im = Image.open("assets/weeb.jpg")

im = im.resize((finalX, finalY))

colourArr = [[(0, 0, 0) for x in range(width)] for y in range(height)]

finalImage = Image.new('RGB', (finalX, finalY))

for i in range(0, width):
    for j in range(0, height):
        box = (sectionWidth * i, sectionHeight * j, sectionWidth * (i + 1), sectionHeight * (j + 1))
        subsection = im.crop(box)
        sectionRGB = subsection.convert('RGB')
        colourArr[i][j] = avgColour(sectionRGB)
        tempImage = Image.new('RGB', (sectionWidth, sectionHeight), colourArr[i][j])
        finalImage.paste(tempImage, (i * sectionWidth, j * sectionHeight))

finalImage.save('assets/result.jpg')


