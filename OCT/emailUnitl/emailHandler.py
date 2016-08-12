# coding:utf-8
# __author__ = 'angustang'
import smtplib

from email.mime.text import MIMEText
from email.header import Header
from email.utils import COMMASPACE,formatdate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.application import MIMEApplication
import mimetypes
import  time
import  pyh
import  os
import  datetime

class MyEmail():
    def __init__(self,sendFrom,sendTo,username,passowrd,smtpSrv,port):
        self.sendFrom = sendFrom
        self.sendTo = sendTo
        self.username = username
        self.password = passowrd
        self.smtpSrv =  smtpSrv
        self.port = port
        self.smtp = smtplib.SMTP(self.smtpSrv,self.port)
    def login(self):
        self.smtp.login(self.username,self.password)
        pass
    def sendMail(self,mail_subject,mail_content,attachment_path_set):
        msg = MIMEMultipart()
        msg['From'] = self.sendFrom
        msg['To'] = COMMASPACE.join(self.sendTo)
        msg['Date']=formatdate(localtime=True)
        # 注意，这里的msg['To']只能为逗号分隔的字符串，形如 'sdxx@163.com', 'xdflda@126.com'
        msg['Subject'] = mail_subject

        # 添加邮件内容
        content = MIMEText(mail_content, _charset='utf-8')
        # 说明，这里_charset必须为gbk，和# -*- coding:GBK -*- 保持一直，否则邮件内容乱码

        msg.attach(content)

        for attachment_path in attachment_path_set:
            if os.path.isfile(attachment_path): # 如果附件存在
                type, coding = mimetypes.guess_type(attachment_path)
                if type == None:
                    type = 'application/octet-stream'

                major_type, minor_type = type.split('/', 1)
                with open(attachment_path, 'r') as file:
                    if major_type == 'text':
                        attachment = MIMEText(file.read(), _subtype=minor_type, _charset='utf-8')
                    elif major_type == 'image':
                        attachment = MIMEImage(file.read(),  _subtype=minor_type)
                    elif major_type == 'application':
                        attachment = MIMEApplication(file.read(), _subtype=minor_type)
                    elif major_type == 'audio':
                        attachment = MIMEAudio(file.read(), _subtype=minor_type)

                # 修改附件名称
                attachment_name = os.path.basename(attachment_path)
                attachment.add_header('Content-Disposition', 'attachment', filename =  attachment_name)
                # 说明：这里的('gbk', '', attachment_name)解决了附件为中文名称时，显示不对的问题

                msg.attach(attachment)

        # 得到格式化后的完整文本
        full_text = msg.as_string()

        # 发送邮件
        self.smtp.sendmail(self.sendFrom, self.sendTo, full_text)
        pass

    def quit(self):
        self.smtp.quit()

