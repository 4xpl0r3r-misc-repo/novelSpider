# -*- coding: utf-8 -*-
from multiprocessing import Queue

class urlManager:
	def __init__(self):
		self.newUrls=Queue()
		self.oldUrls=set()
	def addUrl(self,url):
		if(not url is None and not url in self.oldUrls):
			self.newUrls.put(url)
			self.oldUrls.add(url)
			print("[info]","成功添加:%s"%(url))
		else:
			print("[warn]","无法添加:%s"%(url))

	def addUrls(self,urls):
		if(len(urls)==0 or urls is None):
			return
		for url in urls:
			self.addUrl(url)

	def hasNewUrl(self):
		return not self.newUrls.empty()

	def getNewUrl(self):
		return self.newUrls.get()
