# -*- coding: utf-8 -*-

class htmlOutputer:
	def __init__(self):
		self.datas=[]

	def collectData(self,data):
		if data is None:
			return
		self.datas.append(data)

	def outputData(self):
		fout=open('out.html','w',encoding='utf-8')
		fout.write('<html>')
		fout.write(r"<meta charset='utf-8'>")
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