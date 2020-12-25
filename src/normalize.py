import torchvision.transforms as transforms

from PIL import Image   
import cv2
import os
import numpy as np

def compute_mean_std(path):
    file_names = os.listdir(path)
    per_image_Rmean = []
    per_image_Gmean = []
    per_image_Bmean = []
    for file_name in file_names:
        print(file_name)
        img = cv2.imread(os.path.join(path, file_name), 1)
        # opencv 读图的顺序BGR;  PIL读图的顺序是RGB
        per_image_Bmean.append(np.mean(img[:, :, 0]))
        per_image_Gmean.append(np.mean(img[:, :, 1]))
        per_image_Rmean.append(np.mean(img[:, :, 2]))
    R_mean = np.mean(per_image_Rmean)/255
    G_mean = np.mean(per_image_Gmean)/255
    B_mean = np.mean(per_image_Bmean)/255
    stdR = np.std(per_image_Rmean)/255
    stdG = np.std(per_image_Gmean)/255
    stdB = np.std(per_image_Bmean)/255
    return R_mean, G_mean, B_mean, stdR, stdG, stdB



def main():
    # path = './data'
    # R_mean, G_mean, B_mean, stdR, stdG, stdB = compute_mean_std(path)
    # mean = [R_mean, G_mean, B_mean]
    # std = [stdR, stdG, stdB]
    # print(mean)
    # print(std)

    mean = [0.6376033295310112, 0.646677376905662, 0.26815270339355546]
    std = [0.1509007825836042, 0.12134844473103676, 0.07960188625607592]
    img = Image.open('./data/timg.jpeg') 
    # 图片大小是 256*256
 
    transform = transforms.Normalize(mean=mean, std=std,inplace=True)
    
    t=transforms.ToTensor()
    img = t(img)
    transform(img)
    imgt = transforms.ToPILImage()(img).convert('RGB')
    # imgt = Image.fromarray(imgt)
    imgt.save('./data/normalize_4True.jpeg')

import random
import matplotlib.pyplot as plt
import numpy as np
def main2():
    # 生成一组数据
    y = []
    # x = []
    for i in range(50):
        y.append(random.randint(100, 1000))
        # x.append(0)
    
    ymean = np.mean(y)
    ystd = np.std(ymean)+1e6
    y = np.array(y)
    yt = (y-ymean)/ystd

    fig = plt.figure()                      
    fig, ax_lst = plt.subplots(2, 1)
    x = np.linspace(100, 1000, 50)
    plt.subplot(211)
    plt.scatter(x, y, color="blue")
    plt.subplot(212)
    plt.scatter(x, yt, color="blue")

    plt.show()
    # plt.savefig('./nomalize_main2.jpg')


if __name__ == "__main__":
    # main()
    main2()