from PIL import Image
import os
folder1 = "‪D:\\dataset\\Land vehicle\\PersonBW"
#folder = folder1.strip("\u202a")
folder = os.path.normpath("D:/dataset/Land vehicle/PersonBW")
i=0
for filename in os.listdir(folder):
    im = Image.open(filename)
    rgb_im = im.convert('RGB')
    rgb_im.save("cvtdimage/PersonBW/"+i+'img.jpg')
    print(i)
    i+=1
    