# coding=utf-8
__author__ = 'KiddoMa'

import os
import logging
import json

def getFitnesseInfoByName(data):
    fitness_server_name = data['fitnesse_server_name']
    infos = getFitnesseInfo()
    for info in infos['servers']:
        if info['name'] == fitness_server_name:
            return info
    return {}


def getFitnesseInfo():
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    try:
        fp = open('../data/fitnesse_servers_info.json','r')
        s = json.load(fp)
        return s
    except Exception as e:
        logging.error(e)
    finally:
        fp.close()



if __name__ == '__main__':
    data = {'fitnesse_server_name':'zfjs'}
    print getFitnesseInfoByName(data)