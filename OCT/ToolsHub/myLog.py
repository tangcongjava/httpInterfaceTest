# coding:utf-8
__author__ = 'angustang'
import  logging,os,sys,time
from .GenDatetime import  TimeHandler
from OCT import OCTcfg
from .basicUtils import format

class MyLogging(object):
    def __init__(self,logPath=None):
        logfilename =  TimeHandler().getLogFileName()
        if not logPath:
            logPath =  os.path.dirname(__file__).replace("ToolsHub","log")
        if not  os.path.exists(logPath):
            os.mkdir(logPath)
        logging.basicConfig(level=logging.DEBUG,
                            format=('%(asctime)s-------%(message)s'),
                            datefmt='%Y-%m-%d %H:%M:%S',
                            filename=os.path.join(logPath,logfilename),
                            filemode='a')
        
    def debug(self,*msg):
        if OCTcfg.isLoggingOpen:
            len_msg = len(msg)
            if len_msg == 1:
                logging.debug(*msg)
            elif len_msg == 2:
                logging.debug(msg[0] + format(str(msg[1])))
        else:
            pass