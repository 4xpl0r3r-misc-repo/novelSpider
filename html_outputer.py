# -*- coding: utf-8 -*-
import logging

class htmlOutputer:
	def __init__(self):
		self.datas=[]
		self.counter=0

	def collectData(self,data):
		self.datas.append(data)
		self.counter=self.counter+1

	def outputData(self):
		fout=open('out.html','w',encoding='utf-8')
		fout.write('<html>')
		fout.write("<meta charset='utf-8'>")
		fout.write('<title>Spider数据输出</title>')
		fout.write('<body>')
		fout.write('<table>')
		for data in self.datas:
			fout.write('<tr>')
			fout.write('<td><a href="%s">'%data['url'])
			fout.write("%s</a></td>"%data['title'])
			fout.write("<td>%s</td>"%data['summary'])
			fout.write('</tr>')
		fout.write('</table>')
		fout.write('</body>')
		fout.write('</html>')
		fout.close()