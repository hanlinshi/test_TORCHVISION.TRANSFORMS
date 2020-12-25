import torchvision.transforms as transforms

from PIL import Image


def main():

    img = Image.open('./data/timg.jpeg') # 原图大小695,391
    for i in range(6):
        transform = transforms.RandomPerspective(distortion_scale=0.5, p=0.5, 
                interpolation=2, fill=0)
        imgt = transform(img)
        imgt.save('./data/random_perspective' + str(i) + '.jpg')
    
    interpolations = [0,2,3]
    for i,interpolation in enumerate(interpolations):
        transform = transforms.RandomPerspective(distortion_scale=0.5, p=1, 
                interpolation=interpolation, fill=0)
        imgt = transform(img)
        imgt.save('./data/random_perspective_i' + str(i) + '.jpg')

if __name__ == "__main__":
    main()
