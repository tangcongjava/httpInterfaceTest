#coding=cp936
'''登录接口测试用例集'''

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

#登录接口链接地址
url_login = URL_PATENT_BASE+"/index/index/"

#登出接口链接地址
url_logout = URL_PATENT_BASE+"/index/logout/"

log = myLog.MyLogging(__file__)
myhttp = MyHttp()

def login(username, password,myhttp = MyHttp()):
    ''' 登录
    '''
    requestData={}
    requestData["username"] = username
    requestData["password"] = password
#     print logindata

    resp = myhttp.login(url_login, requestData)
    print "登录请求返回结果为： ", resp.decode("unicode_escape")
    return json.loads(resp)

def logout(myhttp):
    ''' 登出
    '''
    myhttp.logout(url_logout)
    


@ddt.ddt
class LoginTest(unittest.TestCase):
    @ddt.data(*getData.get_csv_data("../../resource/login/TestLogin.loginNormalCase.csv"))
    @ddt.unpack
    def testloginNormalCase(self,caseid,  username, password):
        '''
        正常登录
        '''
        log.debug('\n接收到的参数为： caseid=%s,  username=%s, password=%s' \
          % (caseid,  username, password))
        print '\n接收到的参数为： caseid=%s,  username=%s, password=%s' \
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


