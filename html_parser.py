# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re,urllib.parse
import logging

class ParseException(Exception):
	def __init__(self, arg):
		super(ParseException, self).__init__()
		self.str=arg

	def __str__(self):
		return self.str
		

class htmlParser:
	def __init__(self):
		self.parser=None

	def getNewUrls(self,content):
		try:
			self.parser=BeautifulSoup(content,'lxml')
			newUrls=set()
			links=self.parser.find_all('a',href=re.compile(r"/item/[^\?]+"))
			for link in links:
				newUrl=link['href']
				newFullUrl=urllib.parse.urljoin(url,newUrl)
				newUrls.add(newFullUrl)
			if(len(newUrls)==0 or newUrls is None):
				logging.warn("未获取到Url:%s"%url)
			return newUrls
		except Exception as e:
			raise ParseException(e)

	def getData(self,url,content):
		try:
			self.parser=BeautifulSoup(content,'lxml')
			resData={}
			#url
			resData['url']=url
			#title
			titleNode=self.parser.find('dd',class_=r'lemmaWgt-lemmaTitle-title').find('h1')
			resData['title']=titleNode.get_text()
			#summary
			summaryNode=self.parser.find('div',class_=r'lemma-summary')
			resData['summary']=summaryNode.get_text()
			return resData
		except Exception as e:
			raise ParseException(e)