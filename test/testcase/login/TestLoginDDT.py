#coding=cp936
'''��¼�ӿڲ���������'''

from OCT.ToolsHub.decorators import getData
from OCT.interface.http import MyHttp
from test.OCTcfg import URL_PATENT_BASE
import json
import nose
from nose.tools import  *
from  OCT.ToolsHub import  myLog
import  ddt
import  unittest
from  OCT.ToolsHub import  getData
__author__ = 'wanel.zhang'

#��¼�ӿ����ӵ�ַ
url_login = URL_PATENT_BASE+"/index/index/"

#�ǳ��ӿ����ӵ�ַ
url_logout = URL_PATENT_BASE+"/index/logout/"

log = myLog.MyLogging(__file__)
myhttp = MyHttp()

def login(username, password,myhttp = MyHttp()):
    ''' ��¼
    '''
    requestData={}
    requestData["username"] = username
    requestData["password"] = password
#     print logindata

    resp = myhttp.login(url_login, requestData)
    print "��¼���󷵻ؽ��Ϊ�� ", resp.decode("unicode_escape")
    return json.loads(resp)

def logout(myhttp):
    ''' �ǳ�
    '''
    myhttp.logout(url_logout)
    


@ddt.ddt
class LoginTest(unittest.TestCase):
    @ddt.data(*getData.get_csv_data("../../resource/login/TestLogin.loginNormalCase.csv"))
    @ddt.unpack
    def testloginNormalCase(self,caseid,  username, password):
        '''
        ������¼
        '''
        log.debug('\n���յ��Ĳ���Ϊ�� caseid=%s,  username=%s, password=%s' \
          % (caseid,  username, password))
        print '\n���յ��Ĳ���Ϊ�� caseid=%s,  username=%s, password=%s' \
          % (caseid,  username, password)
        try:
            resp = login(username, password, myhttp)
            assert resp["header"]["code"] == 104
            assert resp["body"]["status"] == 1
        finally:
            logout(myhttp)
        pass
if __name__ == "__main__":
    # noseArg=['-v','-s',__file__,'--with-html','--html-file=output.html']
    # assert nose.run(argv=noseArg)
    testCases = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    testSuite = unittest.TestSuite([testCases])
    unittest.TextTestRunner(verbosity=2).run(testSuite)


