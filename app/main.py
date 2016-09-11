# coding:utf-8

import os
import re

from config import Config
from samson import samson


if __name__ == '__main__':
    samson.apply_config(config=Config)
    # samson.thumbnails_for_post("/Users/zzhoo8/IMG_9524.JPG")

    path = "/Users/zzhoo8"
    parents = os.listdir(path)
    for parent in parents:
        child = os.path.join(path, parent)
        if re.match(pattern=r"(.*).JPG", string=child):
            samson.thumbnails_for_post(path=child)
