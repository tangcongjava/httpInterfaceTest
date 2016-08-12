# coding:utf-8
# __author__ = 'angustang'
from interface import  http
import  json
import  os
from  nose.tools import  *
def testLogin():
    pass
def testupfiles():
    filelist = os.listdir("./fileHubs")
    for filename in filelist:
        yield  testUploadJDFile,filename
@nottest
def testUploadJDFile(filname=None):
    myhttp = http.MyHttp()
    loginData={
        "username":"elva",
        "password":"zz123asd"
    }
    loginurl = "http://patent.test.chofn.net/index/index/"
    logouturl = "http://patent.test.chofn.net/index/logout/"
    respmsg = myhttp.login(loginurl,loginData)
    rspmsg = myhttp.postFile("http://patent.test.chofn.net/File/upload","uploadFile","./fileHubs/20160606170312.bmp")
    file_name =json.loads(rspmsg)["body"]["data"][0]['file_name']
    file_no =json.loads(rspmsg)["body"]["data"][0]['file_no']

    postdata ={
  "id": "",
  "customerId": "1383188",
  "customerName": "15982056452",
  "bailorId": "111289",
  "bailorWholeAddress": "四川省成都市青羊区草市街123号",
  "contactId": "1085383",
  "money": "9950.00",
  "agencyFee": "6000.00",
  "additionalCharge": "500.00",
  "publicExpense": "3450.00",
  "publicExpenseTitleCate": "3",
  "publicExpenseTitle": "超凡志成",
  "remark": "",
  "nextHandler": 0,
  "businessType": 0,
  "tplType": 0,
  "items": [
    {
      "id": "0",
      "detailExtId": 0,
      "commitmentId": "2",
      "businessId": 1,
      "isCompleteInfo": 1,
      "money": "9950.00",
      "agencyFee": "6000.00",
      "publicExpense": "3450.00",
      "additionalCharge": "500.00",
      "remark": "",
      "clarificaitonbook": {
        "id": "0",
        "name": "20160606170312",
        "hasProject": 1,
        "hasClarificaitonbook": 1,
        "hasPicture": 0,
        "remark": "",
        "bookFile": "[{\"file_no\":\"A00111183\",\"file_name\":\"20160606170312.bmp\"}]",
        "otherFile": "",
        "isSubCheck": 1
      },
      "timeLimit": "15",
      "cutFee": "0",
      "rightItemNum": "",
      "specificationPageNum": "",
      "submitCheck": "1",
      "advancedPublic": "1",
      "isRisk": 0,
      "isPriority": "0",
      "priority": [

      ],
      "proposer": [
        {
          "id": 0,
          "proposerId": "123261",
          "proposerCountryId": "1",
          "proposerProvinceId": "0",
          "proposerCityId": "0",
          "proposerAreaId": "0",
          "proposerCardNo": "45645654654654",
          "proposerEnName": "",
          "proposerZipcode": "610000",
          "proposerAddress": "",
          "proposerEnAddress": "",
          "officialSeal": "",
          "license": "",
          "licenseTranslate": "",
          "idCard": "",
          "sort": 1
        }
      ],
      "inventor": [
        {
          "id": 0,
          "inventorId": "61",
          "sort": 1,
          "firstInventor": 1,
          "name": "",
          "certificateName": "",
          "certificateNo": "",
          "publishName": "1",
          "countryId": "",
          "cardIds": [

          ]
        }
      ],
      "operatorId": "2108094",
      "technologyContact": {
        "id": 0,
        "technologyContactId": "2108094",
        "name": "jinban",
        "mobile": "13724237588",
        "email": ""
      },
      "fee": {
        "isRebate": 0,
        "partner": "",
        "partnerMoney": "",
        "isStages": 0,
        "firstPayed": "",
        "stagesWay": ""
      },
      "hasDivideConsultant": 0,
      "divideConsultant": [

      ],
      "feeList": [
        {
          "id": "0",
          "detailId": "0",
          "cate": "1",
          "paymentNameId": "8",
          "paymentName": "国内专利发明申请代理费",
          "money": "6000.00",
          "isRebate": "0",
          "businessId": "1"
        },
        {
          "id": "0",
          "detailId": "0",
          "cate": "3",
          "paymentNameId": "14",
          "paymentName": "制图费",
          "money": "500.00",
          "isRebate": "0",
          "businessId": "1"
        },
        {
          "id": "0",
          "detailId": "0",
          "cate": "2",
          "paymentNameId": "7",
          "paymentName": "实质审查费",
          "money": "2500.00",
          "isRebate": "0",
          "businessId": "1"
        },
        {
          "id": "0",
          "detailId": "0",
          "cate": "2",
          "paymentNameId": "2",
          "paymentName": "文件印刷费",
          "money": "50.00",
          "isRebate": "0",
          "businessId": "1"
        },
        {
          "id": "0",
          "detailId": "0",
          "cate": "2",
          "paymentNameId": "1",
          "paymentName": "申请费",
          "money": "900.00",
          "isRebate": "0",
          "businessId": "1"
        }
      ]
    }
  ],
  "errorList": {
    "hasError": False,
    "msg": [
      ""
    ]
  },
  "contactMobile": "15982056452",
  "contactEmail": "test@126.com",
  "contactTel": "028-86934296"
}
    fileinfo="[{\"file_no\":\"%s\",\"file_name\":\"%s\"}]" % (file_no,file_name)
    postdata["items"][0]["clarificaitonbook"]["bookFile"] = fileinfo
    msg = myhttp.post("http://patent.test.chofn.net/clarificaitonbookcheck/add/",postdata,{"Content-Type":
                                                                                           "application/x-www-form-urlencoded;charset=UTF-8"},postFile=False,postJson=True)
    assert_equal(json.loads(msg)["header"]["msg"],u'操作成功')
    assert_equal(json.loads(msg)["body"]["data"]["success"],True)
    print msg
    #这里从服务器的返回信息获取到数据对返回结果进行难证
    print rspmsg
    # myhttp.parseRspMsg(respmsg)
    print myhttp.logout(logouturl)
def testUpdateJDbook():
    assert_equal("aaa","bbb","aaa not equal bbb")
@nottest
def testCheckJDbook():
    logindata = {
        "username":"ida",
        "password":"zz123asd"
    }
    loginurl = "http://patent.test.chofn.net/index/index/"
    myhttp= http.MyHttp()
    myhttp.login(loginurl,logindata)
    type={
        'handleType':1
    }
    myhttp.post("http://patent.test.chofn.net/clarificaitonbookcheck/statusList/",type,{"Content-Type":
                                                                                           "application/x-www-form-urlencoded;charset=UTF-8"},postFile=False,postJson=False)
    data={
        "bailorName":'',
        "consultantName":'',
        "submitTime":0
    }

    uncheckurl = "http://patent.test.chofn.net/ClarificaitonbookCheck/index/?page=1&handleType=1"
    #get the uncheckitem
    rntmsg = myhttp.post(uncheckurl,data)
    items = json.loads(rntmsg)["body"]["data"]["rows"]
    #将最大的item项的项进行审核,
    verifyData = {
        'technosphereId':'2',
        'complexity':'2',
        'remark':'autotest',
        'result':'1',
        'id':items[len(items)-1]["id"]
    }
    rntmsg = myhttp.post(postUrl="http://patent.test.chofn.net/ClarificaitonbookCheck/check/",postData=verifyData)
    print rntmsg
    # itemid=[]
    # maxid = ""
    # for eachitem in items:
    #     a = 0
    #     if a ==1:
    #         break
    #     itemid.append(eachitem["id"])
    #     verifyData = {
    #     'technosphereId':'2',
    #     'complexity':'2',
    #     'remark':'',
    #     'result':'1',
    #     'id':eachitem["id"]
    # }
    #     rntmsg = myhttp.post("http://patent.test.chofn.net/ClarificaitonbookCheck/check/",verifyData)
    #     print rntmsg
if __name__ == '__main__':
    # testUploadJDFile()
    # testCheckJDbook()
    testupfiles()