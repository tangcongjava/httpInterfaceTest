# coding:utf-8
# __author__ = 'Administrator'
from redmine import Redmine
def createBug(bugmsg="test"):
    redmine = Redmine("http://pms.chofn.net:24",username="angustang",password="5510806a",version="2.4.2",
                  impersonate="paul")
    chaofan = redmine.project.get("chofnneu")
    redmine.issue.create(project_id='chofnneu',subject="autotest dmeo",tracker_id=1,description=bugmsg,
                             category_id=35,assigned_to_id =152,custom_fields=[{"id":9,"value":u'一般'},{"id":16,"value":u"系统集成阶段"},{"id":21,"value":u'合同管理'}],
                             fixed_version_id=149)
if __name__ == '__main__':
    createBug("it is a bug")