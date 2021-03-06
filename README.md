# 参孙

> 参孙（英文：Samson）是圣经士师记中的一位犹太人士师，生于前11世纪的以色列，玛挪亚的儿子。参孙以藉著上帝所赐极大的力气，徒手击杀雄狮并只身与以色列的外敌非利士人争战周旋而著名。

## todo

* 参数使用配置文件导入
* 加入图片优化和图片增强功能，例如锐化等
* 更多的边框和文字模板选择
* 代码更健壮
* 考虑是不是做成web服务^_^

## 功能

### 2016-09-11

* 优化数码照片边框，字体缩小到24px，颜色采用网页安全色灰白色系
* 支持命令行输入一个图片文件路径`python main.py /tmp/xxx.jpg`，但是输出还是写死在代码里- -b，需要下次改好
* 支持批量处理图片

### 2016-09-04

* 实现数码照片按比例缩小，以高度800px为基准
* 实现数码照片添加EXIF文字的边框

## 安装

* 下载samson代码库
* 创建python虚拟环境`pip install virtualenv && virtualenv venv`
* 激活虚拟环境`source venv/bin/activate`
* 程序打包`python setup.py sdist`（因为程序中写死了输入和输出的路径，以及一些参数，所以需要用IDE打开运行）
* 安装程序以及对应的依赖`pip install -r app/requirements.txt dist/*.tar.gz`
* 写例子运行, Have fun!

```python
# coding:utf-8

from config import Config
from samson import samson


if __name__ == '__main__':
    samson.apply_config(config=Config)
    samson.thumbnails_for_post()

```

