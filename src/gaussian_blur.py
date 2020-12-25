import torchvision.transforms as transforms

from PIL import Image


def main():

    img = Image.open('./data/timg.jpeg') # 
    kernel_sizes = [1,3,5,7,9,11]
    for i, size in enumerate(kernel_sizes):
        transform = transforms.GaussianBlur(kernel_size=size, sigma=(10.0, 10.0))
        imgt = transform(img)
        imgt.save('./data/gaussian_blur_' + str(i) + '.jpg')

    img = Image.open('./data/timg.jpeg') # 
   
    for i in range(6):
        transform = transforms.GaussianBlur(kernel_size=11, sigma=(0.1, 10.0))
        imgt = transform(img)
        imgt.save('./data/gaussian_blur_s' + str(i) + '.jpg')

if __name__ == "__main__":
    main()
