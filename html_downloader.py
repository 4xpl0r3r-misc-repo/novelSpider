# -*- coding: utf-8 -*-

import urllib.request

class htmlDownloader:
	def download(self,url):
		if url is None:
			return
		else:
			try:
				print("[info]","开始下载:%s"%url)
				response=urllib.request.urlopen(url)
				if response.getcode()==200:
					return response.read()
				else:
					raise downloadError("下载失败，状态码为:%d",response.getcode())
			except Exception as e:
				print("[error]","下载发生异常:%s\n\t异常信息如下:"%url)
				print('\t',e)
				return False