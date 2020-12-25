import torchvision.transforms as transforms

from PIL import Image   


def main():

    img = Image.open('./data/timg.jpeg') 
    # 图片大小是 256*256

    size = 100  
    transform = transforms.TenCrop(size)
    imgts = transform(img)
    for i, imgt in enumerate(imgts):
        imgt.save('./data/ten_crop_'+str(i)+'.jpeg')


if __name__ == "__main__":
    main()