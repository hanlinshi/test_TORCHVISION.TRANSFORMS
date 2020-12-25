import torchvision.transforms as transforms
from PIL import Image   


def main():

    img = Image.open('./data/img.jpeg') # 原图大小695,391
    
    sizes = [150,(150, 150)]
    for i, size in enumerate(sizes):
        transform = transforms.Resize(size)
        imgt = transform(img)
        imgt.save('./data/resize_s'+str(i)+'.jpeg')


    size = (150, 150)
    interpolations = [0,1,2,3,4,5]
    for i, interpolation in enumerate(interpolations):
        transform = transforms.Resize(size=size, interpolation=interpolation)
        imgt = transform(img)
        imgt.save('./data/resize_i'+str(i)+'.jpeg')

if __name__ == "__main__":
    main()