# coding:utf-8
__author__ = 'angustang'
from test.ToolsHub import  GetUserInfo
from OCT.interface import  http
from  test.Msg import  GeneratePostMsg
from  test.Msg import  ClarificationBook
from  test.Msg import  submitContract
from  test.Msg import   SignContract
from  test.Msg import  BaseMsg
from  test.Msg import  nonStandardContrackCheck
import json
from  test.OCTcfg import  consultant,DBcfg
from  test.Msg import  SignContract
import  nose,time
from  nose.tools import  *
from  OCT.ToolsHub import  myLog
import  test.OCTcfg
import  unittest
from test.ToolsHub import  urls
from  OCT.DB.mysqlHandler import sqlCheck
loginUrl = test.OCTcfg.URL_PATENT_BASE + "/index/index"
logoutUrl = test.OCTcfg.URL_PATENT_BASE + "/index/logout"

#合同流程的接口测试
class TestContractFlow(unittest.TestCase):
    contractId =0
    myhttp = http.MyHttp()
    custormerID = None
    log = myLog.MyLogging()
    print urls.custormUrl
    crm = GetUserInfo.CRMPepole(custormUrl=urls.custormUrl,
                            BailorUrl=urls.bailorUrl,
                            ProposerUrl=urls.proposerUrl,
                            ContactUrl=urls.contactUrl,
                            InventorUrl=urls.inventorUrl,
                            httpHandler=myhttp)
    custormerInfo = None
    bailorInfo = None
    proposerInfo = None
    contactInfo = None
    inventorInfo = None
    @classmethod
    def setup_class(cls):
        #登录并获取客户的信息
        cls.crm.myhttp.login(urls.loginUrl,
                             {"username":consultant.get("username"),"password":consultant.get("password")})
        #获取客户信息,然后随机选择一个
        customerList= cls.crm.getCustormInfo(postdata={
            "page":1,
            "pageSize":15
        })
        customerInfo=None
        for item in customerList:#item代表的是一个客户信息
            if item["name"].find(unicode(consultant["customerName"],"utf-8")) != -1:
                cls.crm.setCustomerID(item["id"])
                customerInfo=item
                TestContractFlow.custormerID = item["id"]
            else:
                continue
        if not TestContractFlow.custormerID:
            raise  Exception("the customer is not vaild,pls check the config")#顾问门下没有对应的客户

        bailorInfo = cls.crm.getBailorInfo()
        cls.log.debug(u"委托人信息")
        cls.log.debug(bailorInfo)

        proposerInfo = cls.crm.getProposerInfo()
        cls.log.debug(u"申请人信息")
        cls.log.debug(proposerInfo)
        contactInfo = cls.crm.getContactInfo()
        cls.log.debug(u"联系人信息")
        cls.log.debug(contactInfo)
        inventorInfo = cls.crm.getInventorInfo()
        cls.log.debug(u'发明人信息')
        cls.log.debug(inventorInfo)
        # print BailorInfo
        genData = GeneratePostMsg.GenData(submitContract.submitContractWithoutClarificationMsg,BaseMsg.itemsAndFeeWithoutClarification)
        cls.contractSubmitMsg = genData.genJsonData(bizType=6,customerInfo=customerInfo,bailorInfo=bailorInfo,
                                     poroposerInfo=proposerInfo,contactInfo=contactInfo,
                                     inventorInfo=inventorInfo)#直接传入一个大的客户信息字典
        TestContractFlow.custormerInfo = customerInfo
        TestContractFlow.bailorInfo = bailorInfo
        TestContractFlow.proposerInfo = proposerInfo
        TestContractFlow.contactInfo = contactInfo
        TestContractFlow.inventorInfo = inventorInfo
        pass
    @classmethod
    def teardown_class(cls):
        # logout
        cls.myhttp.logout(urls.logoutUrl)
        pass
    def setUp(self):
        #创建数据库链接,将conn置为全局变量
        global  dbconn
        dbconn = sqlCheck(host=DBcfg.get("host"),user=DBcfg.get("username"),pswd=DBcfg.get("password"),
                 port=DBcfg.get("port"),dbname=DBcfg.get("dbname"))
        pass
    def tearDown(self):
        #关闭数据库链接
        dbconn.clear()
        pass
    def test_A_ContractSubmit(self):
        #提交合同
        print 'begin to submit contract提交合同'

        msg = self.myhttp.post(urls.contractSubmitUrl,self.contractSubmitMsg,
                             {"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8"},postFile=False,postJson=True)
        TestContractFlow.contractId = json.loads(msg)["body"]["data"]["contractId"]
        sql=  "select * from ps_contract as a where a.id = %d" % int(TestContractFlow.contractId)
        row = dbconn.getAllRecode(sql)
        self.assertIsNotNone(row,'创建合同失败')
        #到时把这块封装成一个函数来进行检测
        self.assertEqual(row[0]["bailorId"],int(TestContractFlow.bailorInfo["bailorId"]))
        self.assertEqual(row[0]["customerId"],int(TestContractFlow.bailorInfo["customerId"]))
        self.assertEqual(row[0]["status"],5)
        self.assertEqual(row[0]["factMoney"],10950)#官费不正确
        self.assertEqual(row[0]["agencyFee"],6000,'代理费不正确')
        self.assertEqual(row[0]["additionalCharge"],1500,'附加费不正确')
        self.assertEqual(row[0]["publicExpense"],3450,'官费不正确')
        self.assertEqual(row[0]["factAgencyFee"],6000,'实际代理费不正确')
        #合同明细数据库验证
        sql = 'select * from ps_contract_detail  as a  where a.contractId = %d' % int(TestContractFlow.contractId)
        row = dbconn.getAllRecode(sql)
        self.assertIsNotNone(row,'创建合同明细失败')
        self.assertEqual(row[0]["commitmentId"],2)
        self.assertEqual(row[0]["money"],10950)
        self.assertEqual(row[0]["agencyFee"],6000)
        self.assertEqual(row[0]["publicExpense"],3450)
        self.assertEqual(row[0]["isStages"],0)
        self.assertEqual(row[0]["isRisk"],0)
        self.assertEqual(row[0]["isRebate"],0)
        # self.assertEqual(row[0]["isClarificaitonbook"],0)#这里有个bug
        self.assertEqual(row[0]["isPriority"],0)
        #委托联系人验证
        sql = 'select * from ps_contract_bailor_contact as a where a.contractId = %d' %int(TestContractFlow.contractId)
        row = dbconn.getAllRecode(sql)
        self.assertIsNotNone(row,"委托人、联系人数据无")
        print TestContractFlow.contractId
        print row[0]["customerId"],type(row[0]["customerId"])
        print TestContractFlow.bailorInfo["customerId"],type(TestContractFlow.bailorInfo["customerId"])
        self.assertEqual(row[0]['customerId'],int(TestContractFlow.bailorInfo["customerId"]),'customerId is not equal')
        self.assertEqual(row[0]["bailorId"],int(TestContractFlow.bailorInfo["bailorId"]))
        self.assertEqual(row[0]["bailorName"],TestContractFlow.bailorInfo["bailorName"])
        self.assertEqual(row[0]["contactId"],int(TestContractFlow.contactInfo["contactId"]))
        #委托基本信息数据库验证,detail
        sql = "select * from ps_contract_detail as a where a.contractId = %d and a.commitmentId = %d"  % (int(TestContractFlow.contractId),
                                                                                                          2)
        detailId = dbconn.getAllRecode(sql)[0]["id"]
        sql = "select * from ps_contract_detail_ext as a where a.contractDetailId= %d" % detailId
        row = dbconn.getAllRecode(sql)
        self.assertIsNotNone(row,"没有委托基本信息")
        self.assertEqual(row[0]["submitCheck"],1)
        self.assertEqual(row[0]["advancedPublic"],1)
        #费用信息数据库检测
        sql = "select * from ps_contract_detail_finance as a where a.contractDetailId = %d" %detailId
        row = dbconn.getAllRecode(sql)
        self.assertIsNotNone(row,'没有生成费用信息')
        sql = "select * from ps_contract_detail_proposer as a where a.contractId = %d and a.contractDetailId = %d " %(
            int(TestContractFlow.contractId),detailId
        )
        row = dbconn.getAllRecode(sql)
        self.assertIsNotNone(row,'申请人信息记录不成功')
        #发明人记录
        sql = "select * from ps_contract_detail_inventor as a where a.contractId = %d and a.contractDetailId = %d" %(
            int(TestContractFlow.contractId),detailId
        )
        row = dbconn.getAllRecode(sql)
        self.assertIsNotNone(row,'没有申请发明人')
        self.assertEqual(row[0]["certificateNo"],TestContractFlow.inventorInfo["cardno"])
        self.assertEqual(row[0]["inventorId"],int(TestContractFlow.inventorInfo["id"]))
        self.assertEqual(row[0]["enName"],TestContractFlow.inventorInfo["name_en"])
        #经办人 ps_contract_detail_operator
        sql = "select * from ps_contract_detail_operator as a where a.contractId = %d and a.contractDetailId = %d" %(
            int(TestContractFlow.contractId),detailId
        )
        row = dbconn.getAllRecode(sql)
        self.assertIsNotNone(row,'没有经办人')#经办人选验证下有没有记录
        #技术联系人
        sql = "select * from ps_contract_detail_technology_contact as a where a.contractId = %d and a.contractDetailId = %d" %(
            int(TestContractFlow.contractId),detailId
        )
        row = dbconn.getAllRecode(sql)
        self.assertIsNotNone(row,"没有技术联系人")

        print TestContractFlow.contractId
    @nottest
    def testDemo(self):
        self.assertIsNotNone(14,'it is none')
    def test_B_ContractSign(self):
        #签订标准合同
        print '='*30
        print '\n'
        print self.contractId

        genData = GeneratePostMsg.GenData(SignContract.SignStandardContractMsg)
        contractSignMsg = genData.genJsonData(1,customerInfo=None,bailorInfo=None,poroposerInfo=None,contactInfo=None,inventorInfo=None,
                            contractSignMsg={"contractId":TestContractFlow.contractId,
                                             "nextHandlerId":""})
        rspmsg = self.myhttp.post(urls.contractSignUrl,postData=contractSignMsg,postJson=True)
        sql = "select * from ps_contract as a where a.id = %d" % int(TestContractFlow.contractId)
        row = dbconn.getAllRecode(sql)
        self.assertEqual(row[0]['status'],1)


