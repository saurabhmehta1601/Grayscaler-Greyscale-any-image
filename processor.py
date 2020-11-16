from PIL import Image


def processor(filename):
    file='./images/'+filename
    img=Image.open(file)
    greyimg=img.convert('L')
    greyimg.save(file)

processor('5XqgSe.jpg')
