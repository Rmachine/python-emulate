# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 09:40:23 2019

@author: 姜
"""
"""
1.进程 pid 唯一标示符,使用kill 杀死进程
2.主线程 创造一个进程的时候，会创造一个线程，这个线程被称为主线程,一个进程里只有一个主线程
3.python里的多线程，不是真正意义上的多线程。在任意的指定时间里，有且只有一个线程在运行;
4.线程启动速度快，进程启动速度慢。
5.lock = threading.Lock()  lock.acquire()  lock.release() #加锁就需要解锁
6.用于生产者消费者模型中，解决生产者，消费者速度匹配的问题。


全局锁
"""
"""
例子
"""
event = threading.Event()
def chihuoguo(name):
    # 等待事件，进入等待阻塞状态
    print('%s 已经启动' % threading.currentThread().getName())
    print ('小伙伴 %s 已经进入就餐状态！'%name)
    time.sleep(1)
    event.wait()
    # 收到事件后进入运行状态
    print('%s 收到通知了.' % threading.currentThread().getName())
    print( '小伙伴 %s 开始吃咯！'%name)

# 设置线程组
threads = []
# 创建新线程
thread1 = threading.Thread(target=chihuoguo, args=("a", ))
thread2 = threading.Thread(target=chihuoguo, args=("b", ))
# 添加到线程组
threads.append(thread1)
threads.append(thread2)

# 开启线程
for thread in threads:
    thread.start()

time.sleep(0.1)
# 发送事件通知
print('主线程通知小伙伴开吃咯！')
event.set()


"""
习题一：已知列表 info = [1,2,3,4,55,233]
生成6个线程对象,每次线程输出一个值，最后输出："the end"。
"""
import threading,time

def test(p):
    time.sleep(0.1)#推迟执行的秒数
    print(p)

ts=[]

for i in range(0,15):
    th = threading.Thread(target=test,args=[i])#创建一个线程实例
#target目标函数;name线程起名;args目标函数传递实参（元组）;Kwargs目标函数关键词传参，字典
    th.start() #启动这个线程实例
    th.join()
#不加join的话，主线程和子线程完全是并行的，加了join主线程得等这个子线程执行完毕，才能继续往下走。保证代码的执行顺序。
    ts.append(th)
    
for i in range(0,15):
    th = threading.Thread(target=test,args=[i])#创建一个线程实例
#target目标函数;name线程起名;args目标函数传递实参（元组）;Kwargs目标函数关键词传参，字典
    th.start() #启动这个线程实例
    ts.append(th)

"""
    习题二：已知列表 urlinfo = ['http://www.sohu.com','http://www.163.com','http://www.sina.com'] 
用多线程的方式分别打开列表里的URL，并且输出对应的网页标题和内容。
"""
import urllib,re,threading,chardet

def url(web):
    wb = urllib.request.urlopen('http://www.sina.com').read()
    k = re.search(r'charset=(?<=“)(.*?)*(?=”)/*>',str(wb)) #读取网页的编码格式;前面的一个 r 表示字符串为非转义的原始字符串，让编译器忽略反斜杠
    ws = wb.decode(k.group(2)) #将文本转为应有格式，防止乱码
    #re.search(r'<title>(.*)</title>',ws)
    print(re.search(r'<title>(.*)</title>',ws))

ts=[]
urlinfo = ['http://www.sina.com']
for i in urlinfo:
    th = threading.Thread(target=url,args=[i])
    th.start() #启动这个线程实例
    ts.append(th)
