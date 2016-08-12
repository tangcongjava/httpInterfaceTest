# coding:utf-8
__author__ = 'angustang'
from  test.testcase.clarification import  checkerCheck
from  OCT.interface import  http
from  nose.tools import  *
from test.ToolsHub import  urls
from  test.OCTcfg import consultant
import  unittest
from test.OCTcfg import  DBcfg
from  OCT.DB.mysqlHandler import  sqlCheck
import  json
#之所以这样写的原因是为重新创建一个测试用例
class testBefore(checkerCheck.testClarificationFlow):
    pass
class testCase(unittest.TestCase):
    myhttp = http.MyHttp()
    @classmethod
    def setup_class(cls):
        cls.myhttp.login(urls.loginUrl,logindata={
            "username":consultant.get("username"),
            "password":consultant.get("password")
        })
        pass
    @classmethod
    def teardown_class(cls):
        cls.myhttp.logout(urls.logoutUrl)
        pass
    def setUp(self):
        global  dbconn
        dbconn = sqlCheck(host=DBcfg.get("host"),user=DBcfg.get("username"),pswd=DBcfg.get("password"),
                          port=DBcfg.get("port"),dbname=DBcfg.get("dbname"))

    def tearDown(self):
        dbconn.clear()
    def getCaseID(self,rspMsg,contractID):
        #获取案件ID
        rspMsg = json.loads(rspMsg)
        for caseInfo in rspMsg["body"]["data"]["rows"]:
            if caseInfo["contractId"] == contractID:
                caseId  = caseInfo["id"]
            else:
                continue
        return  caseId
    def pay(self,contractId):
        print "*****************************"
        rspMsg  = self.myhttp.post(urls.payCaseQueryUrl,postData={
            "ourDocNo":"",
            "contractCode":"",
            "bailorName":"",
            "customerName":"",
            "title":""
        },postHeaders={"X-Requested-With":"XMLHttpRequest"})
        #通过合同ID获取到对应的待付款数据库ID
        for item in json.loads(rspMsg)["body"]["data"]["rows"]:
            if item["contractId"] == contractId:
                itemID = item["id"]
            else:
                continue
        rspMsg = self.myhttp.post(urls.payFromBanlanceUrl,{
            "ids":itemID #这里的IDS不是合同id，而是查询出来的待支付的ID
        })
        print '888888888'+'payment msg is ' +rspMsg
    def testCaseApply(self):
        #立案申请,使用类继承可以实现测试用例的重复使
        #1.先查询出业待立案的案子.
        print "case msg is "
        caseMsg = self.myhttp.post(postUrl=urls.caseQueryUrl,postData={
            "page":1,
            "handleType":1
        })
        print caseMsg
        caseID = self.getCaseID(caseMsg,checkerCheck.testClarificationFlow.contractId)
        # print "=====================the contract id is "+self.getCaseID(caseMsg,ClarificationFlow2.testClarificationFlow.contractId)
        #2 付款,这里还要添加一下钱不够的情况
        self.pay(checkerCheck.testClarificationFlow.contractId)
        #3.再发起立案申请
        caseApplyMsg = {
            "nextHandlerId":962,#下一节点处理人ID,写在配置文件
            "id":caseID,# case id
            "patentType":1,#专利类型
            "remark":"",
            "divideRateData":#
                {
                    "hasDivideConsultant": 0,#分成顾问
                    "divideConsultant": []
                }
        }
        rntmsg = self.myhttp.post(urls.submitApplyUrl,postData=caseApplyMsg)
        sql = "select * from ps_case as a where a.contractId = %d" % int(checkerCheck.testClarificationFlow.contractId)
        row = dbconn.getAllRecode(sql)
        self.assertIsNotNone(row,'立案信息录入失败')
        self.assertEqual(row[0]["customerId"],int(checkerCheck.testClarificationFlow.bailorInfo["customerId"]))
        self.assertEqual(row[0]["bailorId"],int(checkerCheck.testClarificationFlow.bailorInfo["bailorId"]))
        self.assertEqual(row[0]["status"],2)#待审核状态
        self.assertEqual(row[0]["fee"],10950)
        self.assertEqual(row[0]["payed"],10950)
        self.assertEqual(row[0]["agencyFee"],6000)
        self.assertEqual(row[0]["publicExpense"],3450)
        self.assertEqual(row[0]["additionalCharge"],1500)
        self.assertEqual(row[0]["isClarificaitonbook"],1)
        self.assertEqual(row[0]["agencyId"],0)
        self.assertEqual(row[0]["qaId"],0)
        self.assertEqual(row[0]["finishedClarificaitonbook"],1)
        sql = "select * from ps_case_ext as a where a.caseId = %d " % int(caseID)
        row = dbconn.getAllRecode(sql)
        self.assertIsNotNone(row,'录入案件扩展信息不正确')
        self.assertEqual(row[0]["contractId"],int(checkerCheck.testClarificationFlow.contractId))
        sql ="select * from ps_trans as a where a.bizId = %d and a.bizModel = 'case' " % int(caseID)
        row = dbconn.getAllRecode(sql)
        self.assertIsNotNone(row,'流程数据录入不成功')
        self.assertEqual(row[0]["nodeId"],18)
        self.assertEqual(row[0]["bizModel"],"case")
        print rntmsg


