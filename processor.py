from PIL import Image


def processor(filename,filepath):
    file=filepath+filename
    img=Image.open(file)
    greyimg=img.convert('L')
    greyimg.save(file)

