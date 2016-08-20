#coding=utf-8
#demo url:http://www.cnblogs.com/fnng/p/3576154.html
import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist=re.findall(imgre,html)
    return imglist

def saveImg(imglist):
    x=0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1
    return x

if __name__=='__main__':
    html = getHtml("http://tieba.baidu.com/p/2460150866")
    img_list = getImg(html)
    print saveImg(img_list)
