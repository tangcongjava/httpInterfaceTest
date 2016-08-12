# coding:utf-8
__author__ = 'angustang'
import  time
class TimeHandler(object):
    def __init__(self):
        pass
    
    @staticmethod
    def getCurrentTime():
        '''
        生成YYYY-MM-D-m-s的当前时间
        :return:
        '''
        now = time.localtime(time.time())
        return time.strftime("%Y-%m-%d %H:%M:%S",now)
        pass
    def getLogFileName(self):
        now = time.localtime(time.time())
        return time.strftime("%Y%m%d")+".log"
    
    @staticmethod
    def getStrCurrentTime():
        ''' 将当前时间生成YYYYMMDDHHMMSS格式的字符串
        '''
        return time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    
if __name__ == '__main__':
    timehandler = TimeHandler()
    print timehandler.getCurrentTime()
    print TimeHandler.getStrCurrentTime()