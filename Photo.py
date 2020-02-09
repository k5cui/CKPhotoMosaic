from PIL import Image

im = Image.open("assets/carolyn.png")

im = im.resize((500, 500))

colourarr = [[]]

def avgColour(imgregion):
    r,g,b = [0,0,0]
    for i in range(0, 49):
        for i in range(0,49):
            tempr,tempg,tempb = imgregion.getpixel((i,j))
            #print(tempr,tempg,tempb)
            r=r+tempr
            g=g+tempg
            b=b+tempb
            #r,g,b = r,g,b + tempr,tempg,tempb
    #r,g,b = r,g,b/2500
    r=r/2500
    g=g/2500
    b=b/2500
    return r,g,b
    #r, g, b = imgregion.getpixel((1,1))
    #print(r, g, b)

for i in range(0, 9):
    for j in range (0, 9):
        box = (50 * i, 50 * j, 50 * (i + 1), 50 * (j + 1));
        subsection = im.crop(box)
        sectionRGB = subsection.convert('RGB')
        avgColour(sectionRGB)
        #colourarr[]

