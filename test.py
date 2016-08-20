#coding=utf-8
#demo url:http://www.cnblogs.com/fnng/p/3576154.html
import re
import urllib
"""
a demo
"""
def getHtml(url):
    "获得url页面内容"
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getStrList(html,reg):
    "根据reg正则表达式的格式，获得html内容中的所需内容的列表"
    str_reg = re.compile(reg)
    str_list=re.findall(str_reg,html)
    return str_list

def saveImg(imglist):
    "保存图片"
    x=0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1
    return x

def write2File(html):
    "调试的时候可以先写到文件里面看一下网页的内容，再做匹配"
    f = open('1.txt','w')
    f.write(html)
    f.close()


if __name__=='__main__':
    html = getHtml("http://photo.poco.cn/lastphoto-htx-id-5200329-p-0.xhtml")
    # write2File(html)
    reg = r'data_org_bimg ="(.+?\.jpg[?]\d{4}[x]\d{4}[_]\d{3})"'
    str_list = getStrList(html,reg)
    print saveImg(str_list)
    # print str_list
