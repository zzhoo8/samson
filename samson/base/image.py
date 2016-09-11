# coding:utf-8

"""
    图片
"""

from PIL import Image, ImageDraw
from PIL import ImageEnhance
from PIL.ExifTags import TAGS


class ImageItem(object):

    image = None

    def __init__(self, **kwargs):
        """
        图像构造函数
        :param kwargs:
        """

        # 从文件中获取图像
        if "path" in kwargs:
            path = kwargs.get('path')
            self.image = Image.open(path)
        else:
            pass

    def thumbnails_for_post(self, out=None):
        """
        适合推到社交网络的缩略图,保持比例
        :return:
        """
        from samson import samson
        if self.image is None:
            return None

        # 原图比例
        x, y = self.image.size
        ratio = x * 1.0 / y * 1.0

        # 按比例缩放到合适尺寸,小边优先
        size = samson.config.get('THUMB_SIZE')
        xx = int(size[0] if size[0] < size[1] else size[1] * ratio)
        yy = size[1]
        self.image.thumbnail((xx, yy), Image.BICUBIC)

        # 原图增加1像素的边缘线
        # xx += 1
        # yy += 1
        # line = Image.new("RGBA", (xx, yy), (255, 255, 255))
        # line.paste(self.image, box=(1, 1))

        # 增加exif信息之后的图片大小
        # 安全色参考 http://www.bootcss.com/p/websafecolors/
        xx += 80
        yy += 80
        # thumb = Image.new("RGBA", (xx, yy), (51, 51, 51))
        thumb = Image.new("RGBA", (xx, yy), (238, 238, 238))

        # 拼接,取边框大小
        # thumb.paste(self.image, box=(40, 40))
        thumb.paste(self.image, box=(40, 40))

        # 写入Exif信息
        if hasattr(self.image, '_getexif'):
            raw_exif = self.image._getexif()
            exif = dict()
            for key, value in raw_exif.items():
                key = TAGS.get(key)
                exif[key] = value

            """
            {'YResolution': (72, 1), 'ResolutionUnit': 2, 'Copyright': u'', 'WhitePoint': ((313, 1000), (329, 1000)),
             'Make': u'Canon', 'Flash': 16, 'SceneCaptureType': 0, 'GPSInfo': {0: '\x02\x02\x00\x00'},
             'MeteringMode': 6, 'XResolution': (72, 1), 'ExposureBiasValue': (0, 1),
             'MakerNote': 'xxx',
             'FocalPlaneYResolution': (3168000, 597), 'WhiteBalance': 0, 'FNumber': (35, 10), 'CustomRendered': 0,
             'DateTimeOriginal': u'2015:07:22 07:43:50', 'Artist': u'', 'FocalLength': (18, 1),
             'PrimaryChromaticities': ((64, 100), (33, 100), (21, 100), (71, 100), (15, 100), (6, 100)),
             'ExposureMode': 0, 'ComponentsConfiguration': '\x01\x02\x03\x00', 'FocalPlaneXResolution': (4752000, 894),
             'ExifOffset': 484, 'ExifImageHeight': 3168, 'SubsecTimeDigitized': u'15', 'ISOSpeedRatings': 100,
             'Model': u'Canon EOS 50D', 'DateTime': u'2015:07:22 07:43:50', 'Gamma': (22, 10), 'ExposureTime': (1, 30),
             'FocalPlaneResolutionUnit': 2, 'SubsecTime': u'15', 'Orientation': 1, 'ExifInteroperabilityOffset': 8738,
             'SubsecTimeOriginal': u'15', 'FlashPixVersion': '0100', 'YCbCrPositioning': 2,
             'ShutterSpeedValue': (327680, 65536), 'ExifVersion': '0221'}
            """

            # 相机型号
            _model = exif.get('Model')
            # 拍摄日期
            _datetime = exif.get('DateTimeOriginal')[:10].replace(':', '-')

            # 曝光时间
            if exif.get('ExposureTime')[0] > exif.get('ExposureTime')[1]:
                # 曝光时间大于1秒
                _exposuretime = str(exif.get('ExposureTime')[0] * 1.0 / exif.get('ExposureTime')[1] * 1.0)
            else:
                _exposuretime = str(exif.get('ExposureTime')[0]) + "/" + str(exif.get('ExposureTime')[1])

            # ISO
            _iso = exif.get('ISOSpeedRatings')

            # 光圈值
            _fnumber = 1.0 * exif.get('FNumber')[0] / exif.get('FNumber')[1]

            # 写入信息
            from PIL import ImageFont
            # 使用Mac默认字体: /Library/Fonts/
            # Windows同学应该也可以自动取到字体
            font = ImageFont.truetype("华文黑体.ttf", 24)
            exif_info = "@%s  %s  F%s %s ISO%s   photo by zzhoo8" % (_datetime, _model, _fnumber, _exposuretime, _iso)
            draw = ImageDraw.Draw(thumb)
            # draw.text(xy=(40, yy-30), text=exif_info, fill=(255, 255, 255), font=font)
            # draw.text(xy=(40, yy - 30), text=exif_info, fill=(68, 68, 68), font=font)
            draw.text(xy=(40, yy - 30), text=exif_info, fill=(0, 0, 0), font=font)
        try:
            # 图片增强
            # raw = thumb.copy()
            enhance = ImageEnhance.Contrast(thumb)
            thumb = enhance.enhance(factor=samson.config.get('CONTRAST', 1.0))
            # enhance = ImageEnhance.Brightness(thumb)
            # thumb = enhance.enhance(factor=1.1)
            enhance = ImageEnhance.Sharpness(thumb)
            thumb = enhance.enhance(factor=samson.config.get('SHARPNESS', 1.0))

            out = out if out else "out.jpg"
            from samson import logger
            logger.info("thumb.save(%s, format='JPEG')", out)
            thumb.save(out, format='JPEG')
        except IOError, e:
            print e.message

        thumb.close()
