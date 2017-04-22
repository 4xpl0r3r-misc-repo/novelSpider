# -*- coding: utf-8 -*-

import url_manager,html_downloader,html_parser,html_outputer
import sys

def test(tSpider):
	sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
	url=tSpider.urlManager.getNewUrl()
	t=tSpider.htmlParser.parse(url,tSpider.htmlDownloader.download(url))
	tSpider.urlManager.addUrls(t[0])
	for (a,b) in t[1].items():
		print(b.encode().decode('utf-8','ignore'))

class Spider:
	def __init__(self):
		self.urlManager=url_manager.urlManager()
		self.htmlDownloader=html_downloader.htmlDownloader()
		self.htmlParser=html_parser.htmlParser();
		self.htmlOutputer=html_outputer.htmlOutputer();
		self.urlManager.addUrl(sys.argv[1])

def main():
	iSpider=Spider()
	count = 1
	while count<=int(sys.argv[2]):
		print(count)
		if(not iSpider.urlManager.hasNewUrl()):
			break
		nextUrl=iSpider.urlManager.getNewUrl()
		data=[]
		data.append(nextUrl)
		data.append(iSpider.htmlDownloader.download(nextUrl))
		if(data==False):
			count=count-1
			continue
		if data[1]!='' and not data[1] is None:
			count=count+1
		try:
			data=iSpider.htmlParser.parse(*data)
		except Exception as e:
			print("[error]","解析失败:%s"%nextUrl,"\n\t","异常信息如下:","\n\t",e)
			count=count-1
			continue
		iSpider.urlManager.addUrls(data[0])
		iSpider.htmlOutputer.collectData(data[1])

	iSpider.htmlOutputer.outputData()

if __name__=='__main__':
	print("[info]","开始运行")
	main()
	print("[info]","程序结束")
else:
	print("[error]","非法调用!")
