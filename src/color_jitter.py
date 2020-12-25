import torchvision.transforms as transforms

from PIL import Image


def main():

    img = Image.open('./data/timg.jpeg')
    # 图片大小是 256*256
    # # ============ 默认值
    # ColorJitter(brightness=0, contrast=0, saturation=0, hue=0)
    transform = transforms.ColorJitter(brightness=2, contrast=0, saturation=0, hue=0)
    for i in range(6):
        imgt = transform(img)
        imgt.save('./data/colorjitter_b'+str(i)+'.jpeg')

    transform = transforms.ColorJitter(brightness=0, contrast=2, saturation=0, hue=0)
    for i in range(6):
        imgt = transform(img)
        imgt.save('./data/colorjitter_c'+str(i)+'.jpeg')

    transform = transforms.ColorJitter(brightness=0, contrast=0, saturation=2, hue=0)
    for i in range(6):
        imgt = transform(img)
        imgt.save('./data/colorjitter_s'+str(i)+'.jpeg')

    transform = transforms.ColorJitter(brightness=0, contrast=0, saturation=0, hue=0.5)
    for i in range(6):
        imgt = transform(img)
        imgt.save('./data/colorjitter_h'+str(i)+'.jpeg')

    

if __name__ == "__main__":
    main()
