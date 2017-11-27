# -*- coding: utf-8 -*-
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib#smtplib负责发送
#email模块构造邮件
from email.mime.text import MIMEText

#_format_addr()来格式化一个邮件地址
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
	
class Sendmail(object):
	def __init__(self):
		self.from_addr = 'finn_mao@163.com'
		self.password = 'maoliyang1996512'
		self.to_addr = '384674734@qq.com'
		self.smtp_server = 'smtp.163.com'
		self.server = smtplib.SMTP(self.smtp_server, 25)
		self.server.login(self.from_addr,self.password)	
		
	def makemail(self,text):
		self.msg = MIMEText(text, 'plain', 'utf-8')
		self.msg['From'] = _format_addr('电脑 <%s>' % self.from_addr)
		self.msg['To'] = _format_addr('finn_mao <%s>' % self.to_addr)
		self.msg['Subject'] = Header('要求数据', 'utf-8').encode()

	def sendmail(self):
		self.server.sendmail(self.from_addr, [self.to_addr], self.msg.as_string())
	def sendquit(self):	
		self.server.quit()

# a=Sendmail()
# a.makemail('maoliyang')
# a.sendmail()
# a.sendquit()
		
