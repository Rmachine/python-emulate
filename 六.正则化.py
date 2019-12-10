# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 10:42:57 2019

@author: 姜
"""
"""
#coding=utf-8

'''
正则表达式，是字符串检索引擎
1.正则的几个基本概念

[0-9];\d 全部数字；[0-9]改为[1-2]或其他的话可以限制数字范围

\w 单词类字符 a-z A-Z 0-9 _
\W 非单词类字符
[ ]具有去特殊符号的作用

{2}  {n}  前面的表达式匹配n次；比如[0-9]\{2\} 匹配两次数组--反斜杠说明{并不是文本符号而是转义符
{0,2} {m,n} 前面的表达式匹配m到n次

. 匹配任意的字符
\+ 前面的表达式，出现1到无限次  最少，出现1次
\? 前面的表达式，出现0到1次  最多，出现1次
* 前面的表达式，出现0到无限次 出现不出现，都没关系
$ 完全匹配;’^’代表从起始位置开始,’$’代表到末尾为止
否定环视: (?!)和(?=);肯定环视: (?<!)和(?<=);例如 (?!/) 就代表匹配的字符串右边不能出现’/’;(?<!/) 就代表左边不能出现’/’
    
3.python里的正则模块 re https://www.runoob.com/python/python-reg-expressions.html
    compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
    re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
    re.search匹配整个字符串，直到找到一个匹配。
    findall字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
    
4.一些基本操作
4.1 一次取配 match:"hello lilei"  r'(\w+) (\w+)'
4.2 切割 split
4.3 查找全部 findall
4.4 finditer 迭代器什么的最有爱了
"""
'''
实例
'''
import re
s = '1102231990xxxxxxxx'
res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})',s)
res.groupdict()

line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
matchObj.group(0) 
'''
(.*) 第一个匹配分组，.* 代表匹配除换行符之外的所有字符。
 (.*?) 第二个匹配分组，.*? 后面多个问号，代表非贪婪模式，也就是说只匹配符合条件的最少字符
 后面的一个 .* 没有括号包围，所以不是分组，匹配效果和第一个一样，但是不计入匹配结果中。
matchObj.group() 等同于 matchObj.group(0)，表示匹配到的完整文本字符
matchObj.group(1) 得到第一组匹配结果，也就是(.*)匹配到的
matchObj.group(2) 得到第二组匹配结果，也就是(.*?)匹配到的
因为只有匹配结果中只有两组，所以如果填 3 时会报错。
'''

"""
1 已知字符串:
info = '<a href="http://www.baidu.com">baidu</a>'
用正则模块提取出网址："http://www.baidu.com"和链接文本:"baidu"
"""
import re
info = '<a href="http://www.baidu.com">baidu</a>'
m = re.search(r'<a href="(.*?)">(.*?)</a>',info)
m.group(1)
m.group(2)

pattern1=re.compile(r"[w.]*baidu\.*\w*") #['www.baidu.com', 'baidu'] #[ ]具有去特殊符号的作用
f1=pattern1.findall(info)
re.search(pattern1,info)
print(f1)

string = 'abe(ac)ad)'
p1 = re.compile(r'[(](.*?)[)]', re.S) #最小匹配
p2 = re.compile(r'[(](.*)[)]', re.S)  #贪婪匹配
print(re.findall(p1, string))
print(re.findall(p2, string))

"""
字符串："one1two2three3four4" 用正则处理，输出 "1234"
"""
info = 'one1two2three3four4'
re.findall(r'\d',info)

"""
已知字符串：text = "JGood is a handsome boy, he is cool, clever, and so on..." 查找所有包含'oo'的单词。
"""
text = "JGood is a handsome boy, he is cool, clever, and so on..."
re.findall(r'\w*oo\w*',text)

"""
已知字符串：
info = 'test,&nbsp;url("http://www.baidu.com")&,dddddd "="" <svg></svg><path></path><img src="http://www.baidu.com">ininnnin<img src="http://www.dd.com">'
要求完成下面2个小功能：
1.1 关闭[img]标签
1.2 将url()中的["]转为[']
最后结果字符串：
"test,&nbsp;url('http://www.baidu.com')&,dddddd "="" <svg></svg><path></path><img src="http://www.baidu.com"></img>ininnnin<img src="http://www.dd.com"></img>"
"""
def amend(string:str):
    rep = re.compile("(<img[^>]*>)")
    rep2 = re.compile("""(url\()"([^)]*)"(\))""")
    string = rep.sub(r"\1</img>",string)
    string = rep2.sub(r"\1'\2'\3",string)
    return string

info = 'test,&nbsp;url("http://www.baidu.com")&,dddddd "="" <svg></svg><path></path><img src="http://www.baidu.com">ininnnin<img src="http://www.dd.com">'
print(amend(info))