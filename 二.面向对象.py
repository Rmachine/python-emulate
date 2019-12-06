# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:28:15 2019

@author: 姜
"""

""" 
进阶 面向对象 
一、初识class
类(Class) 用来描述具有相同的属性和方法的对象的集合。
1.如何去定义一个最基本的class  
2.class最基本的子元素  
3.class传参
4.__init__方法 （初始化对象，让实例变量显式）
5.class和函数的区别 （class相当与函数集合；类中定义的函数第一个参数永远是实例变量self，并且调用时不用传递该参数。）

如何去使用对象内置的方法
1.实例化这个class （test） t = test()
2.使用 class.method()的方式去调用 class 的内置方法

注意：
1.当定义一个class的内置方法method时，method的参数的第一个永远是self（代表对象本身）。
2.函数中的参数一般不可被其他函数使用，除非将该参数定义为glob；但是在对象里面定义的各方法参数可相互使用，self.var1 = var1中的var1值就可共用。

步骤：分化需求；找到共同性；找到最小节点
@property 讲函数当装饰用，引用函数的时候不需要.d()仅.的即可
@staticmenthod  静态方法的装饰
"""
# 例子
class test(object):  # 我们所有的class都是object的派生类
	# get被称之为test对象的方法
    a = 1  # a被称为 test的 属性
    
    def __init__(self,var1):
        self.var1 = var1
    
    def get(self,a=None):
        return self.var1
    
    pass
"""
t是类test的一个实例
"""
t = test('test str heiheihei')
t.a
print(t.get())

#习题：
'''
一：定义一个学生类。有下面的类属性：1 姓名;2 年龄;3 成绩（语文，数学，英语)[每课成绩的类型为整数]
类方法：
1 获取学生的姓名：get_name() 返回类型:str
2 获取学生的年龄：get_age() 返回类型:int
3 返回3门科目中最高的分数。get_course() 返回类型:int
'''
class student(object):
    def  __init__(self,name,age,scores):  #__init__底下不能使用return，仅赋值 只能用print
        self.name = name
        self.age = age
        self.scores = scores    
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        return max(self.scores)
st = student('zhangming', 20, [69, 88, 90])
st.get_age()
st.get_course()
st.get_name()

''''
二：定义一个字典类：dictclass。完成下面的功能：
dict = dictclass({你需要操作的字典对象})
1 删除某个key  del_dict(key)
2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"   get_dict(key)
3 返回键组成的列表：返回类型;(list)  get_key()
4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)   update_dict({要合并的字典})
'''
class dictclass(object):
    def __init__(self, dict):
        self.dict = dict
        
    def del_dict(self,key):
        if key in self.dict.keys():
            del self.dict[key]
        else:
            return "not found"
        
    def get_dict(self,key):
        if key in self.dict.keys():
            return self.dict[key]
        else:
            return "not found"
                 
    def get_key(self):
        return self.dict.keys()
    
    def update_dict(self,dict2):
        self.dict = dict(self.dict, **dict2)
        #字典合并，list合并:https://www.cnblogs.com/zhaoyingjie/p/8675365.html
        return self.dict.values()    

A = dictclass({'a': 1, 'b': 2})
print(A.get_dict('a'))
print(A.del_dict('a'))
print(A.get_key())
print(A.updata_dict({'c': 3, 'd': 4}))

A = {'a': 1, 'b': 2}
'a' in A.keys()  #字典
A['a']
A.values()
del A['a']

# 关于合并字典
A = {'a': 1, 'b': 2, 'c': 3}
B = {'d': 4, 'e': 5, 'f': 6}
A.update(B)  # 直接改变了A的字典
dict(A, **B)  # 这种合并方法会比上一种快很多。对于重复的key，B会覆盖A；该方法不会直接改变A
'''
三.定义一个列表的操作类：Listinfo
包括的方法: 
1 列表元素添加: add_key(keyname)  [keyname:字符串或者整数类型]
2 列表元素取值：get_key(num) [num:整数类型]
3 列表合并：update_list(list)	  [list:列表类型]
4 删除并且返回最后一个元素：del_key() 
'''
class Listinfo(object):
    def __init__(self, lists):
        self.lists = lists
    def add_key(self,keyname):
        if isinstance(keyname, (str, int)): #
            self.lists.append(keyname) #.append()向列表尾部追加一个新元素   .extend() 向列表尾部追加一个列表
            return self.lists
        return "error"
    def get_key(self,num):
        if num >= 0 and num < len(self.lists):
            return self.lists[num] # 注意该操作会改变self.lists内的值；使用.copy可避免
        return "超出取值范围"
    def update_list(self,list1):
        list3 = self.lists.copy() 
        if isinstance(list1, list):
            list3.extend(list1)
            return list3
        return "类型错误"
    def del_key(self):
        list4 = self.lists.copy()
        return list4.pop(-1) #pop删除下标所对应的元素,并返回删除值；.remove('e')删除制定元素、del names[4]
    
a = Listinfo([44, 222, 111, 333, 454, 'sss', '333'])
print(a.add_key(1))
print(a.get_key(1))
print(a.update_list([1, 2, 3]))
print(a.del_key())

'''
四.定义一个集合的操作类：Setinfo
包括的方法: 
1 集合元素添加: add_setinfo(keyname)  [keyname:字符串或者整数类型]  add
2 集合的交集：get_intersection(unioninfo) [unioninfo :集合类型]     A & B;A.intersection(B)
3 集合的并集： get_union(unioninfo)[unioninfo :集合类型]  A | B;A.union(B)
4 集合的差集：del_difference(unioninfo) [unioninfo :集合类型]   A - B;A.difference(B)
# 集合(set)是一个无序的不重复元素序列
'''
class Setinfo():
    def __init__(self, my_set):
        self.sett = my_set
    def add_setinfo(self, keyname):
        if isinstance(keyname, (str, int)):
            self.sett.add(keyname)
            return self.sett
    def get_intersection(self, unioninfo):
        if isinstance(unioninfo, set):
            a = self.sett & (unioninfo)
            return a
    def get_union(self, unioninfo):
        if isinstance(unioninfo, set):
            a = self.sett | (unioninfo)
            return a
    def del_difference(self, unioninfo):
        if isinstance(unioninfo, set):
            a = self.sett - (unioninfo)
            return a

a = Setinfo({1, "a", 2, "b", 3, "c"})
print(a.add_setinfo(4))
print(a.get_intersection({1, 2, "a"}))
print(a.get_union({2, 3, 4, "c", "d"}))
print(a.del_difference({1, 2, 3, 4}))

"""
五： 写一个网页数据操作类。完成下面的功能：提示：需要用到urllib模块
get_httpcode()获取网页的状态码，返回结果例如：200,301,404等 类型为int 
get_htmlcontent() 获取网页的内容。返回类型:str
get_linknum()计算网页的链接数目。
urllib.request 请求模块;urllib.error 异常处理模块;urllib.parse url解析模块
"""
import urllib
class page_data(object):
    def __init__(self,webs):
        self.webs = webs
        self.webo = urllib.request.urlopen(webs)
    def get_httpcode(self):
        status = self.webo.code
        return status
    def get_htmlcontent(self):
        contentstr = self.webo.read() #read（）操作可以得到一个包含网页的二进制字符串
        return contentstr
    def get_linknum(self):
        content = str(self.webo.read())
        return len(content.split('<a href=')) - 1
# TypeError: a bytes-like object is required, not 'str'

A = page_data("http://www.baidu.com")
print(A.get_httpcode())  
print(A.get_htmlcontent())
print(A.get_linknum())

"""
六.对象中嵌套对象（继承）
"""
class SchoolMember():
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print ('(Initialized SchoolMember: %s)' % self.name)

    def tell(self):
        '''Tell my details.'''
        print ('Name:"%s" Age:"%s"' % (self.name, self.age))

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print ('(Initialized Teacher: %s)' % self.name)

    def tell(self):
        print ('Salary: "%d"' % self.salary)

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print ('(Initialized Student: %s)' % self.name)

    def tell(self):
        print ('Marks: "%d"' % self.marks)

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 22, 75)

members = [t, s]
for member in members:
    member.tell()




