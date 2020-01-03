# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 16:29:31 2019

@author: 姜
参考：https://blog.csdn.net/songbinxu/article/details/80411388
"""
import pandas as pd
import numpy as np
import sys

'''
0. 准备工作：数据集
'''

def createInitSet(dataSet):  # 用于实现上述从列表到字典的类型转换过程;构造成 element : count 的形式
    retDict = {}
    for trans in dataSet: #dataSet为[[],[]],trans循环取出里面的一个列表
        #retDict[frozenset(trans)] = 1
        retDict[frozenset(trans)] = retDict.get(frozenset(trans), 0) + 1  # 若没有相同事项，则为1；若有相同事项，则加1
        ## frozenset是冻结的集合，它是不可变的，存在哈希值，好处是它可以作为字典的key，也可以作为其它集合的元素。
        ## D.get(key,default=None)函数用于返回指定键的值，如果值不在字典中返回默认值
    return retDict


"""
1. 构建FP树
1.1 为了能方便地访问FP树种每一个不同的元素，需要为每种元素（的链表）设置一个头（header），
    这个header除了指向指定元素的第一个结点外，还可以保存该元素在数据集中的总出现次数。
1.2 首先，遍历一次数据集，统计每个元素出现的次数，然后把出现次数较小的滤掉（例如选取最小支持度3，将出现次数小于3的元素滤除）
1.3 然后，对每个样本按照元素出现次数重排序。
1.4 接着，构造FP树。从根节点∅开始，将过滤并排序后的样本一个个加入树中，若FP树不存在现有元素则添加分支，若存在则增加相应的值。
""""
def createFPtree(dataSet, minSup=1): #dataset是需要分析的数据类型 -- 字典
    headerTable = {}

    '''该for函数遍历一次数据集，统计每个元素出现的次数'''
    for trans in dataSet: #读取字典的key -- 对应需分支的‘清单’
        for item in trans: #item是每个key下对应元素
            headerTable[item] = headerTable.get(item, 0) + dataSet[trans] #读取对应元素的个数
#    for k in headerTable.keys():
#        if headerTable[k] < minSup:
#            del (headerTable[k] )# 删除不满足最小支持度的元素 
#    运行时错误：字典在迭代期间更改了大小

    '''该for函数删除不满足最小支持度的元素'''
    headerTable = {k: v for k, v in headerTable.items() if v >= minSup}
    
    '''初始化headerTable element: [count, node]'''
    freqItemSet = set(headerTable.keys()) # 满足最小支持度的频繁项集
    if len(freqItemSet) == 0:
        return None, None  # 如果没有元素项满足要求，则退出
    for k in headerTable: #'p': [2, None] -- element: [count, node]
        headerTable[k] = [headerTable[k], None] ## 初始化headerTable element: [count, node]
    
    '''treeNode是FP树中节点的类定义'''
    retTree = treeNode('Null Set', 1, None) 
    for tranSet, count in dataSet.items():
        # dataSet：[element, count]
        localD = {}
        for item in tranSet:
            if item in freqItemSet: # 过滤，只取该样本中满足最小支持度的频繁项
                localD[item] = headerTable[item][0] # element : count
        if len(localD) > 0:
            # 根据全局频数 对元素 从大到小对单样本排序  ['z', 'x', 'y', 's', 't', 'q']
            orderedItem = [v[0] for v in sorted(localD.items(), key=lambda p:p[1], reverse=True)]
            #(Dictionary) items() 函数以列表返回可遍历的(键, 值) 元组数组
            # 用过滤且排序后的样本更新树
            updateFPtree(orderedItem, retTree, headerTable, count)
    return retTree, headerTable

"""
构建FP树时需要的辅助函数：1.treeNode -- FP树中节点的类定义
2. updateFPTree 更新树
3. updateHeader 更新头指针表，确保节点链接指向树中该元素项的每一个实例
"""

'''1. FP树结点
   name存放结点名字，count用于计数，nodeLink用于连接相似结点（即图中箭头），parent用于存放父节点，用于回溯，
   children存放儿子结点（即图中实线）。disp仅用于输出调试。'''
minSup = 0
minPeopleCnt = 0
class treeNode:
    def __init__(self, nameValue, numOccur, parentNode):
        self.name = nameValue  # 节点名字
        self.count = numOccur  # 节点计数值
        self.nodeLink = None  # 用于链接相似的元素项
        self.parent = parentNode  # needs to be updated
        self.children = {}  # 子节点

    def inc(self, numOccur):
        #对count变量增加给定值
        self.count += numOccur

    def disp(self, ind=1): #仅用于输出调试 -- 参考网页
        print("  "*ind, self.name, " ", self.count)  #用'  '的数可代表第几层‘子集’
        for child in self.children.values():
            child.disp(ind+1)

    def findPattern(self, parentname='', minSupport=minSup, peopleCnt=minPeopleCnt):#递归寻找频繁项 -- 市民卡
        parentname = parentname + ',' + self.name
        print(parentname)
        for child in self.children.values():
            tmp = (parentname + ',' + child.name + ' ' + str(child.count)).replace(",Null Set,", '')
            if (child.count >= int(minSupport) and len(tmp.split(',')) >= int(peopleCnt)):
                patternLst.append(tmp.split(' '))
            child.findPattern(parentname)

"""
那么对于单个样本，FP树应该怎么生长呢？  递归。
    因为每个样本都是排序过的，频数高的频繁项集在前面，它总是更接近根结点，所以也可以把每个样本看成一棵子树，而我们要做的就是把子树添加到FP树里。
    因此每次只需判断第一个结点是否是根的儿子，若是则增加计数，若不是则增加分枝，然后递归调用构造FP树，传入第二个元素开始的子树即可。
    比如上例中往根节点∅增加样本(z,r)时，根没有z这个儿子，因此增加分支z。接着，只需递归地构造FP树，传入(r)，发现当前FP树∅-z也没有r这个儿子，因此增加分支r。最终递归返回，引入样本(z,r)后构造的FP树就是∅-z-r。
参数的传入：items 排序后的元素； inTreeFP 树结点的类传入;headerTable 为每种元素（的链表）设置一个头 ；count 集合中的样本数
"""

def updateFPtree(items, inTree, headerTable, count):
    if items[0] in inTree.children:  # 首先检查是否存在该节点
        inTree.children[items[0]].inc(count)  # 存在则计数增加
    else:  # 不存在则将新建该节点
        inTree.children[items[0]] = treeNode(items[0], count, inTree)#创建一个新节点
        if headerTable[items[0]][1] == None:  # 若原来不存在该类别，更新头指针列表
            headerTable[items[0]][1] = inTree.children[items[0]]#更新指向
        else:#更新指向
            updateHeader(headerTable[items[0]][1], inTree.children[items[0]])
    if len(items) > 1:  #仍有未分配完的树，迭代
        updateFPtree(items[1::], inTree.children[items[0]], headerTable, count)

def updateHeader(nodeToTest, targetNode):
    '''
    this version does not use recursion
    Do not use recursion to traverse a linked list!
    更新头指针表，确保节点链接指向树中该元素项的每一个实例
    '''
    while (nodeToTest.nodeLink != None):
        nodeToTest = nodeToTest.nodeLink
    nodeToTest.nodeLink = targetNode

"""
2. 从FP树挖掘频繁项集
2.1 从FP树提取条件模式基
2.2 用条件模式基构造FP树
2.3 重复1和2直到树只包含一个元素
""""
"""
2.1提取条件模式基
条件模式基（conditional pattern base）定义为以所查找元素为结尾的所有前缀路径（prefix path）的集合。我们要做的就是从header列表开始，针对每一个频繁项，都查找其对应的条件模式基。
代码实现查找以目标元素结尾的所有路径（条件模式基）
"""
# 递归回溯
def ascendFPtree(leafNode, prefixPath):
    if leafNode.parent != None:
        prefixPath.append(leafNode.name)
        ascendFPtree(leafNode.parent, prefixPath)

# 条件模式基
def findPrefixPath(basePat, myHeaderTab):
    treeNode = myHeaderTab[basePat][1] # basePat在FP树中的第一个结点
    condPats = {}
    while treeNode != None:
        prefixPath = []
        ascendFPtree(treeNode, prefixPath) # prefixPath是倒过来的，从treeNode开始到根
        if len(prefixPath) > 1:
            condPats[frozenset(prefixPath[1:])] = treeNode.count # 关联treeNode的计数
        treeNode = treeNode.nodeLink # 下一个basePat结点
    return condPats


#递归查找频繁项集
def mineFPtree(inTree, headerTable, minSup, preFix, freqItemList):
    # 最开始的频繁项集是headerTable中的各元素
    bigL = [v[0] for v in sorted(headerTable.items(), key=lambda p: p[1][0])] # 根据频繁项的总频次排序
    for basePat in bigL: # 对每个频繁项
        newFreqSet = preFix.copy()
        newFreqSet.add(basePat)
        freqItemList.append(newFreqSet)
        condPattBases = findPrefixPath(basePat, headerTable) # 当前频繁项集的条件模式基
        myCondTree, myHead = createFPtree(condPattBases, minSup) # 构造当前频繁项的条件FP树
        if myHead != None:
            # print 'conditional tree for: ', newFreqSet
            # myCondTree.disp(1)
            mineFPtree(myCondTree, myHead, minSup, newFreqSet, freqItemList) # 递归挖掘条件FP树

def fpGrowth(dataSet, minSup=3): # 主函数
    initSet = createInitSet(dataSet)
    myFPtree, myHeaderTab = createFPtree(initSet, minSup)
    freqItems = []
    mineFPtree(myFPtree, myHeaderTab, minSup, set([]), freqItems)
    return freqItems
