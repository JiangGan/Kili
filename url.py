# coding=utf-8
__author__ = 'KiddoMa'

#定义URL的映射

import sys

from Test.Cazorla.handler.index.indexHandler import *


reload(sys)

url = [
    (r'/Cazorla/build', index),
]