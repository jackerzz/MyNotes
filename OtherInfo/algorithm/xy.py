from PIL import Image


from PIL import Image

def join(png1, png2, flag='horizontal'):
    """
    :param png1: path
    :param png2: path
    :param flag: horizontal or vertical
    :return:
    """
    img1, img2 = Image.open(png1), Image.open(png2)
    size1, size2 = img1.size, img2.size
    if flag == 'horizontal':
        joint = Image.new('RGB', (size1[0]+size2[0], size1[1]))
        loc1, loc2 = (0, 0), (size1[0], 0)
        joint.paste(img1, loc1)
        joint.paste(img2, loc2)
        joint.save('horizontal.png')
    elif flag == 'vertical':
        joint = Image.new('RGB', (size1[0], size1[1]+size2[1]))
        loc1, loc2 = (0, 0), (0, size1[1])
        joint.paste(img1, loc1)
        joint.paste(img2, loc2)
        joint.save('vertical.png')

def resize_and_crop_video_thumbnail(img_thumbnail, width, height):
    w, h = img_thumbnail.size
    if float(w)/float(h) > width/height:
        img_thumbnail = img_thumbnail.resize(
            (int(float(height/float(h))*float(w)), height), Image.ANTIALIAS)
        w, h = img_thumbnail.size
        img_thumbnail = img_thumbnail.crop((w/2-width/2, 0, w/2+width/2,
                                                height))
    else:
        img_thumbnail = img_thumbnail.resize(
            (width, int(float(width/float(w))*float(h))), Image.ANTIALIAS)
        w, h = img_thumbnail.size
        img_thumbnail = img_thumbnail.crop((0, h/2-height/2, width,
                                                h/2+height/2))
    return img_thumbnail

def iamge_transpose(image1,image2):
    NEW = Image.new("RGB",(750,600),750)
    x,_ = NEW.size
    xLeft = x // 2
    boxLeftNew,boxRightNew  = (0, 0),(xLeft, 0)
    image1 = resize_and_crop_video_thumbnail(image1,700,300)
    image2 = resize_and_crop_video_thumbnail(image2,275,300)
    image1.show()
    image2.show()
    print(image1.size,image2.size)
    NEW.paste(image1, boxLeftNew)
    NEW.paste(image2, boxRightNew)
    return NEW


def run(png1,png2):
    img1, img2 = Image.open(png1), Image.open(png2)
    print(img2.size)
    avatar = iamge_transpose(img1,img2)
    avatar.save("new.png")




if __name__ == '__main__':
    png1 = 'ss.jpg'
    png2 = '13572.jpg'
    # imageFName = '13572.jpg'
    run(png1,png2)
    
    
    # join(png1, png2)
    # join(png1, png2, flag='vertical')