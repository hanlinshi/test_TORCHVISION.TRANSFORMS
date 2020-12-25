import torchvision.transforms as transforms

from PIL import Image


def main():

    img = Image.open('./data/timg.jpeg') # 原图大小256*256
    degreeses = [0, 30, 400, (-30, 60)]  
    for i, degrees in enumerate(degreeses):
        transform = transforms.RandomAffine(degrees)
        imgt = transform(img)
        imgt.save('./data/random_affine_d' + str(i) + '.jpg')

    degrees = 0
    translates = [(0,0.5),(0.5,0),(1,1)]
    for i, translate in enumerate(translates):
        transform = transforms.RandomAffine(degrees, translate=translate)
        imgt = transform(img)
        imgt.save('./data/random_affine_t' + str(i) + '.jpg')

    degrees = 0
    scales = [(0.1,0.2),(1,100),(1,1)]
    for i, scale in enumerate(scales):
        transform = transforms.RandomAffine(degrees, scale=scale)
        imgt = transform(img)
        imgt.save('./data/random_affine_sc' + str(i) + '.jpg')
    
    degrees = 0
    shears = [30,[-30,30],[0,10,20,30]] 
    for i, shear in enumerate(shears):
        transform = transforms.RandomAffine(degrees, shear=shear)
        imgt = transform(img)
        imgt.save('./data/random_affine_sh' + str(i) + '.jpg')
    
    degrees = 0
    scale=(3,3)
    resamples = [0,2,3]
    for i, resample in enumerate(resamples):
        transform = transforms.RandomAffine(degrees,scale=scale, resample=resample)
        imgt = transform(img)
        imgt.save('./data/random_affine_r' + str(i) + '.jpg')

    degrees = 0
    translate=(0.5,0.5)
    fillcolors = [122,(0,234,121)]
    for i, fillcolor in enumerate(fillcolors):
        transform = transforms.RandomAffine(degrees,translate=translate, fillcolor=fillcolor)
        imgt = transform(img)
        imgt.save('./data/random_affine_f' + str(i) + '.jpg')
    degrees = 0
    scale=(0.5,0.5)
    fillcolors = [122,(0,234,121)]
    for i, fillcolor in enumerate(fillcolors):
        transform = transforms.RandomAffine(degrees,scale=scale, fillcolor=fillcolor)
        imgt = transform(img)
        imgt.save('./data/random_affine_f' + str(i+2) + '.jpg')
    
if __name__ == "__main__":
    main()
