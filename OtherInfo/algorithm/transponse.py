from PIL import Image
# import Image as img
import os,sys

def Cutting(currentFile):

    imgTypes = ['.png','.jpg','.bmp']

    horizon = 8
    vertic  = 1

    for root, dirs, files in os.walk('.'):
        for currentFile in files:
            crtFile = root + '\\' + currentFile
            if crtFile[crtFile.rindex('.'):].lower() in imgTypes:
                crtIm = img.open(crtFile)
                crtW, crtH = crtIm.size
                hStep = crtW // horizon
                vStep = crtH // vertic
                for i in range(vertic):
                    for j in range(horizon):
                        crtOutFileName = crtFile[:crtFile.rindex('.')] + \
                            '_' + str(i) + '_' + str(j)\
                            + crtFile[crtFile.rindex('.'):].lower()
                        box = (j * hStep, i * vStep, (j + 1) * hStep, (i + 1) * vStep)
                        cropped = crtIm.crop(box)
                        cropped.save(crtOutFileName)
    return  cropped   

def iamge_transpose(image):
    '''
        Input: a Image instance
        Output: a transposed Image instance
        Function:
            * switches the left and the right part of a Image instance
            * for the left part of the original instance, flips left and right\
                and then make it upside down.
    '''
    xsize, ysize = image.size  
    xsizeLeft    = xsize // 2 # while xsizeRight = xsize - xsizeLeft

    boxLeft      = (0, 0, xsizeLeft, ysize)
    boxRight     = (xsizeLeft, 0, xsize, ysize)
    boxLeftNew   = (0, 0, xsize - xsizeLeft, ysize)
    boxRightNew  = (xsize - xsizeLeft, 0, xsize, ysize)

    partLeft     = image.crop(boxLeft).transpose(Image.FLIP_LEFT_RIGHT).\
        transpose(Image.ROTATE_180)
    # crop() 方法将原图 boxLeft 的区域（也就是原图的左半边）切下来
    # transpose() 方法先后进行左右颠倒和旋转 180° 的工作
    partRight    = image.crop(boxRight)
    # crop() 方法将原图 boxRight 的区域（也就是原图的右边半边）切下来
    image.paste(partRight, boxLeftNew)
    image.paste(partLeft, boxRightNew)
    # paste() 方法，将前两步得到的 partLeft 和 partRight 分别粘贴到指定的区域
    return image

def Dichotomous(image):
    x,y=750,600
    xsize,ysize = image.size
    xsizeLeft = xsize // 2
    print(xsize)

    boxLeft = (0 , 0, xsizeLeft, ysize)
    boxRight = (xsizeLeft, 0, xsize, ysize)

    boxLeftNew = (0, 0,x // 2, y)
    boxRightNew = (x // 2, 0, x, y)

    partLeft = image.crop(boxLeft)
    partRight = image.crop(boxRight)
    newimg = image.new(RGB,(750,600))
    
    image.frombuffer(partLeft,partRight)
    # image.paste(partRight, boxLeftNew)
    # image.paste(partLeft, boxRightNew)
    # image.thumbnail((750,600))
    return image

def Dichotomous1(img1,img2):
    img1 = Image.open(img1)
    img2 = Image.open(img2)
    x,y=750,600
    boxLeft = (y , x // 2, y, x//2)
    boxRight = (y , x // 2, y, x // 2)

    # boxLeftNew = (0, 0,x // 2, y)
    # boxRightNew = (x // 2, 0, x, y)

    partLeft = newimg.crop(img1)
    partRight = newimg.crop(img2)
    newimg.paste(partRight, boxLeftNew)
    newimg.paste(partLeft, boxRightNew)
    return newimg




def Thumbnail(img1,img2):
    from PIL import ImageChops
    img1 = Image.open(img1)
    img2 = Image.open(img2)
    img = ImageChops.multiply(img1,img2)
    x,y = img.size
    print(x,y)
    img.save(r"/home/vsnew05/桌面/Notes/OtherInfo/algorithm/img/sands.png")
    print(img.size)
    img.show()





    

def run():
   
    avatar = Image.open(imageFName)
    avatar = Dichotomous1(avatar)
    avatar.save(r"/home/vsnew05/桌面/Notes/OtherInfo/algorithm/img/s3.png")


if __name__ == "__main__":
    imageFName = r'/home/vsnew05/桌面/Notes/OtherInfo/algorithm/img/12220.jpg'
    imageFName1 = r'/home/vsnew05/桌面/Notes/OtherInfo/algorithm/img/13572.jpg'
    # run()
    # Thumbnail(imageFName,imageFName1)
    Dichotomous1(imageFName,imageFName1)