from PIL import Image
import os , sys

def newimg():
    newimg = Image.new('RGB', (750, 600), 'red')
    newimg.save(r'/home/vsnew05/桌面/Notes/OtherInfo/algorithm/img/new.png')
    newimg.show()
    newimg2 = Image.new('RGB', (750, 600), (255, 255, 0, 120))
    newimg2.save(r'/home/vsnew05/桌面/Notes/OtherInfo/algorithm/img/new2.png')
    newimg2.show()


def cropimg():
    imgcroping=Image.open(imgpath)
    imgcroping = imgcroping.crop((750,600,500,300))
    imgcroping.show()

# def chanllageimg():
#
#
#
# def compound():



def open():
    img = Image.open(imgpath)
    width, height = img.size
    print(img.size,width,height)
    print(img.format,img.format_description)
    img.save(r'/home/vsnew05/桌面/Notes/OtherInfo/algorithm/img/go.jpg')
    img.show()
if __name__ == "__main__":

    imgpath = r'/home/vsnew05/桌面/Notes/OtherInfo/algorithm/img/12220.jpg'
    # open()
    # compound()
    cropimg()