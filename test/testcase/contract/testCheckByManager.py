# coding:cp936
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

#��ͬ���̵Ľӿڲ���

class TestContractCheckByManager(unittest.TestCase):

    '''
      �Ǳ��ͬʡ���������ͨ��
    '''
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
        #��¼����ȡ�ͻ�����Ϣ
        cls.crm.myhttp.login(urls.loginUrl,
                             {"username":consultant.get("username"),"password":consultant.get("password")})
        #��ȡ�ͻ���Ϣ,Ȼ�����ѡ��һ��
        customerList= cls.crm.getCustormInfo(postdata={
            "page":1,
            "pageSize":15
        })
        customerInfo=None
        for item in customerList:#item�������һ���ͻ���Ϣ
            if item["name"].find(unicode(consultant["customerName"],"utf-8")) != -1:
                cls.crm.setCustomerID(item["id"])
                customerInfo=item
                TestContractCheckByManager.custormerID = item["id"]
            else:
                continue
        if not TestContractCheckByManager.custormerID:
            raise  Exception("the customer is not vaild,pls check the config")#��������û�ж�Ӧ�Ŀͻ�

        bailorInfo = cls.crm.getBailorInfo()
        cls.log.debug(u"ί������Ϣ")
        cls.log.debug(bailorInfo)

        proposerInfo = cls.crm.getProposerInfo()
        cls.log.debug(u"��������Ϣ")
        cls.log.debug(proposerInfo)
        contactInfo = cls.crm.getContactInfo()
        cls.log.debug(u"��ϵ����Ϣ")
        cls.log.debug(contactInfo)
        inventorInfo = cls.crm.getInventorInfo()
        cls.log.debug(u'��������Ϣ')
        cls.log.debug(inventorInfo)
        # print BailorInfo
        genData = GeneratePostMsg.GenData(submitContract.submitContractWithoutClarificationMsg,BaseMsg.itemsAndFeeWithoutClarification)
        cls.contractSubmitMsg = genData.genJsonData(bizType=6,customerInfo=customerInfo,bailorInfo=bailorInfo,
                                                    poroposerInfo=proposerInfo,contactInfo=contactInfo,
                                                    inventorInfo=inventorInfo)#ֱ�Ӵ���һ����Ŀͻ���Ϣ�ֵ�
        TestContractCheckByManager.custormerInfo = customerInfo
        TestContractCheckByManager.bailorInfo = bailorInfo
        TestContractCheckByManager.proposerInfo = proposerInfo
        TestContractCheckByManager.contactInfo = contactInfo
        TestContractCheckByManager.inventorInfo = inventorInfo
        pass
    @classmethod
    def teardown_class(cls):
        '''
            the function of teardown
        :return:
        '''
        cls.myhttp.logout(urls.logoutUrl)
        pass
    def setUp(self):
        global  dbconn

        dbconn = sqlCheck(host=DBcfg.get("host"),user=DBcfg.get("username"),pswd=DBcfg.get("password"),
                          port=DBcfg.get("port"),dbname=DBcfg.get("dbname"))
        pass
    def tearDown(self):
        dbconn.clear()
    def test_a_ContractSubmit(self):
        #�ύ��ͬ
        rspMsg = self.myhttp.post(urls.contractSubmitUrl,self.contractSubmitMsg,postJson=True)
        TestContractCheckByManager.contractId= json.loads(rspMsg)["body"]["data"]["contractId"]
    def test_b_NoStandarContractSign(self):
        #�ύ�Ǳ�׼��ͬ
        nonStandardContrackSignMsg={
                "id":TestContractCheckByManager.contractId,
                "contractId":TestContractCheckByManager.contractId,
                "nextHandlerId":"2549"#�ύ������ʡ������
        }
        dataGener = GeneratePostMsg.GenData(SignContract.SignNonStandardContractMsg)
        postMsg = dataGener.genJsonData(bizType=2,
                                        contractSignMsg=nonStandardContrackSignMsg,customerInfo=None,inventorInfo=None,
                                        bailorInfo=None,poroposerInfo=None,contactInfo=None)
        rspMsg = self.myhttp.post(urls.contractSignUrl,postData=postMsg,postJson=True)
        sql = 'select * from ps_contract as a where a.id = %d' % int(TestContractCheckByManager.contractId)
        row = dbconn.getAllRecode(sql)
        self.assertEqual(row[0]["status"],3)
        self.assertEqual(row[0]["type"],2)
        #������־���ps_trans
        sql = 'select * from ps_trans as a where a.bizid = %d' % int(TestContractCheckByManager.contractId)
        row = dbconn.getAllRecode(sql)
        self.assertIsNotNone(row,'�������̼�¼������')
        transId = row[0]["id"]
        self.assertEqual(row[0]["bizId"],int(TestContractCheckByManager.contractId))
        self.assertEqual(row[0]["bizModel"],"contract")
        self.assertEqual(row[0]["handleId"],2549)
        self.assertEqual(row[0]["flowId"],1)
        self.assertEqual(row[0]["nodeId"],5)
        sql = 'select * from  ps_trans_log as a WHERE  a.transId = %d' % int(transId)
        row = dbconn.getAllRecode(sql)
        self.assertIsNotNone(row,'����������־������')
    def test_c_contractCheckManager(self):
        #�л���ʡ�������¼��Ȼ��������
        self.myhttp.logout(urls.logoutUrl)
        self.myhttp.login(urls.loginUrl,{
            "username":"belly",
            "password":"zz123asd"
        })
        managerCheckMsg={
            "contractId":TestContractCheckByManager.contractId,
        }
        dataGener = GeneratePostMsg.GenData(nonStandardContrackCheck.nonStandardCheckByManagerMsg)
        postMsg = dataGener.genJsonData(bizType=3,ManagerCheckMsg=managerCheckMsg,
                                        customerInfo=None,bailorInfo=None,inventorInfo=None,
                                        contactInfo=None,poroposerInfo=None)
        rspmsg = self.myhttp.post(urls.nostandardContractCheck,postData=postMsg,
                         postJson=True)
        sql = "select * from ps_contract as a where a.id = %d" % int(TestContractCheckByManager.contractId)
        row = dbconn.getAllRecode(sql)
        self.assertIsNotNone(row,'���º�ͬ��¼ʧ��')
        self.assertEqual(row[0]["status"],5)
        sql = "select * from ps_trans as a where a.bizid = %d" % int(TestContractCheckByManager.contractId)
        row = dbconn.getAllRecode(sql)
        self.assertIsNotNone(row,'���º�ͬ��¼��Ϣʧ��')
        self.assertEqual(row[0]["nodeId"],8)
        self.assertEqual(row[0]["bizModel"],"contract")
        pass
    def test_d_contractSign(self):
        #ʡ������˺󣬽��к�ͬǩ��
        self.myhttp.logout(urls.logoutUrl)
        self.myhttp.login(urls.loginUrl,{
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
        rspmsg = self.myhttp.post(urls.contractSignUrl,postData=postMsg,postJson=True)
        print  rspmsg
        sql = "select * from ps_contract as a where a.id = %d" % int(TestContractCheckByManager.contractId)
        row = dbconn.getAllRecode(sql)
        self.assertIsNotNone(row,'���º�ͬ״̬ʧ��')
        self.assertEqual(row[0]["status"],1)
        #����԰����Ƿ�����
        sql = 'select * from ps_case as a where a.contractId = %d' % int(TestContractCheckByManager.contractId)
        row = dbconn.getAllRecode(sql)
        self.assertIsNotNone(row,'���ɰ���ʧ��')
        self.assertEqual(row[0]["status"],0)
        self.assertEqual(row[0]["customerId"],int(TestContractCheckByManager.bailorInfo["customerId"]))
        self.assertEqual(row[0]["bailorId"],int(TestContractCheckByManager.bailorInfo["bailorId"]))
        self.assertIsNotNone(row[0]["ourDocNo"],'�����ҷ��ĺ�Ϊ��')
        pass

if __name__ == '__main__':
    nosearg=['foo','-s','-v','ContractFlow.py:TestContractFlow']
    nose.run(argv=nosearg)
