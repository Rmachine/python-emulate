# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 10:02:01 2019

@author: 姜
"""
"""
1.去哪里找模块：pypi.python.org python的模块库
2.选择哪些的模块:内置文档http://docs.python.org/2.7/
help()

3.常用模块
3.1 urllib urllib2 网络
3.2 datetime time 时间
3.3 os 系统，丰富的方法用来处理文件和目录
3.4 pickle  对象序列化
      常用数据交换格式 json xml 
3.5 bsddb key=>value 
3.6 logging 日志
"""

"""
习题一：
1.1 用time模块获取当前的时间戳.
1.2 用datetime获取当前的日期，例如：2013-03-29
1.3 用datetime返回一个月前的日期：比如今天是2013-3-29 一个月前的话：2013-02-27
"""
import time
import datetime
time.time()
a = datetime.date.today()
a.__format__('%Y-%m-%d')
datetime.date(a.year,a.month-1,a.day)

#函数可更改为前几个月或后几个月
class date_pre_next(object): #class里面的函数也可相互调用
    def __init__(self,dt):
        self.dt = dt
    #返回一个月前的日期
    def premonth(self):                                                     
        if self.dt.month == 1: #上一个月跨年
            premonth = datetime.date(self.dt.year-1, 12,self.dt.day) #1月与12月的天数一样多
        else: #月尾的日期不同
            next_month_first_day = datetime.date(self.dt.year,self.dt.month-1,1) 
            if self.dt.day > eomonth(next_month_first_day).day:
                premonth = datetime.date(self.dt.year,self.dt.month-1,eomonth(next_month_first_day).day)
            else:
                premonth = datetime.date(self.dt.year, self.dt.month-1, self.dt.day)
        return premonth
    #返回上一个月的日期
    def edate(self):  
        if self.dt.month == 12:  
            next_month_date = datetime.date(self.dt.year+1, 1,self.dt.day)
        else:
            next_month_first_day = datetime.date(self.dt.year,self.dt.month+1,1)
            if self.dt.day > eomonth(next_month_first_day).day:
                next_month_date = datetime.date(self.dt.year,self.dt.month+1,eomonth(next_month_first_day).day)
            else:
                next_month_date = datetime.date(self.dt.year, self.dt.month+1, self.dt.day)
        return next_month_date
    # 指定日期当月最后一天的日期和本月天数
    def eomonth(self):
        if self.dt.month == 12:
            next_month_first_date = datetime.date(self.dt.year+1,1,1) 
        else:
            next_month_first_date = datetime.date(self.dt.year, self.dt.month+1, 1) 
        return next_month_first_date - datetime.timedelta(1) 

date = datetime.date(2017,10,31) 
a = date_pre_next(date)
a.premonth()

# 提前或之后几个月
class date_prenext(object): #class里面的函数也可相互调用
    """
    dt是datatime.date()时间
    m是需要提前或者之后的月份数,之前为-  之后为+
    """
    def __init__(self,dt,n_month):
        self.dt = dt
        self.m = n_month
    #返回一个月前的日期
    def PNMonth(self):
        mm = self.dt.month + self.m 
        m_add = mm % 12
        if m_add == 0:
            m_add = 12
        y_add = (mm-1) // 12
        pn_month = datetime.date(self.dt.year + y_add,m_add ,1)
        #月尾的日期不同
        if self.dt.day > eomonth(pn_month).day:
            pn_month = datetime.date(self.dt.year + y_add,m_add ,eomonth(pn_month).day)
        else:
            pn_month = datetime.date(self.dt.year + y_add,m_add , self.dt.day)
        return pn_month

    # 指定日期当月最后一天的日期和本月天数
    def eomonth(self):
        if self.dt.month == 12:
            next_month_first_date = datetime.date(self.dt.year+1,1,1) 
        else:
            next_month_first_date = datetime.date(self.dt.year, self.dt.month+1, 1) 
        return next_month_first_date - datetime.timedelta(1) 

date = datetime.date(2017,10,31) 
a = date_prenext(date,-25)
a.PNMonth()

"""
习题二:
1 用os模块的方法完成ping www.baidu.com 操作。 #丰富的方法用来处理文件和目录
2 定义一个函数kouzhang(dirpwd)，用os模块的相关方法，返回一个列表，列表包括：dirpwd路径下所有文件不重复的扩展名，如果有2个".py"的扩展名，则返回一个".py"。
"""
import os
os.system("ping www.baidu.com")
#文件路径和文件名的折分与合并
os.path.split('D:\\python_code\\split_functon.py')
filepath = os.path.join('D:\\python_code', 'split_functon.py')
os.path.splitext('D:\\python_code\\split_functon.py')[1]#文件名和扩展名的拆分
# dirpwd路径下所有文件不重复的扩展名
a = []
for files in os.listdir('C:\\Users\\姜\\Desktop\\python\\笔记'):
    b = os.path.splitext(files)[1]
    a.append(b)
a = list(set(a))

