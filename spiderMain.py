# -*- coding: utf-8 -*-

import html_downloader,html_parser,html_outputer
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
		self.htmlDownloader=html_downloader.htmlDownloader()
		self.htmlParser=html_parser.htmlParser();
		self.htmlOutputer=html_outputer.htmlOutputer();
		self.baseUrl=sys.argv[1][:sys.argv[1].rfind('/')+1]
		self.nextUrl=sys.argv[1][sys.argv[1].rfind('/')+1:]

def main():
	iSpider=Spider()
	count = 1
	while iSpider.nextUrl!='./':
		print("开始第",count,"次下载")
		nextUrl=iSpider.baseUrl+iSpider.nextUrl
		data=[]
		data.append(nextUrl)
		data.append(iSpider.htmlDownloader.download(nextUrl))
		try:
			data=iSpider.htmlParser.parse(*data)#data含义转变
		except Exception as e:
			print("[error]","解析失败:%s"%nextUrl,"\n\t","异常信息如下:","\n\t",e)
			count=count-1
			continue
		iSpider.nextUrl=data[0]
		#输出数据
		print("[info]","第",count,"章","数据导出中...")
		iSpider.htmlOutputer.outputData(count,data[1])
		print("[info]","第",count,"章","数据导出完成")
		count=count+1
		
	print("[info]","结尾数据导出中...")
	iSpider.htmlOutputer.outputFinalData(count)
	print("[info]","结尾数据导出完成")

if __name__=='__main__':
	print("[info]","开始运行")
	main()
	print("[info]","程序结束")
else:
	print("[error]","非法调用!")
