# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re,urllib.parse

class htmlParser:

	def getNewUrls(self,url,parser):
		newUrls=set()
		links=parser.find_all('a',href=re.compile(r"/item/[^\?]+"))
		for link in links:
			newUrl=link['href']
			newFullUrl=urllib.parse.urljoin(url,newUrl)
			newUrls.add(newFullUrl)
		if(len(newUrls)==0 or newUrls is None):
			print("[warn]","未获取到Url:%s"%url)
		return newUrls

	def getData(self,url,parser):
		resData={}
		#url
		resData['url']=url
		#title
		titleNode=parser.find('dd',class_=r'lemmaWgt-lemmaTitle-title').find('h1')
		resData['title']=titleNode.get_text()
		#summary
		summaryNode=parser.find('div',class_=r'lemma-summary')
		resData['summary']=summaryNode.get_text()
		return resData

	def parse(self,url,content):
		if(url is None or content is None):
			return
		print("[info]","开始解析:%s"%url)
		soupparser=BeautifulSoup(content,'html.parser',from_encoding='utf-8')
		newUrls=self.getNewUrls(url,soupparser)
		htmlContent=self.getData(url,soupparser)
		print("[info]","解析完成:%s"%url)
		return newUrls,htmlContent