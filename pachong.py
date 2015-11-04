#encoding:utf-8
import re
import urllib


def getHtml(url):
    #获取整个页面的信息
    page=urllib.urlopen(url) 
    html=page.read()
    return html

def getImg(html):
    reg=r'src="(.*?\.jpg)".*width'
    regg=r'src="(.*?\.jpg)'
    imgre=re.compile(reg)
    imglist= re.findall(imgre,html)
    x=0
    filename='D://Users//lizelin//workspace//hello//pic//'
    for imgurl in imglist:
        if 'src=' in imgurl:
            imgurl=re.findall(regg,imgurl)[0]
            
        urllib.urlretrieve(imgurl,filename+'%s.jpg'%x)
        x=x+1
    return imglist
    
html=getHtml('http://tieba.baidu.com/p/3977787294')
listimg=getImg(html)
for lurr in listimg:
    print lurr
    