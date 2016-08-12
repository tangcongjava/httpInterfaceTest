# coding:utf-8
# __author__ = 'angustang'
import  MySQLdb
from nose.tools import eq_
from OCT.OCTcfg import DBcfg

class sqlCheck(object):
    def __init__(self,dbConf=None,host=None,user=None,pswd=None,dbname=None,port=None):
        try:
            if dbConf:
                self.connection = MySQLdb.connect(host=dbConf["host"],
                                              user=dbConf["username"],
                                              passwd=dbConf["password"],
                                              db=dbConf["dbname"],
                                              port=dbConf["port"],
                                              charset="utf8")
            else:              
                self.connection = MySQLdb.connect(host=host,
                                              user=user,
                                              passwd=pswd,
                                              db=dbname,
                                              port=port,
                                              charset="utf8")
        except Exception,e:
            if e.args[0] == 2003:
                raise  Exception(e.args[1])
            else:
                raise  Exception(e.args)
        self.cursor=self.connection.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        
    def getAllRecode(self,sql):
        '''
        依据sql语句，返回所有的数据库记录
        :param sql:
        :return:
        '''
        try:
            count = self.cursor.execute(sql)
            if not count:
                return  None
            else:
                row = self.cursor.fetchall()
                return  row
        except Exception,e:
            if e.args[0] == 1146:
                raise  Exception("table not exist" )
            self.clear()
            
    def getConsulantId(self,ConsulantName):
        sql = "select id from ps_user as a where a.userName = '%s'" % ConsulantName
        print sql
        try:
            self.cursor.execute(sql)
            row = self.cursor.fetchall()
        except Exception,e:
            print e.args[1]
            self.clear()
        return  row[0]["id"]
    def clear(self):
        self.cursor.close()
        self.connection.close()
        
    def checker(self,keyMap,expData,actData):
        ''' 根据keyMap校验expData和actData中值是否相等
        usage:
        :param keyMap 需要校验的实际值和期望值中key的映射，字典类型，其key为实际值中key，value为
                      期望结果中的key的元组或者某一具体的期望值
        :param expData 实际值，字典类型
        :expData actData 期望值，字典类型
        :return 
        
        exaples:
        expData = {"data":{"contactId":123}, "code": "4"}
        actData = {"id": 123, "code":4, "status": "5"}
                    那么如果需要校验actData中的全部值，可以设置keyMap如下：
        keyMap = {"id":("data","contactId"), "code":"code", "status": "5"}
        
        '''
        for keyInActData in keyMap:
            # 先找到对应的expData的值
            expValue = expData            
            # 检查keyMap中值类型，如果为元组，那么值即为expData中的key;如果不是，那么就是具体的值
            value = keyMap[keyInActData]
            if isinstance(value, tuple):
                for vKey in value:
                    expValue = expValue[vKey]
            elif value == keyInActData:
                expValue = expValue[value]
            else:
                expValue = value
            # 设置实际值
            actValue = actData[keyInActData]
            # 将实际值和期望值的类型同步一致
            tp = type(actValue)
            # 如果actValue是unicode,转换为str后再比较
            if tp is unicode:
                actValue = actValue.encode("utf-8")
                # 同时也将expValue转换为str
                if type(expValue) is unicode:
                    expValue = expValue.encode("utf-8")
                else:
                    expValue = str(expValue)
            else:    
                expValue = tp(expValue)
            # 进行相等校验
            eq_(actValue,expValue,"%s不正确，期望值为：%s，实际值为：%s" % (keyInActData,expValue,actValue))
                              
if __name__ == '__main__':
#     sql = "select * from ps_contract"
#     print sqlCheck(host=DBcfg.get("host"),
#                    user=DBcfg.get("username"),
#                    pswd=DBcfg.get("password"),
#                    dbname=DBcfg.get("dbname"),
#                    port=DBcfg.get("port")).getAllRecode(sql)
    actData = {"a":1,"b":2,"f":5,"g":"cbd","h":5}
    expData = {"c":{"d":1,"e":[2,3]},"f":"5"}
    keyMap = {"a":("c","d"),"b":("c","e",0),"f":"f","g":"cbd","h":5}
    dbconn = sqlCheck(DBcfg)
    dbconn.checker(keyMap, expData, actData)

