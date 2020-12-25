import torchvision.transforms as transforms
from PIL import Image

def main():

    img = Image.open('./data/img.jpeg')  # 原图大小695,391
    # ============ size
    sizes = [224, (224, 224), (224,) ,[224]] 
    for i, size in enumerate(sizes):
        transform = transforms.RandomCrop(size)
        imgt = transform(img)
        imgt.save('./data/random_crop_s' +str(i)+ '.jpeg')

    # # ============ padding
    size = 400
    paddings = [50,(50,),(50, 100),(50, 100, 150, 200),
                [50],[50, 100],[50, 100, 150, 200]]
                # padding = 4 (pad_if_needed=False会报错，True不会);
    for i, padding in enumerate(paddings):
        transform = transforms.RandomCrop(size, padding=padding,pad_if_needed=False)
        imgt = transform(img)
        imgt.save('./data/random_crop_p' + str(i)+'.jpeg')

    # # ==== fill 
    size = 500
    padding = 100
    fills = [255,(0,255,255)]
    for i, fill in enumerate(fills):
        transform = transforms.RandomCrop(size, padding=padding, fill=fill)
        imgt = transform(img)
        imgt.save('./data/random_crop_f'+str(i)+'.jpeg')

    # # ==== padding_mode 
    img = Image.open('./data/timg.jpeg')  # 图片大小是 256*256   
    size = 1200
    padding = 100
    fill = (255,0,255)  
    padding_modes = ["constant","edge" ,"reflect" ,"symmetric"]
    for i, padding_mode in enumerate(padding_modes):
        transform = transforms.RandomCrop(size, padding=padding,pad_if_needed=True, padding_mode='reflect')
        imgt = transform(img)
        imgt.save('./data/random_crop_m'+str(i)+'.jpeg')


if __name__ == "__main__":
    main()
