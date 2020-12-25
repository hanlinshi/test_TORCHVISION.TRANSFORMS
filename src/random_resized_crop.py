import torchvision.transforms as transforms

from PIL import Image


def main():

    img = Image.open('./data/timg.jpeg') # 图片大小是 256*256
    
    sizes = [224,(224,),[224]]  
    interpolation = 0
    for i,size in enumerate(sizes):
        transform = transforms.RandomResizedCrop(size, interpolation=interpolation)
        imgt = transform(img)
        imgt.save('./data/random_resize_crop_s'+str(i)+'.jpeg')

    # 对比六种不同的插值
    size = 512  
    interpolations = [0, 1, 2, 3, 4, 5]
    scale = (2.0, 2.0)
    ratio = (1.0, 1.0)
    for i,interpolation in enumerate(interpolations):
        transform = transforms.RandomResizedCrop(size, scale=scale, ratio=ratio, interpolation=interpolation)
        imgt = transform(img)
        imgt.save('./data/random_resize_crop_i'+str(i)+'.jpeg') 


if __name__ == "__main__":
    main()
