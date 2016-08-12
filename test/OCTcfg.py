# coding:utf-8
'''
这个文件是OCT接口测试项目的配置文件，所有配置信息依据组件采取python字典形式进行配置如：
db ={
  "host"="127.0.0.1",
  "port"="3306",
    "user"="administrator",
    "password"="5510806a"
}
__author__ = 'Administrator'

'''

URL_PATENT_BASE = "http://patent.test.chofn.net"

ERROR_PATENT_NOT_LOGIN = "先登录才能继续操作"

isLoggingOpen=True
consultant = {
    "username":"elva",
    "password":"zz123asd",
    "customerName":"angustang"
}

pluginSwitch={
    "email":1,
    "redmin":1,
}
email ={
    "login_user":"angus.tang@chaofan.wang",
    "login_pswd":"@WSXcde3",
    "host":"smtp.mxhichina.com",
    "port":25,
    "from_addr":"angus.tang@chaofan.wang",
    "to_addrs":["angus.tang@chaofan.wang","3442462293@qq.com"]
}
redmine={
    "user":"angustang",
}
DBcfg={
    "username":"patentsystem",
    "password":'123456',
    "host":'192.168.0.192',
    "port":3306,
    "dbname":'patentsystem'
}
# the user cfg of flow
# 目前把流程处理人硬编码，以后再想办法动态获取下一节点处理人。这里写是通过查询数据库表中的处理人ID来进行的
contractFlowUser={
    3:"445",# elva发起合同    groupid ===1 再通过ps_group_user查询对应user下的人
    4:"",#团队经理审核 groupid ===3
    5:"2549",# belly省级经理审核 groupid ====4
    6:"21",#lulu代理中心审核 groupid  ====5
    7:"445",#elva签订合同    groupid ======1`
}
clarificaitonBookCheckUser={

}

