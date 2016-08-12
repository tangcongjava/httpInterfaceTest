# coding:utf-8
from urllib import unquote
__author__ = 'angustang'
itemsAndFee = {
      "id": "0",#委托事项ID
      "detailExtId": 0,#合同明细扩展ID
      "commitmentId": "2",#委托事项id
      "businessId": 1, #业务id(一个委托事项可能包含多个业务) 在数据库ps_commitment_business中查看委托事项,在ps_business中查看具体的业务
      "isCompleteInfo": 1,
      "money": "9950.00",#事项总费用
      "agencyFee": "6000.00",#代理费
      "publicExpense": "3450.00",#官费
      "additionalCharge": "500.00",#附加费
      "remark": "",#委托事项备注
      "clarificaitonbook": {
        "id": "0",
        "name": "超凡专利交底书模板7-11",#交底书名称
        "hasProject": 1,#是否有方案
        "hasClarificaitonbook": 1,
        "hasPicture": 0,
        "remark": "",
        "bookFile": "[{\"file_no\":\"A00112602\",\"file_name\":\"超凡专利交底书模板.doc\"}]",
        "otherFile": "",
        "isSubCheck": 1#是否审核，交底书审核和合同提交审核的情况是一样的。
      },
      "timeLimit": "15",#返初稿时间
      "cutFee": "0",#费减信息
      "rightItemNum": "",#权利要求项数
      "specificationPageNum": "",#说明书页数
      "submitCheck": "1",#是否提交实审请求
      "advancedPublic": "1",#是否要求提前公开
      "isRisk": 0,#是否风险代理 0代表否
      "isPriority": "0",#是否申请优先权，0代表否，
      "priority": [

      ],#优先级信息
      "proposer": [
        {
          "id": 0,#申请人编号ID
          "proposerId": "111289",#申请人ID
          "proposerCountryId": "1",#申请人国家ID
          "proposerProvinceId": "112",#申请人省ID... 这个先不做动态化
          "proposerCityId": "326",#城市ID
          "proposerAreaId": "729",#区域ID
          "proposerCardNo": "45645654654654",#证件号
          "proposerEnName": "test",#申请英文名
          "proposerZipcode": "610000",#邮政编号
          "proposerAddress": "草市街123号",#申请人地址(街道)
          "proposerEnAddress": "TESTADDRESS",#申请人英名地址
          "officialSeal": "",#公章，签名图片
          "license": "[{\"path\":\"http:\\/\\/demo.chofn.com:88\\/uploads\\/documents\\/2016\\/06\\/14\\/d41f47f882728f67.jpg\",\"name\":\"\\u8425\\u4e1a\\u6267\\u7167.jpg\",\"size\":10107}]",#这个先写在这里
          "licenseTranslate": "[{\"path\":\"http:\\/\\/demo.chofn.com:88\\/uploads\\/documents\\/2016\\/06\\/14\\/8b74c2bb42d92c4a.jpg\",\"name\":\"\\u62a4\\u7167.jpg\",\"size\":20944}]",
          "idCard": "[{\"path\":\"http:\\/\\/demo.chofn.com:88\\/uploads\\/documents\\/2016\\/06\\/14\\/ce70b1cf3d9d117b.jpg\",\"name\":\"\\u8eab\\u4efd\\u8bc1\\u7167.jpg\",\"size\":42314}]",
          "sort": 1 #排序用来给数据库录入数据
        }
      ],
      "inventor": [
        {
          "id": "0",#发文明编号
          "customerId":"1383188",
          "inventorId": "61",#发文明ID
          "sort": "1",#?
          "firstInventor": 1,#是否是第一发明人
          "name": "周杰伦",#姓名
          "certificateID":"1",
          "certificateName": "身份证",#证件名称
          "certificateNo": "513902199009204664",#证件号
          "publishName": "1",#是否公布姓名
          "countryId": "4",#国家ID
          "cardIds": [#证件信息
              {
                "filename": "7c5d9598eb99973f0dd6d9eab11ece44 .jpg",
              "filesize": 42314,
              "filetype": "jpg",
              "filepath": "http://demo.chofn.com:88/uploads/documents/2016/07 /19/a098cc3a652c714d.jpg",
              "id": 2984
              }
          ]
        }
      ],
      "operatorId": "2108094",#合同明细经办人id
      "technologyContact": {#技术联系人
        "id": 0,
        "technologyContactId": "2108094",#联系人ID
        "name": "jinban",#姓名
        "mobile": "13724237588",#电话
        "email": ""#邮箱地址
      },
      "fee": {
        "isRebate": 0,#是否返点 （合同明细费用表里
        "partner": "",#合作者名字
        "partnerMoney": "",#返点多少元
        "isStages": 0,
        "firstPayed": "",
        "stagesWay": ""
      },
      "hasDivideConsultant": 0,#是否勾选分成顾问
      "divideConsultant": [#分成顾问信息

      ],
      "feeList": [#费用列表
        {
          "id": "0",
          "detailId": "0",
          "cate": "1",#费用类别
          "paymentNameId": "8",#费用名义ID
          "paymentName": "国内专利发明申请代理费",#费用名义
          "money": "6000.00",#费用数量
          "isRebate": "0",#是否返点
          "businessId": "1"#业务ID
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

itemsAndFeeWithoutClarification={
  "id": "0",
  "detailExtId": 0,
  "commitmentId": "2",
  "businessId": 1,
  "isCompleteInfo": 1,
  "money": "10950.00",
  "agencyFee": "6000.00",
  "publicExpense": "3450.00",
  "additionalCharge": "1500.00",
  "remark": "",
  "clarificaitonbook": {
    "id": "0",
    "name": "",
    "hasProject": 0,
    "hasClarificaitonbook": 0,
    "hasPicture": 0,
    "remark": "",
    "bookFile": "",
    "otherFile": ""
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
      "id": "0",
      "customerId": "1383188",
      "inventorId": "61",
      "sort": "1",
      "firstInventor": "1",
      "name": "周杰伦",
      "certificateID": "1",
      "certificateName": "身份证",
      "certificateNo": "513902199009204664",
      "publishName": "1",
      "countryId": "4",
      "country_name": "朝鲜",
      "cardIds": [
        {
          "filename": "7c5d9598eb99973f0dd6d9eab11ece44 .jpg",
          "filesize": 42314,
          "filetype": "jpg",
          "filepath": "http://demo.chofn.com:88/uploads/documents/2016/07 /19/a098cc3a652c714d.jpg",
          "id": 2984
        }
      ]
    }
  ],
  "operatorId": "2108094",#联系人ID
  "technologyContact": {
    "id": 0,
    "technologyContactId": "2108094",
    "name": "",
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
  "feeList": [#费用列表
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
      "paymentNameId": "13",
      "paymentName": "交底书撰写费",
      "money": "1000.00",
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
# 交底书中文件模板
bookFile = {"file_no":"A00112602","file_name":"超凡专利交底书模板.doc"}

# 优先权模板
priorityItem = {
          "applyNo": "001002001",
          "applyDate": "2001-02-01",
          "proposerName": "李龙海",
          "countryId": "1"
}

# 发明人中身份信息模板
cardIdItem = {
              "filename": "发明人复印件.png",
              "filesize": 111933,
              "filetype": "png",
              "filepath": "http://demo.chofn.com:88/uploads/documents/2016/05/31/a7228a8b51dd2b55.png",
              "id": 2713
            }

# 顾问分成项模板
divideConsultantItem = {
          "id": 0,
          "consultantId": "1725",
          "rate": "65"
        }

# 费用项模板
feeItem = {
      "id": "0",
      "detailId": "0",
      "cate": "2",
      "paymentNameId": "1",
      "paymentName": "申请费",
      "money": "900.00",
      "isRebate": "0",
      "businessId": "1"
}

# 申请人项模板
proposerItem = {
          "id": 0,
          "proposerId": "111309",
          "proposerCountryId": "1",
          "proposerProvinceId": "103",
          "proposerCityId": "173",
          "proposerAreaId": "0",
          "proposerCardNo": "444",
          "proposerEnName": "",
          "proposerZipcode": "620000",
          "proposerAddress": "放电了134号",
          "proposerEnAddress": "333",
          "officialSeal": "[{\"path\":\"http:\\/\\/demo.chofn.com:88\\/uploads\\/documents\\/2016\\/07\\/23\\/bc3663b064b5c3da.jpg\",\"name\":\"\\u516c\\u7ae0\\u7b7e\\u540d.jpg\",\"size\":188721}]",
          "license": "[{\"path\":\"http:\\/\\/demo.chofn.com:88\\/uploads\\/documents\\/2016\\/07\\/23\\/039fa5c764b3a909.pdf\",\"name\":\"\\u5de5\\u5546\\u6267\\u7167.pdf\",\"size\":219291}]",
          "licenseTranslate": "[{\"path\":\"http:\\/\\/demo.chofn.com:88\\/uploads\\/documents\\/2016\\/07\\/23\\/092ff0123d75731f.zip\",\"name\":\"\\u6267\\u7167\\u6216\\u7ffb\\u8bd1.zip\",\"size\":113110}]",
          "idCard": "[{\"path\":\"http:\\/\\/demo.chofn.com:88\\/uploads\\/documents\\/2016\\/07\\/23\\/30f19e88bb6ffd72.jpg\",\"name\":\"sfz_fanmian.jpg\",\"size\":16312},{\"path\":\"http:\\/\\/demo.chofn.com:88\\/uploads\\/documents\\/2016\\/07\\/23\\/d87728941cc54e88.jpg\",\"name\":\"sfz_zhengmian.jpg\",\"size\":14428}]",
          "sort": 1
        }

# 交底书模板
clarificaitonbook={
        "id": "0",
        "name": "超凡专利交底书模板7-11",
        "hasProject": 1,
        "hasClarificaitonbook": 1,
        "hasPicture": 0,
        "remark": "",
        "bookFile": [bookFile],
        "otherFile": "",
        "isSubCheck": 1
}

# 发明人项模板
inventor =  {
          "id": "768",
          "customerId": "1957592",
          "inventorId": "40",
          "sort": "1",
          "firstInventor": "1",
          "name": "实用新型测试",
          "certificateID": "1",
          "certificateName": "身份证",
          "certificateNo": "511011198504211213",
          "publishName": "1",
          "countryId": "1",
          "country_name": "中国",
          "cardIds": [cardIdItem]
        }

