#coding=utf-8
''' 基础工具的集合'''
import os
import sys

def getModule(func):
    ''' 获取函数/方法所在文件名及路径
    '''
    #获取被注解函数/方法所属模块的文件夹绝对路径和模块名
    funcModule = sys.modules.get(func.__module__).__file__
    modulePath = os.path.dirname(funcModule)
    moduleName = os.path.basename(funcModule)
    return modulePath,moduleName

def format(strItem,encoding="unicode-escape"):
    ''' 将str中的unicode解析成中文，并返回字符串
    '''
    return strItem.decode(encoding).encode("utf-8")