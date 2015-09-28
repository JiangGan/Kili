# coding=utf-8
__author__ = 'KiddoMa'

from Cazorla.fitnesse.dao import serversTestSuiteInfoDao
from Cazorla.fitnesse.dao import fitnesseInfoDao
from Cazorla.fitnesse.service import testSuiteService


def invockTestSuite(data):
    test_info = getServerTestSuiteInfo(data)
    fitnesse_info = getFitnesseInfo(data)
    runTestSuiteByTags(test_info, fitnesse_info)

    ##############################
    #获取该系统的配置的相关信息
    #包括
    #1.测试集的地址
    #2.测试集配置的tag
    #获取测试系统的信息,包括 URL,系统名称,tags
    #传入数据类型是字典,其中需要包括 key=server_name,表示需要获取那个系统的测试用例信息


def getServerTestSuiteInfo(data):
    return serversTestSuiteInfoDao.getServerTestSuiteInfoByName(data)


    ##############################
    #获取Fitnesse服务器的相关信息
    #包括 服务器ip地址,端口
    #传入数据类型是字典,其中需要包括 key=fitnesse_server_name,表示需要获取哪个事业部的fitnesse服务器信息


def getFitnesseInfo(data):
    return fitnesseInfoDao.getFitnesseInfoByName(data)

    ##############################
    #通过测试集信息和fitnesse服务器信息,运行测试用例


def runTestSuiteByTags(test_info, fitnesse_info):
    data = {}
    data['fitnesse_url'] = fitnesse_info['ip']
    data['fitnesse_port'] = fitnesse_info['port']
    data['testsuite_url'] = test_info['url']
    data['testsuite_tags'] = test_info['tags']
    testSuiteService.runTestSuiteByTags(data)


    #提供给定时task调用的方法.
    #测试结果文件路径地址
    #/Users/mayunfei/Documents/FitNesseRoot/files/testResults/FrontPage.SoapInterfaceTest.SoapTest.TestCase
def getTestSuiteResultFileByServerName(data):
    server_name = data['server_name']
    testsuite_url = data['testsuite_url']
    build_time = data['build_time']
    result_file_path = data['result_file_path']



if __name__ == '__main__':
    data = {'server_name': 'soap', 'fitnesse_server_name': 'zfjs'}
    # print getServerTestSuiteInfo(data)
    # print getFitnesseInfo(data)
    invockTestSuite(data)