# coding:utf-8
__author__ = 'angustang'
from  OCT.interface import  http
from  test.Msg import  submitContract
from  test.Msg import  GeneratePostMsg
from test.Msg import  BaseMsg
from  OCT.ToolsHub import GenDatetime
from test.ToolsHub import GetUserInfo
import  json
from  test.OCTcfg import  consultant,DBcfg
from  test.Msg import  ClarificationBook,SignContract
from nose.tools import  *
from test.ToolsHub import  urls
import  unittest
from OCT.ToolsHub import  myLog
from  OCT.DB.mysqlHandler import sqlCheck
class testClarificationFlow(unittest.TestCase):
    contractId =0
    clfBookId = 0
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
                testClarificationFlow.custormerID = item["id"]
            else:
                continue
        if not testClarificationFlow.custormerID:
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
        testClarificationFlow.custormerInfo = customerInfo
        testClarificationFlow.bailorInfo = bailorInfo
        testClarificationFlow.proposerInfo = proposerInfo
        testClarificationFlow.contactInfo = contactInfo
        testClarificationFlow.inventorInfo = inventorInfo
    @classmethod
    def teardown_class(cls):
        cls.myhttp.logout(urls.logoutUrl)
        pass
    def setUp(self):
        global  dbconn
        dbconn = sqlCheck(host=DBcfg.get("host"),user=DBcfg.get("username"),pswd=DBcfg.get("password"),
                          port=DBcfg.get("port"),dbname=DBcfg.get("dbname"))
        pass
    def tearDown(self):
        dbconn.clear()
        pass
    def test_a_SumbitContract(self):
        #创建合同
        rspMsg = self.myhttp.post(urls.contractSubmitUrl,postData=self.contractSubmitMsg,postJson=True)
        testClarificationFlow.contractId = json.loads(rspMsg)["body"]["data"]["contractId"]
        print rspMsg
        pass
    def test_b_ClarificationEdit(self):
        #编辑交底书, 向合同添加交底书信息
        #一个contract可能对应多个item
        contractDetailMsg = self.myhttp.post(urls.contractDetailUrl,
            {"id":self.contractId})
        #获取到detailID
        itemDetailId = json.loads(contractDetailMsg)["body"]["data"]["itemFinance"]["items"][0]["detailId"]
        itemDetailMsg =  self.myhttp.post(urls.contractItemDetailUrl+"?id="+itemDetailId,
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
        rspMsg = self.myhttp.post(urls.jdBookEditUrl,postData=clfEditMsg,
                                  postJson=True)
        #交底书验证
        sql = "select * from ps_clarificaitonbook as a where a.id = %d " % int(testClarificationFlow.clfBookId)
        row = dbconn.getAllRecode(sql)
        self.assertEqual(row[0]["contractId"],int(testClarificationFlow.contractId))
        self.assertEqual(row[0]["contractDetailId"],int(itemDetailId))
        self.assertEqual(row[0]["bailorId"],int(testClarificationFlow.bailorInfo["bailorId"]))
        self.assertEqual(row[0]["hasProject"],1)
        self.assertEqual(row[0]["hasClarificaitonbook"],1)
        self.assertEqual(row[0]["hasProject"],1)

        # print rspMsg
        pass
    def test_c_clarificationCheck(self):
        #切换至交底审核员，然后进行交底审核
        self.myhttp.logout(urls.logoutUrl)
        self.myhttp.login(urls.loginUrl,{
            "username":"ida",
            "password":"zz123asd"
        })
        srcClfCheckMsg={
                "clfBookId":self.clfBookId,
                "technosphereId":2,#技术领域
                "complexity":2#复杂程度
        }
        genData = GeneratePostMsg.GenData(ClarificationBook.ClarificationBookCheck)
        clfCheckMsg = genData.genJsonData(bizType=8,customerInfo=None,inventorInfo=None,bailorInfo=None,
                                          poroposerInfo=None,contactInfo=None,clfCheckMsg=srcClfCheckMsg)
        rspMsg = self.myhttp.post(urls.jdCheckerCheckUrl,postData=clfCheckMsg,
                                  )
        sql = "select * from ps_clarificaitonbook as a where a.id = %d " % int(testClarificationFlow.clfBookId)
        row = dbconn.getAllRecode(sql)
        self.assertEqual(row[0]["technosphereId"],srcClfCheckMsg.get("technosphereId"))
        self.assertEqual(row[0]["complexity"],srcClfCheckMsg.get("complexity"))
        sql = "select * from ps_trans as a where a.bizId = %d" % int(testClarificationFlow.clfBookId)
        row = dbconn.getAllRecode(sql)
        self.assertIsNotNone(row,'没有生成交底书流程')
        sql = "select * from ps_trans_log as a WHERE  a.bizId = %d" % int(testClarificationFlow.clfBookId)
        row = dbconn.getAllRecode(sql)
        self.assertIsNotNone(row,'交底流程日志没生成')
    def test_d_contractSign(self):
        #标准合同签订
        self.myhttp.logout(urls.logoutUrl)
        self.myhttp.login(urls.loginUrl,
            {
                "username":"elva",#顾问登录进行合同签订
                "password":"zz123asd"
            })
        StandardCheckMsg={
            "contractId":self.contractId,
        }
        dataGener = GeneratePostMsg.GenData(SignContract.SignStandardContractMsg)
        postMsg = dataGener.genJsonData(bizType=1,customerInfo=None,poroposerInfo=None,
                                        contactInfo=None,inventorInfo=None,bailorInfo=None,
                                        contractSignMsg=StandardCheckMsg)
        rspmsg = self.myhttp.post(urls.contractSignUrl,postData=postMsg,postJson=True)
        sql = "select * from ps_contract as a where a.id = %d" % int(testClarificationFlow.contractId)
        row = dbconn.getAllRecode(sql)
        self.assertIsNotNone(row,'更新合同记录失败')


