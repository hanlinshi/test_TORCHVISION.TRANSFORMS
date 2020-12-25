import torchvision.transforms as transforms

from PIL import Image


def main():

    img = Image.open('./data/timg.jpeg')
    # 图片大小是 256*256
    # # ============ padding
    paddings = [50,(50,),(50, 100),(50, 100, 150, 200),
                            [50], [50, 100], [50, 100, 150, 200]]
    for i, padding in enumerate(paddings):
        transform = transforms.Pad(padding=padding)
        imgt = transform(img)
        imgt.save('./data/pad_' + str(i) + '.jpeg')

    # # # ============ fill 
    padding = 50
    fills = [255, (0,255,255)]
    for i, fill in enumerate(fills):
        transform = transforms.Pad(padding=padding, fill=fill)
        imgt = transform(img)
        imgt.save('./data/pad_f' + str(i) + '.jpeg')

    # # # ==== padding_mode 
    padding = 256*2
    fill = (255,0,255)
    padding_modes = ["constant", "edge", "reflect", "symmetric"]
    for i, padding_mode in enumerate(padding_modes):
        transform = transforms.Pad(padding=padding, fill=fill,padding_mode=padding_mode)
        imgt = transform(img)
        imgt.save('./data/pad_m' + str(i) + '.jpeg')

    


if __name__ == "__main__":
    main()
