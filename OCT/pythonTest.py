# coding:utf-8
__author__ = 'angustang'
class TestDemo(object):
    a=25
    def __init__(self,b):
        self.b = b
        pass
    @staticmethod
    def smethod():
        print 'a+b is plus'
        pass
    @classmethod
    def cmethod(cls):
        print 'cls is '+ str(cls)
        print cls.a
    def inmethod(self):
        print 'self is '+str(self)
        print self.__class__.a
if __name__ == '__main__':
    obj = TestDemo(25)
    obj.cmethod()
    obj.inmethod()

