# coding:utf-8
__author__ = 'angustang'
# 上传交底书或提交全同的JSON传递消息
ClarificationBookUpload={
  "id": "",# 合同ID，0表示添加，1表示编辑，
  "customerId": None,#客户ID
  "customerName": None,#客户信息
  "bailorId": None,#委托人ID
  "bailorWholeAddress": None,#委托人的全部地址
  "contactId": None,#联系人ID
  "money": None,#合同总费用
  "agencyFee": None,#合同总代理费
  "additionalCharge": None,#附加费
  "publicExpense": None,#总官费
  "publicExpenseTitleCate": "3",
  "publicExpenseTitle": "超凡志成",
  "remark": "",
  "nextHandler": 0,#下一点处理人 在新建合同的时候就上传交底时下一点处理人就是0
  "businessType": 0,#业务类型
  "tplType": 0,
  "items": [#start
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
        "name": "超凡专利交底书模板7-11",
        "hasProject": 1,
        "hasClarificaitonbook": 1,
        "hasPicture": 0,
        "remark": "",
        "bookFile": "[{\"file_no\":\"A00112602\",\"file_name\":\"超凡专利交底书模板.doc\"}]",
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
          "proposerId": "111289",
          "proposerCountryId": "1",
          "proposerProvinceId": "112",
          "proposerCityId": "326",
          "proposerAreaId": "729",
          "proposerCardNo": "45645654654654",
          "proposerEnName": "test",
          "proposerZipcode": "610000",
          "proposerAddress": "草市街123号",
          "proposerEnAddress": "TESTADDRESS",
          "officialSeal": "",
          "license": "[{\"path\":\"http:\\/\\/demo.chofn.com:88\\/uploads\\/documents\\/2016\\/06\\/14\\/d41f47f882728f67.jpg\",\"name\":\"\\u8425\\u4e1a\\u6267\\u7167.jpg\",\"size\":10107}]",
          "licenseTranslate": "[{\"path\":\"http:\\/\\/demo.chofn.com:88\\/uploads\\/documents\\/2016\\/06\\/14\\/8b74c2bb42d92c4a.jpg\",\"name\":\"\\u62a4\\u7167.jpg\",\"size\":20944}]",
          "idCard": "[{\"path\":\"http:\\/\\/demo.chofn.com:88\\/uploads\\/documents\\/2016\\/06\\/14\\/ce70b1cf3d9d117b.jpg\",\"name\":\"\\u8eab\\u4efd\\u8bc1\\u7167.jpg\",\"size\":42314}]",
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
  ],#end
  "errorList": {
    "hasError": False,
    "msg": [
      ""
    ]
  },
  "contactMobile": None,
  "contactEmail": None,
  "contactTel":None
}
#新建合同后，添加交底书
ClarificationBookEdit={
  "id": 252,#交底书ID
  "hasProject": 1,
  "hasClarificaitonbook": 1,
  "hasPicture": 1,
  "bookFile": [
    {
      "file_no": "A00114291",
      "file_name": "QQ截图20160719203053.bmp"
    }
  ],
  "name": "angustest",
  "otherFile": [

  ],
  "remark": "",
  "checkerRemark": ""
}
#交底审核员，审核
ClarificationBookCheck={
  "technosphereId":2,#技术类别
   "complexity":2,#复杂程度
    "remark":"交底书审核通过",#备注
    "result":1,#处理结果
    "id":52#交底书ID
}
#部门经理审核交底书
ClarificationBookCheckByDeptManager={
    "remark":"",
    "result":2,#交给上级领导审核
    "id":52#交底书ID
}
