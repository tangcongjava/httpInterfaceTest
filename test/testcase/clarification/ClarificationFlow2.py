# coding:utf-8
__author__ = 'angustang'
from  OCT.interface import  http
from  test.Msg import  submitContract
from  test.Msg import  GeneratePostMsg
from test.Msg import  BaseMsg
from  OCT.ToolsHub import  GetUserInfo,GenDatetime
import  json
from  test.Msg import  ClarificationBook,SignContract
from nose.tools import  *
class testClarificationFlow(object):
    contractId = None#合同ID
    clfBookId = None
    myhttp = http.MyHttp()
    crm = GetUserInfo.CRMPepole(custormUrl="http://patent.test.chofn.net/customer/index/",
                            BailorUrl="http://patent.test.chofn.net/Customer/bailorIndex/",
                            ProposerUrl="http://patent.test.chofn.net/Customer/proposerIndex/",
                            ContactUrl="http://patent.test.chofn.net/Customer/contactIndex/",
                            InventorUrl="http://patent.test.chofn.net/Customer/getInventorList",
                            httpHandler=myhttp)
    @classmethod
    def setup_class(cls):
        #登录并获取客户的信息,生成合同新建消息
        cls.crm.myhttp.login("http://patent.test.chofn.net/index/index/",{"username":"elva","password":"zz123asd"})
        customerInfo = cls.crm.getCustormInfo(postdata={
            "page":1,
            "pageSize":15
        })
        BailorInfo = cls.crm.getBailorInfo(postData={
            "customerId":1383188
        })
        ProposerInfo = ProposerInfo = cls.crm.getProposerInfo(postData={
            "customerId":1383188})
        ContactInfo = ContactInfo = cls.crm.getContactInfo(postData={
            "customerId":1383188
        })
        InventorInfo = cls.crm.getInventorInfo(postData={
            "customerId":1383188
        })
        genData = GeneratePostMsg.GenData(submitContract.submitContractWithoutClarificationMsg,BaseMsg.itemsAndFeeWithoutClarification)
        # genData = GeneratePostMsg.GenData(submitContract.test)
        cls.contracSubmitdata = genData.genJsonData(bizType=100,customerInfo=customerInfo,bailorInfo=BailorInfo,
                                     poroposerInfo=ProposerInfo,contactInfo=ContactInfo,
                                     inventorInfo=InventorInfo)

    def test_a_SumbitContract(self):
        rspMsg = self.myhttp.post("http://patent.test.chofn.net/Contract/submit/",postData=self.contracSubmitdata,postJson=True)
        testClarificationFlow.contractId = json.loads(rspMsg)["body"]["data"]["contractId"]
        print rspMsg
        pass
    def test_b_ClarificationEdit(self):
        #一个contract可能对应多个item
        contractDetailMsg = self.myhttp.post("http://patent.test.chofn.net/Contract/detail/",
            {"id":self.contractId})
        #获取到detailID
        itemDetailId = json.loads(contractDetailMsg)["body"]["data"]["itemFinance"]["items"][0]["detailId"]
        itemDetailMsg =  self.myhttp.post("http://patent.test.chofn.net/contract/itemDetail/"+"?id="+itemDetailId,
            postData=None
        )
        testClarificationFlow.clfBookId = json.loads(itemDetailMsg)["body"]["data"]["clarificaitonbook"]["id"]
        print "\nclfbookid is " +testClarificationFlow.clfBookId
        srcClfEditMsg = {
            "id":testClarificationFlow.clfBookId,
            "name":u'接口测试'+GenDatetime.TimeHandler().getCurrentTime()
        }
        genData = GeneratePostMsg.GenData(ClarificationBook.ClarificationBookEdit)
        clfEditMsg = genData.genJsonData(bizType=7,customerInfo=None,inventorInfo=None,bailorInfo=None,
                                         poroposerInfo=None,contactInfo=None,clfEditMsg=srcClfEditMsg)
        rspMsg = self.myhttp.post("http://patent.test.chofn.net/clarificaitonbookcheck/edit/",postData=clfEditMsg,
                                  postJson=True)
        # print rspMsg
        pass
    def test_c_submitToLeader(self):
        #提交给交底书上级领导
        self.myhttp.logout("http://patent.test.chofn.net/index/logout/")
        self.myhttp.login("http://patent.test.chofn.net/index/index",{
            "username":"ida",
            "password":"zz123asd"
        })
        submitToLeaderMsg = {
            "remark":"",
            "result":2,
            "id":self.clfBookId
        }
        rspMsg = self.myhttp.post("http://patent.test.chofn.net/ClarificaitonbookCheck/check/",postData=submitToLeaderMsg)
        pass
    def test_d_ManagerCheck(self):
        #切换至交底审核员，然后进行数据审核
        self.myhttp.logout("http://patent.test.chofn.net/index/logout/")
        self.myhttp.login("http://patent.test.chofn.net/index/index",{
            "username":"Rambo",
            "password":"zz123asd"
        })
        srcClfManagerCheckMsg={
            "id":self.clfBookId,
            "result":1,#1代表通过，2代有不通过
            "remark":"回复信息"
        }
        rspMsg = self.myhttp.post("http://patent.test.chofn.net/clarificaitonbookcheck/reply/",postData=srcClfManagerCheckMsg,
                                  )
        print rspMsg
        pass
    def test_e_clfCheck(self):
        self.myhttp.logout("http://patent.test.chofn.net/index/logout")
        self.myhttp.login("http://patent.test.chofn.net/index/index",{
            "username":"ida",
            "password":"zz123asd"
        })
        clfBookCheckMsg={
            "remark":"交底审核通过",
            "result":1,
            "id":self.clfBookId
        }
        rspMsg = self.myhttp.post("http://patent.test.chofn.net/ClarificaitonbookCheck/check/",postData=clfBookCheckMsg)

    def test_f_contractSign(self):
        #非标合同签订
        self.myhttp.logout("http://patent.test.chofn.net/index/logout")
        self.myhttp.login("http://patent.test.chofn.net/index/index",
            {
                "username":"elva",
                "password":"zz123asd"
            })
        finalNoStandardCheckMsg={
            "contractId":self.contractId,
        }
        dataGener = GeneratePostMsg.GenData(SignContract.FinalNoStandarCheckMsg)
        postMsg = dataGener.genJsonData(bizType=5,customerInfo=None,poroposerInfo=None,
                                        contactInfo=None,inventorInfo=None,bailorInfo=None,
                                        FinalNoStandardCheckMsg=finalNoStandardCheckMsg)
        rspmsg = self.myhttp.post("http://patent.test.chofn.net/SignContract/sign/",postData=postMsg,postJson=True)

        pass
