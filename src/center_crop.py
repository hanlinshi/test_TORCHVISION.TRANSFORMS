import torchvision.transforms as transforms

from PIL import Image


def main():

    img = Image.open('./data/img.jpeg') # 原图大小695,391
    sizes = [224, (224, 224), (224,), [224]]
      
    for i, size in enumerate(sizes):
        transform = transforms.CenterCrop(size)
        imgt = transform(img)
        imgt.save('./data/center_crop_' + str(i) + '.jpg')

if __name__ == "__main__":
    main()
