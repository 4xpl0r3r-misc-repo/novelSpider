# -*- coding: utf-8 -*-
import url_manager,html_downloader,html_parser,html_outputer
from html_parser import ParseException
import sys,logging,bs4,requests,io
import traceback,queue,asyncio
from math import ceil
from multiprocessing.pool import Pool

class Spider:
	def __init__(self):
		self.urlManager=url_manager.urlManager()
		self.htmlDownloader=html_downloader.htmlDownloader()
		self.htmlParser=html_parser.htmlParser()
		self.htmlOutputer=html_outputer.htmlOutputer()
		self.urlManager.addUrl(sys.argv[1])

iSpider=Spider()

def initLogger():
	logging.basicConfig(level=logging.DEBUG)
	File=logging.StreamHandler(open('log.txt','w',encoding='utf-8'))
	File.setLevel(logging.DEBUG)
	logging.getLogger('').addHandler(File);

def endSolve():
	logging.info("进行程序尾处理")
	while not iSpider.urlManager.newUrls.empty():
		iSpider.urlManager.newUrls.get()

def solveData():
	logging.debug('向下载器获取缓存下载内容')
	data=iSpider.htmlParser.getData(*iSpider.htmlDownloader.tRes.get())
	iSpider.htmlOutputer.collectData(data)

def main():
	sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
	while iSpider.htmlOutputer.counter<int(sys.argv[2]):
		if(iSpider.htmlOutputer.counter<=int(sys.argv[2]) and not iSpider.urlManager.hasNewUrl()):
			url=iSpider.urlManager.getWaitUrl()
			urls=iSpider.htmlParser.getNewUrls(iSpider.htmlDownloader.singleDownload(url))
			iSpider.urlManager.addUrls(urls)
		logging.info('正在获取页面')
		iSpider.htmlDownloader.download(iSpider.urlManager.getNewUrls())
		iPool=Pool()
		iPool.apply_async(solveData())
		iPool.close()
		iPool.join()
		try:
			workLoop=asyncio.get_event_loop()
			task=[work() for i in range(iSpider.urlManager.newUrls.qsize())]
			workLoop.run_until_complete(asyncio.wait(task))
		except requests.exceptions.HTTPError as e:
			logging.error('下载发生异常，异常信息：%s'%e)
			continue
		except ParseException as e:
			logging.error('解析发生异常，异常信息：%s'%e)
			continue
		except queue.Empty as e:
			logging.critical('URL序列已空，程序无法继续运行！')
			break
		except Exception as e:
			logging.error('发生其它异常，异常信息：%s'%e)
			traceback.print_exc()
			break
		'''
			logging.info('正在获取第%d个页面'%iSpider.htmlOutputer.counter)
			if(not iSpider.urlManager.hasNewUrl()):
				url=iSpider.urlManager.getWaitUrl()
				urls=iSpider.htmlParser.getNewUrls(url,iSpider.htmlDownloader.download(url))
				iSpider.urlManager.addUrls(urls)
			nextUrl=iSpider.urlManager.getNewUrl()
			data=[]
			data.append(nextUrl)
			data.append(iSpider.htmlDownloader.download(nextUrl))
			data=iSpider.htmlParser.getData(*data)
			iSpider.htmlOutputer.collectData(data)
		'''
	logging.info("数据导出中...")
	iSpider.htmlOutputer.outputData()
	logging.info("数据导出完成")
	endSolve()

if __name__=='__main__':
	initLogger()
	logging.info("开始运行")
	main()
	logging.info("程序结束")

