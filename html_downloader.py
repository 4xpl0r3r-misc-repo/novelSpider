# -*- coding: utf-8 -*-

import requests,logging,asyncio
from multiprocessing import Queue

class htmlDownloader:
	def __init__(self):
		self.count=0
		self.session=requests.Session()
		self.tRes=None
		self.eventLoop=asyncio.get_event_loop()
		self.tRes=Queue()

	def download(self,urls,mode=0):#0为全部，其它则指定长度
		self.tRes=Queue()
		if not mode:
			tasks=[self.in_download(urls.get()) for i in range(urls.qsize())]
		else:
			tasks=[self.in_download(urls.get()) for i in range(mode)]
		logging.debug(len(tasks))
		self.eventLoop.run_until_complete(asyncio.wait(tasks))

	async def in_download(self,url):
		logging.info("开始下载:%s"%url)
		response=self.session.get(url)
		response.raise_for_status()
		response.encoding='utf-8'
		self.tRes.put((url,response.text))

	def singleDownload(self,url):
		logging.info("开始下载:%s"%url)
		response=self.session.get(url)
		response.raise_for_status()
		response.encoding='utf-8'
		return response.text