import torchvision.transforms as transforms

from PIL import Image


def main():

    img = Image.open('./data/timg.jpeg') # 原图大小695,391
      
    for i in range(6):
        transform = transforms.RandomGrayscale(p=0.5)
        imgt = transform(img)
        imgt.save('./data/random_grayscale_' + str(i) + '.jpg')

if __name__ == "__main__":
    main()
