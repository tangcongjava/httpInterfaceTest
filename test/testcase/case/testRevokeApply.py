#coding=utf-8
'''撤案申请测试用例集'''
import sys
print sys.path

from test.OCTcfg import URL_PATENT_BASE,ERROR_PATENT_NOT_LOGIN,consultant
from OCT.interface.http import MyHttp
import json,nose
from OCT.ToolsHub.decorators import getData
from test.testcase.utils import setup_login, teardown_logout
from nose.tools import with_setup

__author__="waynel.zhang"

#撤案申请接口链接地址
url_revoke_apply = URL_PATENT_BASE+"/Case/revokeApply/"

myhttp = MyHttp()

def invokeApply(ajid,nextHandlerId,feeCate,fee,suppleAttachment,myhttp=MyHttp()):
    ''' 撤案申请
    '''
    requestData={}
    if ajid:
        requestData["id"] = ajid
    if nextHandlerId:
        requestData["nextHandlerId"] = nextHandlerId
    if feeCate:
        requestData["feeCate"] = feeCate
    if fee:
        requestData["fee"] = fee
    if suppleAttachment:
        requestData["suppleAttachment"] = suppleAttachment
        
    resp = myhttp.post(url_revoke_apply, requestData)
    print "撤案申请请求返回结果为： ", resp.decode("unicode_escape")
    return json.loads(resp)

@with_setup(setup_login(consultant.get("username"),consultant.get("password"),myhttp),teardown_logout(myhttp))
def apply_with_error_info(caseId, caseDesc,ajid,nextHandlerId,feeCate,fee,suppleAttachment, statusInBody, descInBody):
    ''' 使用错误信息进行撤案
    ''' 
    print '\n接收到的参数为： caseid=%s, caseDesc=%s, ajid=%s,  nextHandlerId=%s, feeCate=%s, fee=%s, \
    suppleAttachment=%s, statusInBody=%s, descInBody=%s' \
    % (caseId, caseDesc, ajid, nextHandlerId, feeCate, fee, suppleAttachment, statusInBody, descInBody)     

    resp = invokeApply(ajid, nextHandlerId, feeCate, fee, suppleAttachment, myhttp)
    
    assert resp["header"]["code"] == 104
    assert resp["body"]["status"] == int(statusInBody)
    assert resp["body"]["desc"] == descInBody.decode("utf-8")

     
def test_pay_without_login():
    ''' 测试未登录时进行撤案
    ''' 
    resp = invokeApply(3,2,1,1,None)
        
    assert resp["header"]["code"] == 102
    assert resp["body"]["status"] == 0
    assert resp["body"]["desc"] == ERROR_PATENT_NOT_LOGIN.decode("utf-8")
  
def test_pay_with_error_info():
    ''' 使用resource中数据测试使用错误信息进行撤案
    ''' 
    for data in getData(apply_with_error_info):
        data.insert(0,apply_with_error_info)
        yield tuple(data)

if __name__  == "__main__":
    noseArg=['-v','-s',__file__,'--with-html','--html-file=output.html']
    assert nose.run(argv=noseArg)