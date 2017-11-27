# -*- coding: utf-8 -*-
from watchdog import Specialpop
from senddata import Sendmail
from readfile import Readfile
from datetime import datetime
from time import sleep


while True:

	heute=int(datetime.now().timestamp())
	sleep(20)
	rec=Specialpop()
	mailtime=int(rec.getdata()[-1]['Date'])
	mailsubject=rec.getdata()[-1]['Subject']
	mailbody=rec.getdata()[-1]['Body']
	#print(mailtime,mailsubject)
	rec.quityou()
	if heute<=mailtime:
		print('收到邮件')
		if mailsubject=='数据请求':
			print('返回数据')
			file=Readfile(mailbody)
			sed=Sendmail()
			sed.makemail(file.getdata())
			sed.sendmail()
			sed.sendquit()

		
			
