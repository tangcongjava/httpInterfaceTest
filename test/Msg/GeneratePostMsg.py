# coding:utf-8
__author__ = 'angustang'
# 这是一个用于生成与后台进行数据交互的模块
import  ClarificationBook
import  BaseMsg
import  SignContract
from OCT.ToolsHub import  GenDatetime
class GenData(object):
    '''
    '''
    def __init__(self,inputData=None,itemsAndFee=None):
        self.inputData = inputData
        self.itemsAndFee = itemsAndFee
        pass
    def genJsonData(self,bizType=None,**kwargs):
        '''
        通过数据类型然后更改消息模块中的链来进行消息的自定义化
        :param bizType:业务类型
        0-------交底书上传和提交审核(因为交底书上传以及提交审核是一个动作)
        1--------签订标准合同
        2--------提交非标准合同
        3--------省级经理审核
        4--------代理中心审核
        5---------非标准合同签订
        6--------提交合同不带交底书
        7---------交底书提交去审核
        8---------审核员进行审核
        9---------交底书支持部审核
        10---------立案前编辑申请人信息
        100-------测试消息
        :return: 返回的是一个消息字典
        '''
        retData={}
        customerInfo=kwargs["customerInfo"]
        bailorInfo=kwargs["bailorInfo"]
        proposerInfo=kwargs["poroposerInfo"]
        contactInfo=kwargs["contactInfo"]
        inventorInfo=kwargs["inventorInfo"]
        if 0==bizType:#针对不同的业务返回不同的form_data传送数据
            #其实这里要是客户消息中的链与
            self.inputData["customerId"]=customerInfo["id"]
            self.inputData["customerName"]=customerInfo["name"]
            self.inputData["bailorId"]=bailorInfo["bailorId"]
            self.inputData["bailorWholeAddress"]=bailorInfo["bailorWholeAddress"]
            self.inputData["contactId"]=contactInfo["contactId"]
            self.inputData["money"]="9950"#合同总费用
            self.inputData["agencyFee"]="6000"#代理费
            self.inputData["additionalCharge"]="500"#额外的费用
            self.inputData["publicExpense"]="3450"#官费
            self.inputData["publicExpenseTitleCate"]="3"#官费名义类别,先写成3
            self.inputData["publicExpenseTitle"]="超凡志成"#官费名义名称,先写成这样
            self.inputData["remark"]=""#合同信息 这里先设置为空
            self.inputData["nextHandler"]="445"#如果是在新建合同的就上传交底书那么就是0，如果签订合同就是具体顾问的ID
            self.inputData["business"]=0
            self.inputData["tplType"]=0#合同新建类型，0代表代理
            self.inputData["items"]=[]
            self.inputData["contactMobile"]=contactInfo["contactMobile"]
            self.inputData["contactEmail"]=contactInfo["contactEmail"]
            self.inputData["contactTel"]=contactInfo["contactTel"]
            self.itemsAndFee["clarificaitonbook"]["name"]=u"接口测试"+GenDatetime.TimeHandler().getCurrentTime()
            self.itemsAndFee["proposer"][0]["proposerId"]=proposerInfo["proposerId"]
            self.itemsAndFee["inventor"][0]["inventorId"]=inventorInfo["customer_id"]
            self.itemsAndFee["inventor"][0]["name"]=inventorInfo["name"]
            self.itemsAndFee["operatorId"]=contactInfo["contactId"]#操作人ID就是联系人ID
            self.itemsAndFee["technologyContact"]["technologyContactId"]=contactInfo["contactId"]
            self.itemsAndFee["technologyContact"]["name"]=contactInfo["contactName"]
            self.itemsAndFee["technologyContact"]["mobile"]=contactInfo["contactMobile"]
            self.itemsAndFee["technologyContact"]["email"]=contactInfo["contactEmail"]
            self.inputData["items"].append(self.itemsAndFee)
            return  self.inputData
            pass
        elif 1==bizType:
            #生成标准合同签订信息
            signSrcMsg=kwargs["contractSignMsg"]
            self.inputData["contractId"]=signSrcMsg["contractId"]
            self.inputData["nextHandlerId"]=""
            self.inputData["postData"]["contractType"]=1
            return  self.inputData
            #其它的数据后续再添加
        elif 2==bizType:
            #生成非标合同签订信息
            signSrcMsg=kwargs["contractSignMsg"]
            self.inputData["contractId"]=signSrcMsg["contractId"]
            self.inputData["nextHandlerId"]=signSrcMsg["nextHandlerId"]
            self.inputData["postData"]["contractType"]=2
            return  self.inputData
        elif 3==bizType:
            #生成省级经理审核信息
            ManageCheckMsg=kwargs["ManagerCheckMsg"]
            self.inputData["id"]=ManageCheckMsg["contractId"]
            self.inputData["contractId"]=ManageCheckMsg["contractId"]
            self.inputData["isSubmit"] = ManageCheckMsg["isSubmit"]
            self.inputData["nextHandlerId"] = ManageCheckMsg["nextHandlerId"]
            return  self.inputData
        elif 4==bizType:
            #生成代理中心审核信息
            AgentCheckMsg=kwargs["agentCheckMsg"]
            self.inputData["id"]=AgentCheckMsg["id"]
            self.inputData["result"] = AgentCheckMsg["result"]
            return self.inputData
        elif 5== bizType:
            noStandardCheckMsg=kwargs["FinalNoStandardCheckMsg"]
            self.inputData["contractId"]=noStandardCheckMsg["contractId"]
            return  self.inputData
        elif 6 == bizType:
            self.inputData["customerId"]=customerInfo["id"]
            self.inputData["customerName"]=customerInfo["name"]
            self.inputData["bailorId"]=bailorInfo["bailorId"]
            self.inputData["bailorWholeAddress"]=bailorInfo["bailorWholeAddress"]
            self.inputData["contactId"]=contactInfo["contactId"]
            self.inputData["money"]="10950"#合同总费用
            self.inputData["agencyFee"]="6000"#代理费
            self.inputData["additionalCharge"]="1500"#额外的费用
            self.inputData["publicExpense"]="3450"#官费
            self.inputData["publicExpenseTitleCate"]="3"#官费名义类别,先写成3
            self.inputData["publicExpenseTitle"]="超凡志成"#官费名义名称,先写成这样
            self.inputData["remark"]=""#合同信息 这里先设置为空
            self.inputData["nextHandler"]="445"#如果是在新建合同的就上传交底书那么就是0，如果签订合同就是具体顾问的ID
            self.inputData["business"]=0
            self.inputData["tplType"]=0#合同新建类型，0代表代理
            self.inputData["items"]=[]
            self.inputData["contactMobile"]=contactInfo["contactMobile"]
            self.inputData["contactEmail"]=contactInfo["contactEmail"]
            self.inputData["contactTel"]=contactInfo["contactTel"]
            # self.itemsAndFee["clarificaitonbook"]["name"]=u"接口测试"+GenDatetime.TimeHandler().getCurrentTime()
            self.itemsAndFee["inventor"][0]["customerId"]=customerInfo["id"]
            self.itemsAndFee["proposer"][0]["proposerId"]=proposerInfo["proposerId"]
            self.itemsAndFee["inventor"][0]["inventorId"]=inventorInfo["id"]
            self.itemsAndFee["inventor"][0]["name"]=inventorInfo["name"]
            self.itemsAndFee["inventor"][0]["certificateID"]=inventorInfo["card_type_id"]
            self.itemsAndFee["inventor"][0]["certificateName"]=inventorInfo["card_type"]
            self.itemsAndFee["inventor"][0]["certificateNo"]=inventorInfo["cardno"]
            self.itemsAndFee["inventor"][0]["firstInventor"]=inventorInfo["is_first_inventor"]
            self.itemsAndFee["inventor"][0]["countryId"]=inventorInfo["country_id"]
            self.itemsAndFee["inventor"][0]["country_name"]=inventorInfo["country_name"]
            self.itemsAndFee["inventor"][0]["cardIds"][0]["filename"]=inventorInfo["serializeinfo"]["attachment"]["idCard"][0]["filename"]
            self.itemsAndFee["inventor"][0]["cardIds"][0]["filesize"]=inventorInfo["serializeinfo"]["attachment"]["idCard"][0]["filesize"]
            self.itemsAndFee["inventor"][0]["cardIds"][0]["filetype"]=inventorInfo["serializeinfo"]["attachment"]["idCard"][0]["filetype"]
            self.itemsAndFee["inventor"][0]["cardIds"][0]["id"]=inventorInfo["serializeinfo"]["attachment"]["idCard"][0]["id"]
            self.itemsAndFee["operatorId"]=contactInfo["contactId"]
            self.itemsAndFee["technologyContact"]["technologyContactId"]=contactInfo["contactId"]
            self.itemsAndFee["technologyContact"]["name"]=contactInfo["contactName"]
            self.itemsAndFee["technologyContact"]["mobile"]=contactInfo["contactMobile"]
            self.itemsAndFee["technologyContact"]["email"]=contactInfo["contactEmail"]
            self.inputData["items"].append(self.itemsAndFee)
            return  self.inputData
        elif 7 == bizType:
            clfEditMsg = kwargs["clfEditMsg"]
            self.inputData["id"]=clfEditMsg["id"]
            self.inputData["name"]=clfEditMsg["name"]
            return  self.inputData
        elif 8 == bizType:
            #交底书审核
            clfCheckMsg = kwargs["clfCheckMsg"]
            self.inputData["id"]=clfCheckMsg["clfBookId"]
            return self.inputData
        elif 9== bizType:
            #交底书上级经理审核
            clfManagerCheckMsg = kwargs["pclfManagerCheckMsg"]
            self.inputData["id"]=clfManagerCheckMsg["clfBookId"]
            return  self.inputData
        elif 10 == bizType:
            #编辑客户信息
            operatorData =kwargs["operatorData"]
            technologycontactData = kwargs["technologycontactData"]
            #更新客户信息
            self.inputData["proposer"][0]["proposerId"]=proposerInfo["proposerId"]
            self.inputData["proposer"][0]["proposerCountryId"]=proposerInfo["proposerCountryId"]
            self.inputData["proposer"][0]["proposerProvinceId"]=proposerInfo["proposerProvinceId"]
            self.inputData["proposer"][0]["proposerCityId"]=proposerInfo["proposerCityId"]
            self.inputData["proposer"][0]["proposerAreaId"] = proposerInfo["proposerAreaId"]
            self.inputData["proposer"][0]["proposerCardNo"]=proposerInfo["proposerCardNo"]
            self.inputData["proposer"][0]["proposerEnName"]=proposerInfo["proposerEnName"]
            self.inputData["proposer"][0]["proposerZipcode"]= proposerInfo["proposerZipcode"]
            self.inputData["proposer"][0]["proposerAddress"]=proposerInfo["proposerAddress"]
            self.inputData["proposer"][0]["proposerEnAddress"]=proposerInfo["proposerEnAddress"]
            self.inputData["proposer"][0]["licenseTranslate"]=proposerInfo["licenseTranslate"]
            self.inputData["proposer"][0]["license"]=proposerInfo["license"]
            self.inputData["proposer"][0]["officialSeal"]=proposerInfo["officialSeal"]
            self.inputData["proposer"][0]["idCard"]=proposerInfo["idCard"]
            self.inputData["proposer"][0]["sort"]=int(proposerInfo["sort"])
            self.inputData["proposer"][0]["proposerClass"]=proposerInfo["proposerClass"]
            self.inputData["proposer"][0]["proposerWholeAddress"]=proposerInfo["proposerWholeAddress"]
            self.inputData["inventor"][0]["id"]=inventorInfo["id"]
            self.inputData["inventor"][0]["customerId"]=operatorData["customerId"]
            self.inputData["inventor"][0]["inventorId"]=inventorInfo["inventorId"]
            self.inputData["inventor"][0]["sort"]=inventorInfo["sort"]
            self.inputData["inventor"][0]["firstInventor"]=inventorInfo["firstInventor"]
            self.inputData["inventor"][0]["name"]=inventorInfo["name"]
            self.inputData["inventor"][0]["certificateID"]=inventorInfo["certificateID"]
            self.inputData["inventor"][0]["certificateName"]=inventorInfo["certificateName"]
            self.inputData["inventor"][0]["certificateNo"]=inventorInfo["certificateNo"]
            self.inputData["inventor"][0]["publishName"]=inventorInfo["publishName"]
            self.inputData["inventor"][0]["countryId"]=inventorInfo["countryId"]
            self.inputData["inventor"][0]["country_name"]=inventorInfo["country_name"]
            self.inputData["inventor"][0]["cardIds"][0]=inventorInfo["serializeinfo"]["attachment"]["idCard"][0]
            self.inputData["operator"]["operatorId"]=operatorData["id"]
            self.inputData["technologyContact"]["id"]=technologycontactData["id"]
            self.inputData["technologyContact"]["technologyContactId"]=technologycontactData["contractId"]
            self.inputData["technologyContact"]["name"]=technologycontactData["name"]
            self.inputData["technologyContact"]["mobile"] = technologycontactData["mobile"]
            self.inputData["technologyContact"]["email"] = technologycontactData["email"]
            return  self.inputData
        elif 100==bizType:
            return  self.inputData
if __name__ == '__main__':
    genData = GenData(ClarificationBook.ClarificationBookUpload,itemsAndFee=BaseMsg.itemsAndFee)


