#coding=utf-8
'''登录接口测试用例集'''

from OCT.ToolsHub.decorators import getData
from OCT.interface.http import MyHttp
from test.OCTcfg import URL_PATENT_BASE
import json
import nose
from nose.tools import  *
from  OCT.ToolsHub import  myLog
__author__ = 'wanel.zhang'

#登录接口链接地址
url_login = URL_PATENT_BASE+"/index/index/"

#登出接口链接地址
url_logout = URL_PATENT_BASE+"/index/logout/"

log = myLog.MyLogging(__file__)
myhttp = MyHttp()
def login(username, password,myhttp = MyHttp()):
    ''' 登录
    '''
    requestData={}
    requestData["username"] = username
    requestData["password"] = password
#     print logindata

    resp = myhttp.login(url_login, requestData)
    print "登录请求返回结果为： ", resp.decode("unicode_escape")
    return json.loads(resp)

def logout(myhttp):
    ''' 登出
    '''
    myhttp.logout(url_logout)
    
# @dataprovider
def loginNormalCase(caseid, caseDesc, username, password):
    ''' 正常登录
    '''
    print '\n接收到的参数为： caseid=%s, caseDesc=%s, username=%s, password=%s' \
    % (caseid, caseDesc, username, password)
    try:
        resp = login(username, password, myhttp)
        assert resp["header"]["code"] == 104
        assert resp["body"]["status"] == 1
    finally:
        logout(myhttp)

# @dataprovider 
def loginErrorCase(caseid, caseDesc, username, password,statusInBody,descInBody):
    ''' 使用错误信息登录
    '''
    log.debug('\n接收到的参数为： caseid=%s, caseDesc=%s, username=%s, password=%s, \
     statusInBody=%s, descInBody=%s' % (caseid, caseDesc, username, password, \
                                        statusInBody,descInBody))
    # print '\n接收到的参数为： caseid=%s, caseDesc=%s, username=%s, password=%s, \
    #  statusInBody=%s, descInBody=%s' % (caseid, caseDesc, username, password, \
    #                                     statusInBody,descInBody)
    try:
        resp = login(username, password,myhttp)
    #     print type(json.loads(resp)["body"]["status"]),type(statusInBody)
    #     print type(json.loads(resp)["body"]["desc"]),type(descInBody.decode("utf-8"))
    #     print json.loads(resp)["body"]["desc"], descInBody.decode("utf-8")
    
        assert resp["header"]["code"] == 104
        assert resp["body"]["status"] == int(statusInBody)
        assert resp["body"]["desc"] == descInBody.decode("utf-8")
    finally:
        logout(myhttp)

def test_NormalLogin():
    ''' 使用resource中数据测试正常登录
    '''
    for data in getData(loginNormalCase):
        data.insert(0,loginNormalCase)
        yield tuple(data)

def test_errorLogin():
    '''  使用resource中数据测试错误信息登录
    '''
    for data in getData(loginErrorCase):
        data.insert(0,loginErrorCase)
        yield tuple(data)
        
if __name__ == "__main__":
    noseArg=['-v','-s',__file__,'--with-html','--html-file=output.html']
    assert nose.run(argv=noseArg)


