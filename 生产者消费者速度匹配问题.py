# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:18:53 2019

@author: 姜
"""

用于生产者、消费者模型，为了解决生产者消费者速度匹配的问题：
import threading
import logging
import random

FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
logging.basicConfig(format=FORMAT,level=logging.INFO) #基础配置

#生成日志
import logging   
logger = logging.getLogger()
logfile = 'test.log'
hdlr = logging.FileHandler('slg.txt') #日志存储文件名
formatter = logging.Formatter('%(asctime)s %(threadName)s %(thread)d %(message)s') #设置格式
hdlr.setFormatter(formatter) #文件操作符 和 格式 关联
logger.addHandler(hdlr) #对象 和 文件操作符 关联
logger.setLevel(logging.NOTSET)

#日志按照info、debug、error等级别来进行区分
class Dispatcher:
    def __init__(self):
        self.data = None
        self.event = threading.Event()

    def produce(self,total):
        for _ in range(total):
            data = random.randint(0,100)
            logging.info(data)
            self.data = data
            self.event.wait(1) # 收到事件后进入运行状态
        self.event.set()#将标志设为True，并通知所有处于等待阻塞状态的线程恢复运行状态。

    def consume(self):
        while not self.event.is_set():
            data = self.data
            logging.info('recieved{}'.format(data))
            self.data = None
            self.event.wait(0.5)

d = Dispatcher()
d.produce(2)

p = threading.Thread(target=d.produce,args=(10,),name='producer')

c = threading.Thread(target=d.consume,name='consume')

c.start()

p.start()
 

消费者采用主动消费，消费者浪费了大量的时间，主动来查看有没有数据。换成通知的机制。

import threading

import logging

import random



FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'

logging.basicConfig(format=FORMAT,level=logging.INFO)



class Dispatcher:

    def __init__(self):

        self.data = None

        self.event = threading.Event()

        self.cond = threading.Condition()



    def produce(self,total):

        for _ in range(total):

            data = random.randint(0,100)

            with self.cond:

                logging.info(data)

                self.data = data

                self.cond.notify_all()
#notify(n=1): 通知其他线程，那些挂起的线程接到这个通知之后会开始运行，默认是通知一个正等待该condition的线程,最多则唤醒n个等待的线程。notify()必须在已获得Lock前提下才能调用，否则会触发RuntimeError。notify()不会主动释放Lock。
#notifyAll(): 如果wait状态线程比较多，notifyAll的作用就是通知所有线程
            self.event.wait(1) # 线程挂起，直到收到一个notify通知或者超时

        self.event.set()



    def consume(self):

        while not self.event.is_set():

            with self.cond:

                self.cond.wait()

                logging.info('recieved{}'.format(self.data))

                self.data = None

            self.event.wait(0.5)



d = Dispatcher()

p = threading.Thread(target=d.produce,args=(10,),name='producer')

c = threading.Thread(target=d.consume,name='consume')

c.start()

p.start()
 

如果是一个生产者，多个消费者呢：

import threading

import logging

import random



FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'

logging.basicConfig(format=FORMAT,level=logging.INFO)



class Dispatcher:

    def __init__(self):

        self.data = None

        self.event = threading.Event()

        self.cond = threading.Condition()



    def produce(self,total):

        for _ in range(total):

            data = random.randint(0,100)

            with self.cond:

                logging.info(data)

                self.data = data

                self.cond.notify_all()

            self.event.wait(1)  #模拟生产速度

        self.event.set()



    def consume(self):

        while not self.event.is_set():

            with self.cond:

                self.cond.wait()  #阻塞等通知

                logging.info('recieved{}'.format(self.data))

            self.event.wait(0.5)  #模拟消费 的速度



d = Dispatcher()

p = threading.Thread(target=d.produce,args=(10,),name='producer')





for i in range(5):

    c = threading.Thread(target=d.consume, name='consume{}'.format(i))

    c.start()

p.start()