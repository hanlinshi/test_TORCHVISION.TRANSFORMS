import torchvision.transforms as transforms

from PIL import Image


def main():

    img = Image.open('./data/timg.jpeg') # 原图大小695,391
    num_output_channelses =[1,3]
      
    for i, num_output_channels in enumerate(num_output_channelses):
        transform = transforms.Grayscale(num_output_channels)
        imgt = transform(img)
        imgt.save('./data/grayscale_' + str(i) + '.jpg')

if __name__ == "__main__":
    main()
