# coding:utf-8
# __author__ = 'angustang'
from OCT.interface import  http
import  json
from OCT.Msg import  ClarificationBook
from OCT.Msg import  BaseMsg
from OCT.Msg import  GeneratePostMsg
from nose.tools import  *
# 1打2
# 国内专利发明申请
# 国内实用新型
# 国内外观设计申请
# 专利转让
# 专利著录项目变更
# 专利年费监测缴纳
# 专利权评价报告
# 专利审查意见答复
# 专利审查流程公共服务
# 专利检索（官方）
# 发明专利优先审查
# 专利交易
# 专利复审
# 专利无效宣告
# 专利无效答辩
# 提交交底审核书的消息模板
# 提交审核的消息模板。

class CRMPepole(object):
    def __init__(self,custormUrl,BailorUrl,ProposerUrl,ContactUrl,InventorUrl,httpHandler):
        self.CustormURL = custormUrl
        self.BailorURL = BailorUrl
        self.ProposeURL = ProposerUrl
        self.ContactURL = ContactUrl
        self.InventorURL = InventorUrl
        self.myhttp = httpHandler
        pass
    def getCustormInfo(self,postdata):
        '''
        获取客户ID
        :return:
        '''
        customerInfo={}
        rspBody = self.myhttp.post(postUrl=self.CustormURL,postData=postdata)#1383188
        self.custormid =[]
        customerInfo = json.loads(rspBody)["body"]["data"]["rows"][3]
        return  customerInfo
    def getBailorInfo(self,postData):
        '''
        获取委托人信息
        :return:
        '''
        BailorDict={}
        rspBody = self.myhttp.post(postUrl=self.BailorURL,postData=postData)
        BailorDict = json.loads(rspBody)["body"]["data"][2]
        print rspBody #目前测试只返回一个11289的联系人
        return  BailorDict
    def getProposerInfo(self,postData=None):
        '''
        获取申请人信息
        :return:
        '''
        ProposerDict={}
        rspBody=self.myhttp.post(postUrl=self.ProposeURL,postData=postData)
        ProposerDict = json.loads(rspBody)["body"]["data"][2]#目前测试只取一个
        # print rspBody
        return  ProposerDict
        pass
    def getContactInfo(self,postData=None):
        '''
        获取到联系人信息
        :return:
        '''
        ContactDict={}
        rspBody = self.myhttp.post(postUrl=self.ContactURL,postData=postData)
        ContactDict = json.loads(rspBody)["body"]["data"][1]
        # print ContactDict
        return ContactDict
        print
    pass
    def getInventorInfo(self,postData=None):
        '''
        获取发明人信息
        :return:
        '''
        InventorDict={}
        rspBody =  self.myhttp.post(postUrl=self.InventorURL,postData=postData)
        InventorDict = json.loads(rspBody)["body"]["data"]["rows"][0]
        print InventorDict
        # print rspBody
        return  InventorDict
        pass
if __name__ == '__main__':
    httpHandler = http.MyHttp()
    crmInfoData = CRMPepole(custormUrl="http://patent.test.chofn.net/customer/index/",
                            BailorUrl="http://patent.test.chofn.net/Customer/bailorIndex/",
                            ProposerUrl="http://patent.test.chofn.net/Customer/proposerIndex/",
                            ContactUrl="http://patent.test.chofn.net/Customer/contactIndex/",
                            InventorUrl="http://patent.test.chofn.net/Customer/getInventorList",httpHandler=httpHandler)
    crmInfoData.myhttp.login("http://patent.test.chofn.net/index/index/",
                             {"username":"elva","password":"zz123asd"})
    customerInfo = crmInfoData.getCustormInfo(postdata={
        "page":1,
        "pageSize":15
    })
    BailorInfo = crmInfoData.getBailorInfo(postData={
        "customerId":1383188
    })
    ProposerInfo = ProposerInfo = crmInfoData.getProposerInfo(postData={
        "customerId":1383188})
    ContactInfo = ContactInfo = crmInfoData.getContactInfo(postData={
        "customerId":1383188
    })
    InventorInfo = crmInfoData.getInventorInfo(postData={
        "customerId":1383188
    })
    genData = GeneratePostMsg.GenData(ClarificationBook.ClarificationBookUpload,BaseMsg.itemsAndFee)
    returndata = genData.genJsonData(bizType=0,customerInfo=customerInfo,bailorInfo=BailorInfo,
                        poroposerInfo=ProposerInfo,contactInfo=ContactInfo,
                        inventorInfo=InventorInfo)

    # print json.dumps(returndata)
    ###############################
    msg = crmInfoData.myhttp.post("http://patent.test.chofn.net/clarificaitonbookcheck/add/",returndata,{"Content-Type":
                                                                                           "application/x-www-form-urlencoded;charset=UTF-8"},postFile=False,postJson=True)
    print msg
    assert_equal(json.loads(msg)["header"]["msg"],u'操作成功')
    assert_equal(json.loads(msg)["body"]["data"]["success"],True)