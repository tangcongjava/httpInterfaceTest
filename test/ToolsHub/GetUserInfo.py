# coding:cp936
# __author__ = 'angustang'
from OCT.interface import  http
import  json
from test.Msg import  ClarificationBook
from test.Msg import  BaseMsg
from test.Msg import  GeneratePostMsg
from nose.tools import  *
import  random
# 1��2
# ����ר����������
# ����ʵ������
# ��������������
# ר��ת��
# ר����¼��Ŀ���
# ר����Ѽ�����
# ר��Ȩ���۱���
# ר����������
# ר��������̹�������
# ר���������ٷ���
# ����ר���������
# ר������
# ר������
# ר����Ч����
# ר����Ч���
# �ύ������������Ϣģ��
# �ύ��˵���Ϣģ�塣

class CRMPepole(object):
    '''
    Ŀǰ������д���Ļ�ȡһ���̶��ͻ��µķ����ˣ�������,����ͨ��random����������Ŀͻ���Ϣ��ȡ
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
        ��ȡ�ͻ�ID
        :return:
        '''
        rspBody = self.myhttp.post(postUrl=self.CustormURL,postData=postdata)#1383188
        customerList = json.loads(rspBody)["body"]["data"]["rows"]
        return  customerList
    def getBailorInfo(self):
        '''
        ��ȡί������Ϣ
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
        ��ȡ��������Ϣ
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
        ��ȡ����ϵ����Ϣ
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
        ��ȡ��������Ϣ
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
        ��ȡ���ͻ��������ˡ������ˡ�ί���˵���Ϣ����һ���ֵ������ȫ������
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
    assert_equal(json.loads(msg)["header"]["msg"],u'�����ɹ�')
    assert_equal(json.loads(msg)["body"]["data"]["success"],True)