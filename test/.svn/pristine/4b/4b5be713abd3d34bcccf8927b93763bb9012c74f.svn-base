#coding=utf-8
'''客户信息接口测试用例集'''

from OCT.ToolsHub.decorators import getData
from OCT.interface.http import MyHttp
from test.OCTcfg import URL_PATENT_BASE,consultant
import json
from nose.tools import with_setup
from test.testcase.utils import setup_login, teardown_logout
from test.testcase.login.TestLogin import login
from test.ToolsHub.checkUtils import basicSuccessCheck
from test.ToolsHub.convertUtils import *

__author__ = 'wanel.zhang'
#客户列表接口链接
url_customer_list = URL_PATENT_BASE+"/Customer/index/"

#委托人列表接口链接
url_bailor_list = URL_PATENT_BASE+"/Customer/bailorIndex/"

#根据委托人id获取联系人列表接口链接
url_contact_list_by_bailorId = URL_PATENT_BASE+"/Customer/contact/"

#根据客户id获取联系人列表接口链接
url_contact_list_by_customerId = URL_PATENT_BASE+"/Customer/contactIndex/"

#根据客户id获取联系人列表接口链接
url_contact_detail = URL_PATENT_BASE+"/Customer/contactDetail/"

#申请人列表接口链接
url_proposer_list = URL_PATENT_BASE+"/Customer/proposerIndex/"

#发明人列表接口链接
url_inventor_list = URL_PATENT_BASE+"/Customer/getInventorList"

#发明人信息接口链接
url_inventor_info = URL_PATENT_BASE+"/Customer/getInventorInfo"

myhttp = MyHttp()

def customerIndex(page, pageSize,customerName,consultantName,myhttp = MyHttp()):
    ''' 获取客户列表
    '''
    requestData={}
    if page:
        requestData["page"] =page 
    if pageSize:
        requestData["pageSize"] =pageSize 
    if customerName:
        requestData["customerName"] =customerName 
    if consultantName:
        requestData["consultantName"] =consultantName 
        
    resp =  myhttp.post(url_customer_list, requestData)
    print "获取客户列表请求的返回结果是： ", resp.decode("unicode-escape")
    return json.loads(resp)

def customerBailorIndex(customerId,myhttp = MyHttp()):
    ''' 获取委托人列表
    '''
    requestData={}
    if customerId:
        requestData["customerId"] =customerId 
        
    resp = myhttp.post(url_bailor_list, requestData)
    print "获取委托人列表请求的返回结果是： ", resp.decode("unicode-escape")
    return json.loads(resp)

def customerContact(bailorId,myhttp = MyHttp()):
    ''' 根据委托人id获取联系人列表
    '''
    requestData={}
    if bailorId:
        requestData["bailorId"] =bailorId 
        
    resp = myhttp.post(url_contact_list_by_bailorId, requestData)
    print "根据委托人id获取联系人列表请求的返回结果是： ", resp.decode("unicode-escape")
    return json.loads(resp)

def customerContactIndex(customerId,myhttp = MyHttp()):
    ''' 根据客户id获取联系人列表
    '''
    requestData={}
    if customerId:
        requestData["customerId"] =customerId 
        
    resp = myhttp.post(url_contact_list_by_customerId, requestData)
    print "根据客户id获取联系人列表请求的返回结果是： ", resp.decode("unicode-escape")
    return json.loads(resp)

def customerContactDetail(contactId,myhttp = MyHttp()):
    ''' 获取联系人详情
    '''
    requestData={}
    if contactId:
        requestData["contactId"] =contactId 
        
    resp = myhttp.post(url_contact_detail, requestData)
    print "获取联系人详情请求的返回结果是： ", resp.decode("unicode-escape")
    return json.loads(resp)

def customerProposerIndex(customerId,myhttp = MyHttp()):
    ''' 获取申请人列表
    '''
    requestData={}
    if customerId:
        requestData["customerId"] =customerId 
        
    resp = myhttp.post(url_proposer_list, requestData)
    print "获取申请人列表请求的返回结果是： ", resp.decode("unicode-escape")
    return json.loads(resp)

def customerGetInventorList(customerId,myhttp = MyHttp()):
    ''' 获取发明人列表
    '''
    requestData={}
    if customerId:
        requestData["customerId"] =customerId 
        
    resp = myhttp.post(url_inventor_list, requestData)
    print "获取发明人列表请求的返回结果是： ", resp.decode("unicode-escape")
    return json.loads(resp)

def customerGetInventorInfo(inventorId,myhttp = MyHttp()):
    ''' 获取发明人详情
    '''
    requestData={}
    if inventorId:
        requestData["inventorId"] =inventorId 
        
    resp = myhttp.post(url_inventor_info, requestData)
    print "获取发明人详情请求的返回结果是： ", resp.decode("unicode-escape")
    return json.loads(resp)

def getCustomerList(page, pageSize,customerName,consultantName,myhttp = MyHttp()):
    ''' 获取客户列表-使用正确的数据并做简单校验
    '''       
    resp =  customerIndex(page, pageSize,customerName,consultantName,myhttp)  
    
    #校验返回结果
    basicSuccessCheck(resp)   
    return resp["body"]["data"]["rows"]

def getBailorList(customerId,myhttp = MyHttp()):
    ''' 获取委托人列表-使用正确的数据并做简单校验
    '''
    resp = customerBailorIndex(customerId,myhttp)
    
    #校验返回结果
    basicSuccessCheck(resp)   
    return resp["body"]["data"]

def getContactListByBailorId(bailorId,myhttp = MyHttp()):
    ''' 根据委托人id获取联系人列表-使用正确的数据并做简单校验
    '''
    resp = customerContact(bailorId,myhttp)
    
    #校验返回结果
    basicSuccessCheck(resp)    
    return resp["body"]["data"]

def getContactListByCustomerId(customerId,myhttp = MyHttp()):
    ''' 根据客户id获取联系人列表-使用正确的数据并做简单校验
    '''
    resp = customerContactIndex(customerId,myhttp)
    
    #校验返回结果
    basicSuccessCheck(resp)    
    return resp["body"]["data"]

def getContactDetail(contactId,myhttp = MyHttp()):
    ''' 获取联系人详情-使用正确的数据并做简单校验
    '''
    resp = customerContactDetail(customerId,myhttp)
    
    #校验返回结果
    basicSuccessCheck(resp)   
    return resp["body"]["data"]

def getProposerList(customerId,myhttp = MyHttp()):
    ''' 获取申请人列表-使用正确的数据并做简单校验
    '''
    resp = customerProposerIndex(customerId,myhttp)
    
    #校验返回结果
    basicSuccessCheck(resp)
    return convertToProposerList(resp)

def getInventorList(customerId,myhttp = MyHttp()):
    ''' 获取发明人列表-使用正确的数据并做简单校验
    '''    
    resp = customerGetInventorList(customerId,myhttp)
    #校验返回结果
    basicSuccessCheck(resp)
    return convertToInventorList(resp)

def getInventorInfo(inventorId,myhttp = MyHttp()):
    ''' 获取发明人详情-使用正确的数据并做简单校验
    '''    
    resp = customerGetInventorInfo(inventorId,myhttp)
    
    #校验返回结果
    basicSuccessCheck(resp)
    return resp["body"]["data"]

if __name__ == "__main__":
    login(consultant.get("username"),consultant.get("password"),myhttp)
    resp = getCustomerList(1, 10, "华润湖南医药有限公司", "cyan", myhttp)
    print resp
    customerId = resp[0]["id"]
    print customerId
    resp = getBailorList(customerId, myhttp)
#     print resp
    bailorId = resp[0]["bailorId"]
#     print bailorId
    print getContactListByBailorId(bailorId, myhttp)
    print getContactListByCustomerId(customerId, myhttp)
#     print getProposerList(customerId, myhttp)

#     print getBailorList(customerId, myhttp)
#     print getInventorList(customerId, myhttp)