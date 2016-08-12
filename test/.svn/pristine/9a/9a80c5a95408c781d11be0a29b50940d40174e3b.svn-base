#coding=utf-8
'''校验方法工具集'''

def basicSuccessCheck(resp):
    ''' 最基础的成功返回结果校验
    '''
    assert resp["header"]["code"] == 104
    assert resp["body"]["status"] == 1
    