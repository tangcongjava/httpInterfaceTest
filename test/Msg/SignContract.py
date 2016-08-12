# coding:utf-8
__author__ = 'angustang'
#非标准合同签订信息,给团队经理审核的
SignNonStandardContractMsg={
  "contractId": "26",#合同ID
  "nextHandlerId": "2549",#下一处理人ID,如果是标准合同签订，这里是空字符串
  "handleResult": 2,#本次节点处理结果.1代表标准合同处理，2代表非标准合同。
  "type": "1",#代理类型都是1
  "postData": {
    "contractType": 2,#合同类型 1代表标准合同，2代表非标准合同
    "nonStandardContractFile": "[{\"file_no\":\"A00113325\",\"file_name\":\"非标准委托合同 .pdf\"}]",#这个代表的是合同信息
    "contractFile": "",
    "otherFile": "",
    "proxyFile": "",
    "reduceFile": "",
    "comfirmFile": "",
    "transferFile": ""
  }
}
#非标合同最终签订
FinalNoStandarCheckMsg={
  "contractId": "155",
  "handleResult": 2,
  "type": "2",
  "postData": {
    "contractType": 2,
    "nonStandardContractFile": [

    ],
    "contractFile": "[{\"file_no\":\"A00113836\",\"file_name\":\"委托合同.pdf\"}]",
    "otherFile": "",
    "proxyFile": "",
    "reduceFile": "",
    "comfirmFile": "",
    "transferFile": ""
  }
}
#以下是标准合同的签订消息,后续还要处理一下对标准合同内容的添加,标准合同签订后，生成案子，且生成付款信息
SignStandardContractMsg={
  "contractId": "96",
  "nextHandlerId": "",#标准合同签订不需要下一节点处理人
  "handleResult": 1,
  "type": "1",
  "postData": {
    "contractType": 1,#代表标准合同
    "nonStandardContractFile": [

    ],
    "contractFile": "[{\"file_no\":\"A00113611\",\"file_name\":\"委托合同.pdf\"}]",#标准合同签订
    "otherFile": "",
    "proxyFile": "",
    "reduceFile": "",
    "comfirmFile": "",
    "transferFile": ""
  }
}
