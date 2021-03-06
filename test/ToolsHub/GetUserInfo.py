# coding:cp936
# __author__ = 'angustang'
from OCT.interface import  http
import  json
from test.Msg import  ClarificationBook
from test.Msg import  BaseMsg
from test.Msg import  GeneratePostMsg
from nose.tools import  *
import  random
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
    '''
    目前这里是写死的获取一个固定客户下的发明人，申请人,后续通过random来进行随机的客户信息读取
    '''
    def __init__(self,custormUrl,BailorUrl,ProposerUrl,ContactUrl,InventorUrl,httpHandler):
        self.CustormURL = custormUrl
        self.BailorURL = BailorUrl
        self.ProposeURL = ProposerUrl
        self.ContactURL = ContactUrl
        self.InventorURL = InventorUrl
        self.myhttp = httpHandler
        self.customerID = None
        pass
    def setCustomerID(self,customerID):
        self.customerID =customerID
    def getCustormInfo(self,postdata):
        '''
        获取客户ID
        :return:
        '''
        rspBody = self.myhttp.post(postUrl=self.CustormURL,postData=postdata)#1383188
        customerList = json.loads(rspBody)["body"]["data"]["rows"]
        return  customerList
    def getBailorInfo(self):
        '''
        获取委托人信息
        :return:
        '''
        rspBody = self.myhttp.post(postUrl=self.BailorURL,postData={
            "customerId":self.customerID
        })
        BailorList = json.loads(rspBody)["body"]["data"]
        bailorInfo = BailorList[random.randint(0,len(BailorList)-1)]
        return  bailorInfo
    def getProposerInfo(self):
        '''
        获取申请人信息
        :return:
        '''
        rspBody=self.myhttp.post(postUrl=self.ProposeURL,postData={
            "customerId":self.customerID
        })
        ProposerList = json.loads(rspBody)["body"]["data"]
        proposerInfo = ProposerList[random.randint(0,len(ProposerList)-1)]
        # print rspBody
        return  proposerInfo
    def getContactInfo(self,postData=None):
        '''
        获取到联系人信息
        :return:
        '''
        rspBody = self.myhttp.post(postUrl=self.ContactURL,postData={
            "customerId":self.customerID
        })
        ContactList = json.loads(rspBody)["body"]["data"]
        contactInfo = ContactList[random.randint(0,len(ContactList)-1)]
        return  contactInfo
    def getInventorInfo(self,postData=None):
        '''
        获取发明人信息
        :return:
        '''
        rspBody =  self.myhttp.post(postUrl=self.InventorURL,postData={
            "customerId":self.customerID
        })
        InventorList = json.loads(rspBody)["body"]["data"]["rows"]
        inventorInfo = inventorInfo = InventorList[random.randint(0,len(InventorList)-1)]
        return   inventorInfo
    def getAllRoleInfo(self):
        '''
        获取到客户、申请人、发明人、委托人的信息放在一个字典里进行全部返回
        :return:
        '''
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