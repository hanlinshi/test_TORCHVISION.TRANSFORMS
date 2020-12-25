import torchvision.transforms as transforms

from PIL import Image   
import cv2
import os
import numpy as np

def main():
    # ======= cv2 
    # im = cv2.imread('./data/img.jpeg')
    # im BGR shape 3, 391, 695
    # t=transforms.ToTensor()
    # imgt = t(im)
    # imt = imgt.numpy()
    # imtg = imt * 255
    # imgtgp = imtg.transpose(1,2,0)
    # cv2.imwrite('./data/totensor_1.jpeg', imgtgp)
    # print("ok")

    # ===== PIL ====
    im = Image.open('./data/img.jpeg')
    # im RGB 391, 695
    t=transforms.ToTensor()
    img = t(im)
    imgt = transforms.ToPILImage()(img).convert('RGB')
    imgt.save('./data/totensor_2.jpeg')
    # print("ok")
    # 
   


if __name__ == "__main__":
    main()