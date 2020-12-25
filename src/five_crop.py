import torchvision.transforms as transforms

from PIL import Image


def main():

    img = Image.open('./data/timg.jpeg') 
    # 图片大小是 256*256

    size = 100  
    transform = transforms.FiveCrop(size)
    imgt = transform(img)
    for i, imgt in enumerate(imgt):
        imgt.save('./data/five_crop_'+str(i)+'.jpeg')

#     # 
#     transform = Compose([
#         FiveCrop(size), # 得到一个PIL图片数组
#         Lambda(lambda crops: torch.stack([ToTensor()(crop) for crop in crops])) # 返回一个4D tensor
#    ])
    #In your test loop you can do the following:
    # input, target = batch # input 是一个 5d tensor, target 是 2d
    # bs, ncrops, c, h, w = input.size()
    # result = model(input.view(-1, c, h, w)) # 融合 batch size 和 ncrops 变成4d
    # result_avg = result.view(bs, ncrops, -1).mean(1) # 拆结果

    
    


if __name__ == "__main__":
    main()
