# httpInterfaceTest
http interface test 
1.该工程实现了web http协议的接口测试。
2.OCT目录是底层的http接口库，实现了post,get,uploadfile常用的http接口测试,以及mysql数据库的操作，连接redmine Bug管理系统，以及测试报告的自动
发送。
3.OCThttp协议的实现主要使用了urllib2.
4.testcase目录为各模块的接口测试用例。使用python ddt模块实现了数据参数化，测试用例的编写使用的是unittest,测试用例的执行是用nosetest.
5.该工程可以复用，且可以与CI联合使用达到自动化测试的功能。
6.开发者可以在现在基础上添加自己所需的功能。
