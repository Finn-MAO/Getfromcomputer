# -*- coding: utf-8 -*-
import os
import docx


def gettxt(path):
	print('是text')
	with open(path,'r') as fp:
		data=fp.readlines()
	data=''.join(data)
	return data
	
def getword(path):
	document=docx.Document(path)
	docText = '\r\n'.join([paragraph.text for paragraph in document.paragraphs])
	return(docText)


def getexcel(path):
	pass

class Readfile(object):

	def __init__(self,path):
		self.path=path
	def getdata(self):
		firstname,extendname=os.path.splitext(self.path)
		#print(firstname,extendname)
		if extendname=='.txt':
			data=gettxt(self.path)
		elif extendname=='.doc' or '.docx' :
			data=getword(self.path)
		elif extendname=='.xls' or '.xlsx':
			data=getexcel(self.path)
		return data

# a=Readfile(r'C:\Users\Cancer Mao\Desktop\通过邮件远程从电脑中取东西\test.docx')
# print(a.getdata())