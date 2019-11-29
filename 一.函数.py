# -*- coding: utf-8 -*-
"""
一. 函数的学习
"""

"""
1.定义一个方法 func，该func可以引入任意多的整型参数，结果返回其中最大与最小的值。
"""
def m_num(*args):
    for i in args:
        if not isinstance(i, int):
            return "输入的参数必须为整型" 
        #return 直接可以跳出循环
    return 'the max num is {}, the min num is {}'.format(max(args), min(args))
print(m_num(2,3,4,435,"a",55456,76,67,345,7))

"""
2.定义一个方法func，该func可以引入任意多的字符串参数，结果返回（长度）最长的字符串。
"""
def longest_char(*char):
    for i in char :
        if not isinstance(i,str):
            return "输入的参数必须为字符串"
    # a = sorted(char, key=lambda k: len(k),reverse = True)
    a = max(char, key=lambda k: len(k))
    # lambda表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数。
    # return 'the longest char is: ' + a[0]
    return 'the longest char is: ' + a

print(longest_char('asd', 'sadff', 'f', 'ffsff', 'sfdreyheg'))

"""
3.定义一个方法get_doc(module)，module参数为该脚本中导入或定义的模块对象，该函数返回module的帮助文档。
"""
def get_doc(module):
    print(module.__doc__)
    
get_doc(open)

"""
4.定义一个方法get_text(f),f参数为任意一个文件的磁盘路径，该函数返回f文件的内容。
"""
import os  #丰富的方法用来处理文件和目录
def get_text(f):
    if os.path.exists(f): #检验给出的路径是否真的存在
        with open(f, 'r') as g: #python文件读写,不必调用f.close()方法确保能正确地关闭文件
            return g.read()
    return "没有这个文件"
print(get_text('C:\\Users\\姜\\Desktop\\python\\python进阶篇\\进阶篇03-函数第二节\\习题.txt'))

"""
5.定义一个方法get_dir(folder),folder参数为任意一个文件夹，该函数返回folder文件夹的文件列表。
glob.glob(r’c:*.txt’) # 获得C盘下的所有txt文件
"""
import glob  #文件操作相关模块，用它可以查找符合自己目的的文件，类似于Windows下的文件搜索，支持通配符操作
def get_dir(folder):
    for i in glob.glob(folder + '\*'): # \*匹配所有文件
        print(i)
get_dir('C:\\Users\\姜\\Desktop\\python\\python进阶篇\\进阶篇03-函数第二节')
os.listdir('C:\\Users\\姜\\Desktop\\python\\python进阶篇\\进阶篇03-函数第二节')    

folder = 'C:\\Users\\姜\\Desktop\\python\\python进阶篇\\进阶篇03-函数第二节'
glob.glob(folder + "\*") # 输出为元组

"""
6. 定义一个方法get_num(num),num参数是列表类型，判断列表里面的元素为数字类型。其他类型则报错，并且返回一个偶数列表：（注：列表里面的元素为偶数）。
"""
def get_num(num):
    if not isinstance(num, list):
        return "参数不是列表类型"
    l = []
    for i in num:
        if not isinstance(i, int):
            return str(i) + "不是数字类型, 是: " + str(type(i)) # "列表里面的元素非数字类型"
        if i % 2 == 0:
            l.append(i)
    return l
print(get_num([1,2,3,4,5,6.5,7,8,9,12,24,45]))
print(get_num([1,2,3,4,5,6,7,8,9,12,24,45]))
    
"""
7. 定义一个方法get_page(url),url参数是需要获取网页内容的网址，返回网页的内容。提示（可以了解python的urllib模块）。
"""
from urllib import request
from io import BytesIO
import gzip

def get_page(url):
    res = urllib.request.urlopen(url)
    htmls = res.read()
    buff = BytesIO(htmls)
    f = gzip.GzipFile(fileobj=buff)
    htmls = f.read().decode('utf-8')
    print(htmls)

get_page('https://www.douyu.com/')

import urllib
import random
import os
def save_url_content(url,folder_path=None):	
	if not (url.startswith('http://') or url.startswith('https://') ):
		return u'url地址不符合规格'
	if not os.path.isdir(folder_path):
		return u'folder_path非文件夹'
	d = urllib.urlopen(url)
	content = d.read()
	rand_filename = 'test_%s'%random.randint(1,1000)
	file_path = os.path.join(folder_path,rand_filename)
	d = open(file_path,'w')
	d.write(content)
	d.close()
	return file_path

# 网页中内置可点页码个数
def get_url_count(url):
	if not (url.startswith('http://') or url.startswith('https://') ):
		return u'url地址不符合规格'
	d = urllib.request.urlopen(url)
	content = str(d.read()) #read（）操作可以得到一个包含网页的二进制字符串
	return len(content.split('<a href=')) - 1

print(get_url_count('http://www.baidu.com')) #网页注意输入完整
print(get_url_count('http://baidu.com'))

"""
8.  定义一个方法 func，该func引入任意多的列表参数，返回所有列表中最大的那个元素。
"""
def max_list(*num):
    l = []
    for i in num :
        if not isinstance(i,list):
            return str(i) + "不是列表类型, 是: " + str(type(i)) 
        l.append(max(i))
    return "列表中最大的那个元素:{} ".format(max(l))
    # +后面只能时字符串,其他类型要用{} ".format

print(max_list([1,2,3],[2],[1,2]))

"""
9.定义一个方法get_dir(f),f参数为任意一个磁盘路径，该函数返回路径下的所有文件夹组成的列表，如果没有文件夹则返回"Not dir"。
"""
import os
import glob

def get_dir(file):
    if os.path.exists(file):
        return glob.glob(file + '/*')
    else:
        return 'No dir'
    
print(get_dir('C:/'))

"""
10. 定义一个方法get_fundoc(func),func参数为任意一个函数对象，返回该函数对象的描述文档，如果该函数没有描述文档，则返回"not found"
"""
def get_fundoc(func):
    # 使用calllable判断是否能被调用
    if not callable(func):
        return "func 参数不是函数对象"
    elif str(type(func)) == "<type 'classobj'>" or str(type(func)) == "<type 'module'>":
        return "func 参数不是函数对象"
    else:
        if func.__doc__ == None:
            return 'func 参数没有文档'
        else:
            return func.__doc__

print(get_fundoc(sorted))

"""
11. 定义一个方法get_cjsum(),求1-100范围内的所有整数的平方和。返回结果为整数类型。
"""
a = 0
for i in range(1,101):
    a += i**2


"""
12. 定义一个方法list_info(list), 参数list为列表对象，怎么保证在函数里对列表list进行一些相关的操作，不会影响到原来列表的元素值
"""
def list_info(l):
    a = l[:]    #a = l.copy()也可以, a = l 不可以
    # print(id(a), id(l))
    a[-1] = 5
    print(a)

l = [1,2,3]
list_info(l)
print(l)

"""
13.用lambda和filter完成下面功能：输出一个列表，列表里面包括：1-100内的所有偶数。（提示：可以用filter,lambda）
"""
lambda x : x % 2 == 0
list(filter(lambda x : x % 2 == 0,[2,4,5,6]))

"""
14.用位置匹配：k1，k2，k3按顺序输入
关键字匹配：k1 = value 锁定关键字，无需按顺序
收集匹配(元组收集*num,字典收集**num)：
分别写4个函数，完成功能；
传递3个列表参数：
[1,2,3],[1,5,65],[33,445,22]
返回这3个列表中元素最大的那个，结果是：445
"""
def max_list1(*num):
    l = []
    for i in num:
        l += i
    return(max(l))

max_list1([1,2,34],[55],[1,99])

"""
15.递归函数【自己调用自己】解释，用自己的话说明这个递归函数的工作流程。

def func1(i):
	if i<100:
		return i + func1(i+1)
	return i
print func1(0)
"""

import os
#使用递归去解决  合并目录下的所有文件，生成all.txt
#遇到问题：python在使用时空格和tab键是不一样的，设置显示空格使分格是一样的;注意缩进
def merge(folder_path):
    if  not  os.path.exists(folder_path):
        print('not exists')
    for  f  in  os.listdir(folder_path):
        #os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
        file_path = os.path.join(folder_path,f)
        if os.path.isdir(file_path):
            merge(file_path)
        else:
            merge_file = open('C:/Users/姜/Desktop/python/test/test2.txt','a')
            #open() 函数用于打开一个文件，创建一个 file 对象;open下有很多的打开方式
            content = open(file_path,'r',encoding='UTF-8').read()
            #遇到问题:文件编码问题，改加encoding='UTF-8'
            merge_file.write(content)
            #遇到问题：TypeError: a bytes-like object is required, not 'str'；
        merge_file.close()

folder_path = 'C:/Users/姜/Desktop/python/笔记'
#file_path = 'C:/Users/姜/Desktop/python/笔记/一.函数.py'
#del folder_path
merge('C:/Users/姜/Desktop/python/笔记')

## 获取url后的参数并返回为字典
#urlparse模块主要是用于解析url中的参数  对url按照一定格式进行 拆分或拼接 
from urllib import parse

def qs(url):
    query = parse.urlparse(url).query
    return dict([(k,v[0]) for k,v in parse.parse_qs(query).items()])

print(qs('http://126.com'))
print (qs('http://api/api?f=5&g=6&y=5'))
print qs('http://api/api?11=53')

#使用递归去解决  删除指定目录下的 所有文件
def delete(folder_path):##习题5
	if not os.path.exists(folder_path):
		return 'not exists'

	for f in os.listdir(folder_path):
		file_path = os.path.join(folder_path,f)
		if os.path.isdir(file_path):
			delete(file_path) #判断是否存在文件夹文件
		else:
			os.remove(file_path) #不存在时直接删除

delete('C:/Users/姜/Desktop/python/test')

'''
16.定义一个func(name)，该函数效果如下。
assert func("lilei") = "Lilei"
assert func("hanmeimei") = "Hanmeimei"
assert func("Hanmeimei") = "Hanmeimei"

assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。
'''
def capstr(name):
    '''
    capstr(name) -> str
    name is a str.
    return a capitalize type of name,or raise TypeError if name is not a str
    '''
    return name.capitalize()  #capitalize第一个字母变成大写,其他字母变小写

"""
17.定义一个func(name,callback=None),效果如下。
assert func("lilei") == "Lilei"
assert func("LILEI",callback=string.lower) == "lilei"
assert func("lilei",callback=string.upper) == "LILEI"
python 字符串常用操作：https://www.cnblogs.com/yujihaia/p/7468253.html
"""
import string
def swastr(name, callback=None):
    '''
    swastr(name, callback=None) -> str
    name is a str.return a str of required tyoe,or a capitalize type if is not required.
    '''
    if callback == None:
        return name.capitalize()
    else:
        return callback(name)    


"""
18.定义一个func(*kargs),效果如下。

l = func(1,2,3,4,5)
for i in l:
	print i,
#输出 1 2 3 4 5

"""
def getitem(*kargs):
    return kargs
getitem(1,2,3,4,5)

"""
19.定义一个func(*kargs)，该函数效果如下。
assert func(222,1111,'xixi','hahahah') == "xixi"
assert func(7,'name','dasere') == 'name'
assert func(1,2,3,4) == None
"""
def shortstr(*kargs):
    '''
    shortstr(*kargs) -> str or None
    return the shortest str in the kargs, or return None if no str in it.
    '''
    #过滤非字符串
    lis = filter(lambda x:isinstance(x,str),kargs)
    #收集长度
    len_lis = [len(x) for x in lis]

    if len_lis:
    		min_index = min(len_lis)
    		return lis[len_lis.index(min_index)]
    return None

"""
20.定义一个func(name=None,**kargs),该函数效果如下。
assert func(“lilei”) == "lilei"
assert func("lilei",years=4) == "lilei,years:4"
assert func("lilei",years=10,body_weight=20) == "lilei,years:4,body_weight:20"
"""
def detail(name=None,**kargs):
    '''
    detail(name=None,**kargs) -> str
    name is a str.return a str like'name,key1:value1,key2:value2'    
    '''
    name = "lilei"
    kargs = {'years':10,'body_weight':20}
    data = []
    for x,y in kargs.items():
        data.extend([',', str(x), ':', str(y)])
   
    info = ''.join(data)
    #  join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串； 'sep'.join(seq) 参数说明 sep：分隔符。
    return '%s%s'%(name,info)   
    #是将值插入到%s占位符的字符串中;
    #%s 字符串；%d 整型；%f 浮点型；
    #Python中%s、%d、%f意义及用法详解:https://blog.csdn.net/weixin_43620235/article/details/90693182

def func(name=None,**kargs):
	lis = ["%s:%s"%(k,v) for k,v in kargs.items()] 
	lis.insert(0,name)
	return ','.join(lis)  

name= input("Please input your name: ")
print("Hello, %s good morning!" %name)



b = list(filter(lambda x : x < 5, a))

b = []
for x in a:
	if x != 5:
		b.append(x)



