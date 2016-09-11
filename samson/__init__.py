# coding:utf-8

import sys

import logging
from logging import handlers

from samson.base.image import ImageItem
from samson.base.log import log

# 日志打印模块
logger = logging.getLogger('samson')
logger.setLevel(level=logging.INFO)
_debug_log_format = '%(asctime)s - %(levelname)s - %(filename)s:%(funcName)s:%(lineno)d:\n%(message)s'
_file_handler = logging.handlers.TimedRotatingFileHandler(filename='../../app/log/samson.log', when='midnight')
_file_handler.setFormatter(fmt=logging.Formatter(fmt=_debug_log_format))
logger.addHandler(hdlr=_file_handler)


class Samson(object):
    """

    """
    config = dict()

    def __init__(self):
        """
        初始化
        """
        pass

    @log
    def apply_config(self, config):
        """
        生效配置文件
        :param config:
        :return:
        """
        self.config = config.__dict__

    @log
    def thumbnails_for_post(self):
        """
        一键生成带边框和exif信息的缩略图
        :return:
        """
        _file = sys.argv[1] if len(sys.argv) > 1 else "/Users/zzhoo8/IMG_9588.JPG"
        image = ImageItem(path=_file)
        # image.image.show()
        image.thumbnails_for_post()


# 实例化
samson = Samson()
