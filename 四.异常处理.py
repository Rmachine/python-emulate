# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:49:52 2019

@author: 姜
"""
#一个try就有一个except
try:
    " 框住了你感觉会抛出异常的代码 "
    print("41223123")
    print( "hahaha")
except:
    " try代码块里的代码如果抛出异常了，该执行什么内容"
    print( u"哈哈")
else:
    "try代码块里的代码如果没有跑出异常，就执行这里"
    print( "hoho")
finally:
    "不管如何，finally里的代码，是总会执行的"
    print( "xixi")

#日志生成  使用ogging.getLogger()
import logging   
logger = logging.getLogger()
logfile = 'test.log'
hdlr = logging.FileHandler('sendlog.txt') #日志存储文件名
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s') #设置格式
hdlr.setFormatter(formatter) #文件操作符 和 格式 关联
logger.addHandler(hdlr) #对象 和 文件操作符 关联
logger.setLevel(logging.NOTSET)


logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename= logging.FileHandler('slog.txt'),
                filemode='w') #函数式简单配置basicconfig 
#basicconfig 局限性：1、中文的乱码问题 2、不能同时往文件和屏幕上输出
    
logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')