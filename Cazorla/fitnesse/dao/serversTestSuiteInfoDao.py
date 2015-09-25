# coding=utf-8
__author__ = 'KiddoMa'


import json
import logging
import os
import sys

#根据系统名称,获取系统的测试信息
def getServerTestSuiteInfoByName(data):
    name = data['server_name']
    infos = getServerTestSuiteInfos()
    for server in infos['servers']:
        if server['name'] == name:
            return server
    return {}

def getServerTestSuiteInfos():
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    try:
        fp = open('../data/server_test_info.json','r')
        s = json.load(fp)
        return s
    except Exception as e:
        logging.error(e)
    finally:
        fp.close()


if __name__ == '__main__':
    info = getServerTestSuiteInfos()
    print info
    print info['servers'][0]['name']
    data = {'server_name':'mgs'}
    print getServerTestSuiteInfoByName(data)