#for those who care about their weight
from PIL import Image, ImageDraw, ImageFont
import ctypes
def generatePic(weight):
    weight_str = str(weight)
    W, H = (1920,1200)
    img = Image.new('RGB', (W, H), color = (0, 0, 0))
    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype("arial.ttf", 400)
    w, h = d.textsize(weight_str,font=fnt)
    print(w,h)
    d.text(((W-w)/2,(H-h)/2), weight_str, font=fnt, fill=(255,255,255))
    
    img.save('D:/weight-pic-generator/weight_pic.png')

def setWallpaper():
    ctypes.windll.user32.SystemParametersInfoW(20, 0, 'D:/weight-pic-generator/weight_pic.png', 0)  # set wallpaper

input_weight = input("Input your weight:")
generatePic(input_weight)
setWallpaper()