import torchvision.transforms as transforms
from PIL import Image


def main():

    img = Image.open('./data/timg.jpeg') 
    # 图片大小是 256*256

    transform = transforms.RandomVerticalFlip(p=1)
    imgt = transform(img)
    imgt.save('./data/vertical_flip.jpeg')


if __name__ == "__main__":
    main()
