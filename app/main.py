# coding:utf-8

from config import Config
from samson import samson


if __name__ == '__main__':
    samson.apply_config(config=Config)
    samson.thumbnails_for_post()
