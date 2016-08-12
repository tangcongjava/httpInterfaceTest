# coding:utf-8
# __author__ = 'angustang'
import  os,nose,sys,shutil

def execute(systemName,path=os.getcwd()):
    '''执行systemName所属系统的所有测试用例
    systemName为 test/testcase下各文件夹名
        日志输出到log文件夹对应的systemName.index文件
    '''
    output = os.path.join(path,'log',systemName+'.html')
    noseArg=['-v','-s','-w',os.path.join(path,'test','testcase',systemName),\
             '--with-html','--html-file=%s' % output]
    assert nose.run(argv=noseArg)
    
    #处理文件，将ascii转换为中文
    tmp = os.path.join(path,'log','tmp.html')
    with open(output) as f:
        with open(tmp,'w') as f2:
            for line in f:
                f2.write(line.decode("string-escape"))
    os.remove(output)
    shutil.move(tmp, output)
    
if __name__ == '__main__':
    param_len = len(sys.argv)
    if param_len == 1:
        execute("patent")
    else:
        execute(sys.argv[1])
        

