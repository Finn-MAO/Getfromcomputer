# -*- coding: utf-8 -*-

from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import poplib
from datetime import datetime

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value
	
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

def print_info(msg,indent=0):
	a={}
	for header in ['From', 'To', 'Subject','Date']:
		value = msg.get(header, '')  
		if value:
			if header=='Subject' or 'Data':
				value = decode_str(value)
				if header=='Date':
					value=datetime.strptime(value[0:31],'%a, %d %b %Y %H:%M:%S %z').timestamp()
			else:
				hdr, addr = parseaddr(value)
				name = decode_str(hdr)
				value = (name, addr)
		a[header]=value
		
	if (msg.is_multipart()):
		parts = msg.get_payload()#得到msg中所有类型的数据list
		for n, part in enumerate(parts):
			content_type = part.get_content_type()
			if content_type=='text/plain':
				content = part.get_payload(decode=True)
				charset = guess_charset(part)
				if charset:
					content = content.decode(charset)
				a['Body']=content
	return a

	
class Specialpop(object):

	def __init__(self,addr='finn_mao@163.com',password='maoliyang1996512',server='pop.163.com'):
		self.email=addr
		self.password=password
		self.pop3_server=server
		self.server = poplib.POP3(self.pop3_server)
		self.server.user(self.email)
		self.server.pass_(self.password)
		
	def getdata(self):
		a=[]
		resp, mails, octets = self.server.list()
		for index in range(1,len(mails)+1):#index代表最后一封邮件，若要全拿下来循环至index=1
			resp, lines, octets = self.server.retr(index)
			msg_content = b'\r\n'.join(lines).decode('utf-8')
			msg = Parser().parsestr(msg_content)
			a.append(print_info(msg))
		return a
	
	def quityou(self):
		self.server.quit()
	def deleteyou(self,index):
		self.server.dele(index)
		
# a=Specialpop()
# print(a.getdata()[-1])
# a.quityou()