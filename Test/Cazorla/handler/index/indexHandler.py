# coding=utf-8
__author__ = 'KiddoMa'

import tornado
import logging

class build(tornado.web.RequestHandler):
    def get(self):
        #获取所有的参数
        args = self.request.arguments
        for arg in args:
            logging.info(self.get_argument(arg))