# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 09:40:23 2019

@author: 姜
"""
"""
多线程
1.进程 pid 唯一标示符,使用kill 杀死进程
2.主线程 创造一个进程的时候，会创造一个线程，这个线程被称为主线程,一个进程里只有一个主线程
3.python里的多线程，不是真正意义上的多线程。在任意的指定时间里，有且只有一个线程在运行;
4.线程启动速度快，进程启动速度慢。
5.lock = threading.Lock()  lock.acquire()  lock.release() #加锁就需要解锁
6.用于生产者消费者模型中，解决生产者，消费者速度匹配的问题。
全局锁

生成器
1.函数只有一个单一的入口，函数只有一次返回结果的机会，因而必须一次返回所有的结果。
    一个生成器函数的定义很像一个普通的函数，除了当它要生成一个值的时候，使用yield关键字而不是return。如果一个def的主体包含yield，这个函数会自动变成一个生成器（即使它包含一个return）
    yield就是专门给生成器用的return(加上点小魔法
    当一个生成器函数调用yield，生成器函数的“状态”会被冻结，所有的变量的值会被保留下来，下一行要执行的代码的位置也会被记录，直到再次调用next()。一旦next()再次被调用，生成器函数会从它上次离开的地方开始。如果永远不调用next()，yield保存的状态就被无视了。
2.生成器函数在Python中与迭代器协议的概念联系在一起。
3.包含yield的函数，则是一个可迭代对象。
利用next方法，取每一次的yield
send()    next()只能以None作为参数传递，而send()可以传递yield的值
应用：
1.生产者，消费者行为
2.无需立刻执行，需要时才执行
3.斐波拉切数列的例子
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

"""
有10个刷卡机，代表建立10个线程，每个刷卡机每次扣除用户一块钱进入总账中，每个刷卡机每天一共被刷100次。账户原有500块。所以当天最后的总账应该为1500
"""
import threading
mLock = threading.Lock()
money = 500

def a():
    global money
    for i in range(100):
        #mLock.acquire()
        money += 1
        print(money)
        #mLock.release()

l = []
for i in range(10):
    t = threading.Thread(target=a)
    t.start()
    l.append(t)

for i in l:
    t.join()
money

""""
习题一：
定义一个生成器函数，函数里只能用yield，要求输出结果：
step 1
step 2 x=haha
step 3 y=haha
提示步骤：建立生成器对象，并且用对象的next()和send()方法来输出结果。send()方法传入的参数是"haha"
"""
def test():
    x = yield 'step 1'
    y = yield 'step2 x=%s' % x
    z = yield 'step3 y=%s' % y

t = test()
print(t.__next__())
print(t.send('haha')) # output: step2 x=haha
print(t.send('haha')) # output: step3 y=haha

"""
用生成器yield实现斐波拉切数列。
"""
def febir(num):
    x,y = 1,1
    while y < num:
        k = yield x  
        #send是发送一个参数给yield的，供其赋值
        #而只有yield时，相当与return，没有赋值能力
        x,y = y,x+y
        print(k)
        
for i in febir(100):
    print(i)

t = febir(100)
t.__next__()
t.send(9)

"""
例子
"""
import random
def get_data():
    """返回0到9之间的3个随机数"""
    return random.sample(range(10), 3)
def consume():
    """显示每次传入的整数列表的动态平均值"""
    running_sum = 0
    data_items_seen = 0

    while True:
        data = yield
        data_items_seen += len(data)
        running_sum += sum(data)
        print('The running average is {}'.format(running_sum / float(data_items_seen)))
def produce(consumer):
    """产生序列集合，传递给消费函数（consumer）"""
    while True:
        data = get_data()
        print('Produced {}'.format(data))
        consumer.send(data)
        yield
if __name__ == '__main__':
    consumer = consume()
    consumer.send(None)
    producer = produce(consumer)
    for _ in range(10):
        print('Producing...')
        next(producer)


'''
生成一个素数列表:
(1)只能被1和自己整除
(2)1不是素数
'''
def is_p(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

def ss():
    for i in range(1, 101):
        if is_p(i) == True:
            yield i