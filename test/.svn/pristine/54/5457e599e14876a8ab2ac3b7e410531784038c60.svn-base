# coding:utf-8
# __author__ = 'angustang'
import  os,nose,sys,shutil

def execute(path=os.getcwd()):
    '''执行test/testcase下所有测试用例
        日志输出到log文件夹patent.html文件
    '''
    output = os.path.join(path,'log','patent.html')
    noseArg=['-v','-s','-w',os.path.join(path,'testcase'),\
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
    execute()
        

