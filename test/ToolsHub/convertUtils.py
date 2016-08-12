#coding=utf-8
'''接口返回结果转换工具集'''

def convertToProposerList(resp):
    ''' 将获取申请人列表返回结果转换为标准申请人列表对象
    
            注意： 使用时，如果一个事项中有多个申请人，需要修改 sort，第一个申请人为1， 第二个为2,第三个为3... 
    '''
    proposerList = []
    for data in resp["body"]["data"]:
        proposer = {}
        proposer["proposerId"] = data["proposerId"]
        proposer["proposerCountryId"] = data["proposerCountryId"]
        proposer["proposerProvinceId"] = data["proposerProvinceId"]
        proposer["proposerCityId"] = data["proposerCityId"]
        proposer["proposerAreaId"] = data["proposerAreaId"]
        proposer["proposerCardNo"] = data["proposerCardNo"]
        proposer["proposerEnName"] = data["proposerEnName"]
        proposer["proposerZipcode"] = data["proposerZipcode"]
        proposer["proposerAddress"] = data["proposerAddress"]
        proposer["proposerEnAddress"] = data["proposerEnAddress"]
        proposer["officialSeal"] = str(data["officialSeal"])
        proposer["license"] = str(data["license"])
        proposer["licenseTranslate"] = str(data["licenseTranslate"])
        proposer["idCard"] = str(data["idCard"])        
        proposer["id"] = "0"
        #注意： 使用时，如果一个事项中有多个申请人，需要修改 sort，第一个申请人为1， 第二个为2,第三个为3...
        proposer["sort"] = "1"
        
        proposerList.append(proposer)        
    return proposerList

def convertToInventorList(resp):
    ''' 将获取发明人列表返回结果转换为标准发明人列表对象

            注意，使用时，如果一个事项中存在多个发明人时，需要修改sort,第一发明是1，第二是2，第三是3...
             同时，只有第一发明人firstInventor才为1，其余均为0
    '''
    map_certificateName_certificateID = { 
           u"身份证" : "1",
           u"军官证" : "2",
           u"护照" : "3",
           u"其他" : "10"
           }
    inventorList = []
    for data in resp["body"]["data"]["rows"]:
        inventor = {}
        inventor["customerId"] = data["customer_id"]
        inventor["inventorId"] = data["id"]
        inventor["name"] = data["name"]
        inventor["certificateName"] = data["card_type"]
        inventor["certificateID"] = map_certificateName_certificateID[data["card_type"]]
        inventor["certificateNo"] = data["cardno"]
        inventor["countryId"] = data["country_id"]
        inventor["country_name"] = data["country_name"]
        inventor["cardIds"] = data["serializeinfo"]["attachment"]["idCard"]
        inventor["id"] = "0"
        #注意，使用时，如果一个事项中存在多个发明人时，需要修改sort,第一发明是1，第二是2，第三是3...
        inventor["sort"] = "1"
        #注意，只有第一发明人firstInventor才为1，其余均为0
        inventor["firstInventor"] = "1"    
        inventor["publishName"] = "1"
        inventorList.append(inventor)
    
    return inventorList
        