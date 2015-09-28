# coding=utf-8
__author__ = 'KiddoMa'

import httplib2

def runTestSuiteByTags(data):
    uri = buildUrl(data)
    print uri
    h = httplib2.Http(timeout=5)
    h.request(uri,method="GET")
    print '请求完成'


def buildUrl(data):
    uri = 'http://'+data['fitnesse_url']+':'+data['fitnesse_port']+'/'+data['testsuite_url']+'?suite&suiteFilter='
    for tag in data['testsuite_tags']:
        uri = uri + tag + ','
    uri = uri[0:-1]
    return uri



