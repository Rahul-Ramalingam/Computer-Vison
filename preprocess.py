import cv2
import os
import numpy as np

def blackndwhite(image):
        bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return bw

def blurimg(image):
        bi = cv2.GaussianBlur(image,(13,13),cv2.BORDER_DEFAULT)
        return bi


def noisy1(image):

        img = image[...,::-1]/255.0
        noise =  np.random.normal(loc=0, scale=1, size=img.shape)
        noisy = np.clip((img + noise*0.2),0,1)
        noisy2 = np.clip((img + noise*0.4),0,1)
        noisy2mul = np.clip((img*(1 + noise*0.2)),0,1)
        noisy4mul = np.clip((img*(1 + noise*0.4)),0,1)

        return noisy2mul

def sp(image):
      row,col,ch = image.shape
      s_vs_p = 0.8
      amount = 0.35
      out = np.copy(image)
      num_salt = np.ceil(amount * image.size * s_vs_p)
      coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in image.shape]
      out[coords] = 1
      num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
      coords = [np.random.randint(0, i - 1, int(num_pepper))
              for i in image.shape]
      out[coords] = 0
      out1 = cv2.cvtColor(out,cv2.COLOR_BGR2GRAY)
      return out

num_to_be_cnvtd = 500
folder1 = "‪D:\\projects\\python projects\\dataset\\OIDv4_ToolKit-master\\OID\\Dataset\\train\\Bird\\images"
folder = folder1.strip("\u202a")
i=1
for filename in os.listdir(folder):
        if i<=num_to_be_cnvtd:
                image_path = os.path.join(folder,filename)
                img = cv2.imread(image_path)
                cnvtd = sp(img)
                cv2.imwrite("D:\\projects\\python projects\\dataset\\OIDv4_ToolKit-master\\OID\\Dataset\\train\\Bird\\noise\\"+filename,cnvtd)
                os.remove(image_path)
                print(filename+" "+str(i))
                i+=1
        else:
                print("---------completed----------")
                break


