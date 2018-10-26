# -*- coding: utf-8 -*-

class htmlOutputer:

	def outputData(self,count,datas):
		filename=str(count)+'.htm'
		fout=open(filename,'w',encoding='utf-8')
		fout.write('<html>')
		fout.write(r"<meta charset='utf-8'>")
		fout.write('<title>'+datas['title']+'</title>')
		fout.write(r'<link href="./style.css" rel="stylesheet" type="text/css" /> ')
		fout.write('<body>')
		if count>1:
			fout.write(r'<a href="'+str(count-1)+'.htm'+r'">上一章</a>')
		fout.write(r'<h3>'+datas['title']+r'</h3>')
		fout.write(r'<p>'+datas['text']+r'</p>')
		fout.write(r'<a href="'+str(count+1)+'.htm'+r'">下一章</a>')
		fout.write('</body>')
		fout.write('</html>')
		fout.close()

	def outputFinalData(self,count):
		filename=str(count)+'.htm'
		fout=open(filename,'w',encoding='utf-8')
		fout.write('<html>')
		fout.write(r"<meta charset='utf-8'>")
		fout.write('<title>看完啦</title>')
		fout.write(r'<link href="./style.css" rel="stylesheet" type="text/css" /> ')
		fout.write('<body>')
		fout.write('看完啦~')
		fout.write('</body>')
		fout.write('</html>')
		fout.close()