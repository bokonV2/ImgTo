# env\Scripts\activate
from PIL import Image, ImageDraw, ImageFont
from pprint import pprint
from progress.bar import Bar




palette = "&$Xx=+;:. "
palette = " .:;+=xX$&"
# palette = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
# palette = " .'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
# font = ImageFont.truetype("Cousine-Bold.ttf")
font = ImageFont.truetype("Cousine-BoldItalic.ttf")

palette_line = list(range(0,255,int(255/len(palette))+1))
palette_line[-1] = 255
# print(palette_line)
name = "test.jfif"
# name = "test.jpg"
# name = "result.jpg"
image = Image.open(name).convert('L')
imageC = Image.open(name)
# image.show()
# image = Image.open("test2.png").convert('L')

# windhLen = 500
# width, height = image.size
# image = image.resize((windhLen, int(height*windhLen/width)))
# imageC = imageC.resize((windhLen, int(height*windhLen/width)))

pixels = image.load()
pixelsC = imageC.load()
width, height = image.size

def text(width, height, text, color):
    factor = 8
    image = Image.new("RGB", (width*factor, height*factor), "black")
    draw = ImageDraw.Draw(image)
    bar = Bar('Build', max=len(text)*len(text[0]))
    for width, textW in enumerate(text):
        for height, simbols in enumerate(textW):
            draw.text((width*factor, height*factor), simbols, font=font, fill=(color[width][height][0],color[width][height][1],color[width][height][2]))
            bar.next()
    bar.finish()
    image.save("result.jpg")
    image.show()

def paint(num):
    for i in range(len(palette_line)-1):
        if palette_line[i] <= num and palette_line[i+1] >= num:
            return palette[i]

def main():
    text = []
    color = []
    for i in range(width):
        textW = []
        colorW = []
        for j in range(height):
            textW.append(paint(pixels[i, j]))
            colorW.append((pixelsC[i,j][0],pixelsC[i,j][1],pixelsC[i,j][2]))
            # print(paint(pixels[j, i]), end="")
        text.append(textW)
        color.append(colorW)
    return text, color

if __name__ == '__main__':
    text(width, height, *main())
