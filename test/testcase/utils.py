#coding=utf-8
'''专利系统工具集，如各种setup，teardown等'''

from test.testcase.login.TestLogin import login,logout

__author__ = "waynel.zhang"

def setup_login(username, password, myhttp):
    '''登录的setup方法,登录系统
            配合@with_setup使用
    :param username   登录用户名
    :param password   登录密码
    :param myhttp     MyHttp实例
    :return function
    
    example:
        @with_setup(setup=setup_login(username, password, myhttp))
    '''
    def wrapper():
        login(username, password, myhttp)
    return wrapper
    
def teardown_logout(myhttp):
    '''登录的teardown方法，退出系统
            配合@with_setup使用
    :param myhttp     MyHttp实例
    
    example:
        @with_setup(teardown=teardown_logout(myhttp))
    '''
    def wrapper():
        logout(myhttp)
    return wrapper

  