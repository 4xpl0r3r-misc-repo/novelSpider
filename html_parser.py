# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re,urllib.parse

class htmlParser:

	def getNextUrl(self,url,parser):
		nextUrl=parser.find('a',id='pager_next')
		nextUrl=nextUrl['href']
		return nextUrl

	def getData(self,url,parser):
		resData={}
		#title
		titleNode=parser.find('div',class_='bookname').find('h1')
		resData['title']=titleNode.get_text()
		#text
		summaryNode=parser.find('div',id='content')
		resData['text']=summaryNode.get_text()
		return resData

	def parse(self,url,content):
		if(url is None or content is None):
			return
		print("[info]","开始解析:%s"%url)
		soupparser=BeautifulSoup(content,'html.parser',from_encoding='utf-8')
		nextUrl=self.getNextUrl(url,soupparser)
		htmlContent=self.getData(url,soupparser)
		print("[info]","解析完成:%s"%url)
		return nextUrl,htmlContent