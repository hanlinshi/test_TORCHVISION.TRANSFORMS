import torchvision.transforms as transforms
from PIL import Image


def main():

    img = Image.open('./data/timg.jpeg') 
    # 图片大小是 256*256
    
    degrees = 30
    for i in range(30):
        transform = transforms.RandomRotation(degrees=degrees)
        imgt = transform(img)
        imgt.save('./data/random_rotation_d' + str(i) + ".jpeg")
    
    # =======
    degrees = 30
    resamples = [0,2,3]
    for i,resample in enumerate(resamples):
        transform = transforms.RandomRotation(degrees=degrees, resample=resample)
        imgt = transform(img)
        imgt.save('./data/random_rotation_r'+str(i)+'.jpeg')
    # # ======= 
    degrees = 45
    expands = [True,False]
    for i, expand in enumerate(expands):
        transform = transforms.RandomRotation(degrees=degrees, expand=expand)
        imgt = transform(img)
        imgt.save('./data/random_rotation_e'+str(i)+'.jpeg')

    # # # ======= 
    degrees = 45
    expands = [True,False]
    center = (10,10)
    for j,expand in enumerate(expands):
        for i in range(9):
            transform = transforms.RandomRotation(degrees=degrees, expand=expand, center=center)
            imgt = transform(img)
            imgt.save('./data/random_rotation_c' +str(j)+'_'+ str(i)+'.jpeg')

    # # # ======= 
    degrees = 34.5
    fills = [123,(0,255,255)]
    center = (100,100)
    for i, fill in enumerate(fills):
        transform = transforms.RandomRotation(degrees=degrees,fill=fill,center=center)
        imgt = transform(img)
        imgt.save('./data/random_rotation_f'+str(i)+'.jpeg')

if __name__ == "__main__":
    main()
