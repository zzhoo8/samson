# coding:utf-8


from samson.base.image import ImageItem


if __name__ == '__main__':
    image = ImageItem(path="/Users/zzhoo8/IMG_9584.JPG")
    # image.image.show()
    image.thumbnails_for_post()