#coding=utf-8
'''余额支付测试用例集'''

from test.OCTcfg import URL_PATENT_BASE,ERROR_PATENT_NOT_LOGIN,consultant
from OCT.interface.http import MyHttp
import json,nose
from OCT.ToolsHub.decorators import getData
from test.testcase.utils import setup_login, teardown_logout
from nose.tools import with_setup

__author__="waynel.zhang"

#余额支付接口链接地址
url_balance_pay = URL_PATENT_BASE+"/PayCase/payFromBalance/"

myhttp = MyHttp()

def pay(ids,myhttp=MyHttp()):
    ''' 余额支付
    '''
    requestData={}
    if ids:
        requestData["ids"] = ids
        
    resp = myhttp.post(url_balance_pay, requestData)   
    print "余额支付请求返回结果为： ", resp.decode("unicode_escape")    
    return json.loads(resp)

@with_setup(setup_login(consultant.get("username"),consultant.get("password"),myhttp),teardown_logout(myhttp))
def pay_with_error_ids(caseId, caseDesc,ids,descInBody):
    ''' 对错误的id进行支付
    '''    
    print '\n接收到的参数为： caseid=%s, caseDesc=%s, ids=%s, descInBody=%s' \
    % (caseId, caseDesc, ids, descInBody)     

    resp = pay(ids,myhttp)
    
    assert resp["header"]["code"] == 104
    assert resp["body"]["status"] == 0
    assert resp["body"]["desc"] == descInBody.decode("utf-8")

     
def test_pay_without_login():
    ''' 测试未登录的时候进行支付
    '''
    resp = pay("40")
    
    assert resp["header"]["code"] == 102
    assert resp["body"]["status"] == 0
    assert resp["body"]["desc"] == ERROR_PATENT_NOT_LOGIN.decode("utf-8")
  
def test_pay_with_error_ids():
    ''' 使用resource中数据测试对错误的id进行支付
    '''    
    for data in getData(pay_with_error_ids):
        data.insert(0,pay_with_error_ids)
        yield tuple(data)

if __name__  == "__main__":
    noseArg=['-v','-s',__file__,'--with-html','--html-file=output.html']
    assert nose.run(argv=noseArg)

