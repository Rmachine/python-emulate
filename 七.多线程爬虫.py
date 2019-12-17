# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 11:36:10 2019

@author: 姜
"""
"""
多线程爬虫
1.抓什么？怎么抓？ -》 确定抓取流程
2.爬虫的第一步是分析
3.分析的工具 ps:mashup,firebug
4.urllib足矣，还有scrapy
5.分析数据，正则 or beautifulsoup
6.beautifulsoup的小入门
"""
"""
作业1：
url :"http://money.163.com/special/pinglun/"
抓取第一页的新闻信息，并按照以下规格输出。
[
  {'title':'生鲜电商为何难盈利？','created_at':'2013-05-03 08:43','url':'http://money.163.com/13/0503/08/8TUHSEEI00254ITK.html'}
  {'title':'生鲜电商为何难盈利？','created_at':'2013-05-03 08:43','url':'http://money.163.com/13/0503/08/8TUHSEEI00254ITK.html'}
]
"""
import urllib
import pandas as pd
import re
import datetime
from bs4 import BeautifulSoup #https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/的文档
import scrapy

pip install scrapy

#抓取第一页的新闻信息
ur = urllib.request.urlopen("http://money.163.com/special/pinglun/")
ur_r = ur.read()
ur_dr = ur_r.decode(encoding= "gbk") #将文本转为应有格式，防止乱码;网页后的/charset=表示编码格式

lists = re.findall(r'<div class="item_top">[\s\S]+?</div>', ur_dr)
result = pd.DataFrame(columns = ['url','title','created_at'])
ncols = 0
for l in lists:
    tem = re.search(r'<h2><a href="([\s\S]+?)">([\s\S]+?)</a></h2>[\s\S]+<span class="time">([\s\S]+?)</span>', l)
    result.loc[ncols,'url'] = tem.groups()[0]
    result.loc[ncols,'title'] = tem.groups()[1]
    result.loc[ncols,'created_at'] = tem.groups()[2]
    ncols += 1
print(result)

result.to_excel(r'C:\Users\姜\Desktop\python\test\网易.xlsx',sheet_name = '网易')

#用BeautifulSoup的方法处理
ur = urllib.request.urlopen("http://money.163.com/special/pinglun/")
bur = BeautifulSoup(ur, "lxml")

bur.title.string
bur.find_all('a')
bur.find_all('p')
bur.find_all(class_="item_top")

bur.a['class'] #tag可能有很多个属性. tag <b class="boldest"> 有一个 “class” 的属性
bur.body.div.a #获得当前名字的第一个tag
itt = bur.body.find_all('div',class_ = 'item_top') #得到所有的<a>标签

result = pd.DataFrame(columns = ['url','title','created_at'])
ncols = 0

for i in itt:
    result.loc[ncols,'url'] = i.a['href']
    result.loc[ncols,'title'] = i.a.string
    result.loc[ncols,'created_at'] = i.span.string
    ncols += 1
print(result)

    

# 抓取前十页的新闻信息

#先定义要存的数据框
result = pd.DataFrame(columns = ['url','title','created_at'])
ncols = 0
# 主代码 - 读网址
for d in range(1,10):
    # 读取页面网址
    if d == 1:
        ur = urllib.request.urlopen("http://money.163.com/special/pinglun/")
    else:
        ym = '%s%s' % ("_0",str(d))
        urd = '%s%s%s' % ('http://money.163.com/special/pinglun',ym,"/")
        ur = urllib.request.urlopen(urd)
    #read并转码
    ur_r = ur.read()
    ur_dr = ur_r.decode(encoding= "gbk")

    #每个网页中的新闻页面
    lists = re.findall(r'<div class="item_top">[\s\S]+?</div>', ur_dr)
    #新闻标题、地址、时间
    for l in lists:
        tem = re.search(r'<h2><a href="([\s\S]+?)">([\s\S]+?)</a></h2>[\s\S]+<span class="time">([\s\S]+?)</span>', l)
        result.loc[ncols,'url'] = tem.groups()[0]
        result.loc[ncols,'title'] = tem.groups()[1]
        result.loc[ncols,'created_at'] = tem.groups()[2]
        ncols += 1
print(result)

#写入表格
result.to_excel('%s%s%s' % (r'C:\Users\姜\Desktop\python\test\网易_',str(datetime.date.today()),'.xlsx'),sheet_name = '网易')

"""
作业2：
url: "http://search.jd.com/Search?keyword=%E5%B9%BC%E7%8C%AB%E7%8C%AB%E7%B2%AE&enc=utf-8#filter"
print jd_search(keyword)
[dict,dict,dict]
dict {pic:'',title:'',price:'',url:''}
"""

keyword = 'iphone11'
a = "http://search.jd.com/Search?keyword={}&enc=utf-8&".format(urllib.parse.quote(keyword))
b = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36' #google浏览器的UA
head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3486.0 Safari/537.36',
        'method': 'GET'}#有些网站是反爬虫的，所以要把爬虫伪装成浏览器，随便打开一个浏览器，复制浏览器的UA（useragent） 值，用来伪装。

# 构造一个请求响应对象
requ = urllib.request.Request(a,headers=head)
#ua = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3486.0 Safari/537.36'
#re = urllib.request.Request(a,headers={'User-Agent':ua})  #有些网站是反爬虫的，所以要把爬虫伪装成浏览器，随便打开一个浏览器，复制浏览器的UA（useragent） 值，用来伪装。

#读网页
cont = urllib.request.urlopen(requ).read().decode()

#切割商品的主体模块
lists = re.findall(r'<div class="gl-i-wrap">[\s\S]+?</div>\s</li>',cont)
len(lists)
#l = lists[1]
#将相关数据写入result
result = pd.DataFrame(columns = ['title','price'])
ncols = 0
for l in lists:
    t = re.search(r'<em>[\s\S]+<font class="skcolor_ljg">([\s\S]+?)</font>([\s\S]+)</em>',l)
    result.loc[ncols,'title'] = t.group(1) + t.group(2)
    result.loc[ncols,'price'] = re.search(r'<em>￥</em><i>([\s\S]+?)</i>',l).group(1)
    ncols += 1

print(result)