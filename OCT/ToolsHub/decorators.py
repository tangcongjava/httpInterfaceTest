#coding=utf-8
''' 装饰器的集合'''
import os
import sys
import shlex
from .basicUtils import getModule

__author__="waynel.zhang"

def dataprovider(func):
    ''' 测试数据绑定装饰器
                   在测试用例方法/函数上使用该装饰器后，将自动绑定resource下对应的数据文件为其参数文件
                   如：测试用例testNormalLogin()在 testcase/patent/login/testLogin.py中,那么会自动
                   绑定resource/patent/login/testLogin.testNormalLogin.csv文件
                   
        Example use::
                    @dataprovider
                    def func():
                        func statement
    '''
    def wrapper(*args):
        #获取方法所在文件名及文件路径
        modulePath,moduleName = getModule(func)
        moduleName = moduleName.split(".")[0]
        #获取被注解函数/方法对应的测试数据,数据文件名为 模块名.方法名.csv
        dataFilePath = modulePath.replace("testcase","resource",1)
        dataFileName = '%s.%s.csv' % (moduleName,func.__name__)
        dataFile = os.path.join(dataFilePath,dataFileName)
#         print dataFile
        with open(dataFile) as f:
            count = 0
            for line in f:
                params = sepStr(line)
                #第一行为列属性描述，可以忽略
                if(count==0):
                    count += 1
                    continue
#                 try:
                func(*(tuple(params))) 
#                 except TypeError: #忽略参数错误提示
#                     pass
    return wrapper

def getData(func):
    ''' 获取方法对应的数据文件，返回list
                   方法对应的数据文件在resource下对应的目录
                   如：测试用例testNormalLogin()在 testcase/patent/login/testLogin.py中,那么将获取
        resource/patent/login/testLogin.testNormalLogin.csv文件中数据
    '''
    #获取被注解函数/方法所属模块的文件夹绝对路径和模块名
    funcModule = sys.modules.get(func.__module__).__file__
#         print funcModule
    modulePath = os.path.dirname(funcModule)
    moduleName = os.path.basename(funcModule).split(".")[0]
#         print moulePath,mouleName
    #获取被注解函数/方法对应的测试数据,数据文件名为 模块名.方法名.csv
    dataFilePath = modulePath.replace("testcase","resource",1)
    dataFileName = '%s.%s.csv' % (moduleName,func.__name__)
    dataFile = os.path.join(dataFilePath,dataFileName)
#         print dataFile
    with open(dataFile) as f:
        count = 0
        for line in f:
            params = sepStr(line)
            #第一行为列属性描述，可以忽略
            if(count==0):
                count += 1
                continue
            yield params 

def sepStr(input_str):
    '''以逗号分隔字符串，返回list
       引号内的逗号不会被分隔
    '''
    input_str = shlex.shlex(input_str.strip(),posix=True)
    input_str.whitespace = ","
    input_str.whitespace_split = True
    return list(input_str)

def loginDecorator(loginFunc):
    '''
    这个函数装修setup 中的login,实现动态的用户登录
    :param loginFunc:
    :return:
    '''
    def _deco(username,password,loginurl):
        loginFunc(username,password,loginurl)
    return  _deco

