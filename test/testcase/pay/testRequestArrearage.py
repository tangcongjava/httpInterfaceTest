#coding=utf-8
'''欠款上报申请测试用例集'''

from test.OCTcfg import URL_PATENT_BASE,ERROR_PATENT_NOT_LOGIN,consultant
from OCT.interface.http import MyHttp
import json,nose
from OCT.ToolsHub.decorators import getData
from test.testcase.utils import setup_login, teardown_logout
from nose.tools import with_setup
from random import randint

__author__="waynel.zhang"

#欠款上报申请接口链接地址
url_request_arrearage = URL_PATENT_BASE+"/PayCase/requestArrearage/"

myhttp = MyHttp()
ERROR_UNKNOWN_IDS = "付款信息数据ID串格式校验失败"

def requestArrearage(ids,nextHandlerId,accountPeriod,myhttp=MyHttp()):
    ''' 欠款上报请求
    '''    
    requestData={}
    if ids:
        requestData["ids"] = ids
    if nextHandlerId:
        requestData["nextHandlerId"] = nextHandlerId
    if accountPeriod:
        requestData["accountPeriod"] = accountPeriod
        
    resp = myhttp.post(url_request_arrearage, requestData)
    print "欠款上报请求返回结果为： ", resp.decode("unicode_escape")    
    return json.loads(resp)

@with_setup(setup_login(consultant.get("username"),consultant.get("password"),myhttp),teardown_logout(myhttp))
def request_with_error_info(caseId, caseDesc,ids,nextHandlerId,accountPeriod,descInBody):
    ''' 使用错误信息进行欠款上报
    '''    
    if accountPeriod:
        accountPeriod = randint(1,6)
    print '\n接收到的参数为： caseid=%s, caseDesc=%s, ids=%s, nextHandlerId=%s, accountPeriod=%s,\
    descInBody=%s' % (caseId, caseDesc, ids,nextHandlerId,accountPeriod,descInBody)     

    resp = requestArrearage(ids,nextHandlerId,accountPeriod,myhttp)
    
    assert resp["header"]["code"] == 104
    assert resp["body"]["status"] == 0
    assert resp["body"]["desc"] == descInBody.decode("utf-8")

     
def test_request_without_login():
    ''' 测试未登录时进行欠款上报
    '''    
    resp = requestArrearage([20],"2222","6")
    
    assert resp["header"]["code"] == 102
    assert resp["body"]["status"] == 0
    assert resp["body"]["desc"] == ERROR_PATENT_NOT_LOGIN.decode("utf-8")
  
def test_request_with_error_info():
    ''' 使用resource中数据测试使用错误信息进行欠款上报
    '''    
    for data in getData(request_with_error_info):
        data.insert(0,request_with_error_info)
        yield tuple(data)

if __name__  == "__main__":
    noseArg=['-v','-s',__file__,'--with-html','--html-file=output.html']
    assert nose.run(argv=noseArg)