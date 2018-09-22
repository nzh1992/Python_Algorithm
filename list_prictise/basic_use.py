"""
created by nzh
Date: 2018/9/21 上午11:00
"""

# 创建数组
# 1. []
list1 = []

# 2. list(iteralbe)
# 给list函数传入一个可迭代变量，iterable可以是str，list，dict，set, tuple
# 如果传入dict，那么dict的所有key会被提取到数组中
list2 = list(set((1, 2, 3)))
list2 = list({'a': 1, 'b': 2})  # output: ['a', 'b']
list2 = list('abc')
list2 = list((1,2,3))

# 3. 列表生成式
list3 = [i for i in 'abc']
# 列表生成式还可以加入筛选条件,比如过滤掉了'a'和'c'
list3 = [i for i in 'abc' if i not in ['a', 'c']]


# 创建二维数组
list4 = ['a'] * 3   # output: ['a', 'a', 'a']
list4 = [{'a': 1, 'b': 2}] * 3  # output: [{'a': 1, 'b': 2}, {'a': 1, 'b': 2}, {'a': 1, 'b': 2}]
list4 = [[]] * 3    # output: [[], [], []]
# 由于内部的[]会被浅赋值，所以当修改其中一个元素时，其他[]也会被修改。
list4[0].append(3)  # output: [[3], [3], [3]]
# 可以使用列表生成式
# for循环表示迭代的次数，[]表示生成的结果
list4 = [[] for i in range(3)]
list4[0].append(1)
list4[1].append([1,3])

list4 = [[0] * 3 for i in range(4)]  #output: [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
list4[1].remove(0)


###################################################
# 查看python列表的内置函数
built_in_function_list = dir(list)
print(built_in_function_list)


# 1. append，在list的末尾添加一个元素
# append函数的返回值是None，函数会直接改变list的值
list5 = [1, 2, 3]
appended_list = list5.append(4)
# print(list5)  # output: [1, 2, 3, 4]
# print(appended_list)  # output: None


# 2. clear，清空list
# clear函数的返回值为None
clear_list = list5.clear()
# print(list5)    # output: []
# print(clear_list)   # output: None


# 3. copy，对list进行浅复制
list6 = [{'a': 2}, 3, '4', 5.1234, [7, 7, 8]]
shadow_copy = list6.copy()
# print(list6)  # output: [{'a': 2}, 3, '4', 5.1234, [7, 7, 8]]
shadow_copy.append(9)
shadow_copy[0] = 1
# print(shadow_copy)    # output: [1, 3, '4', 5.1234, [7, 7, 8], 9]
shadow_copy[4].append(10)
# print(shadow_copy)      # output: [1, 3, '4', 5.1234, [7, 7, 8, 10], 9]


# count，计算list中某个元素出现的次数
# 传入一个值，返回list中这个值的个数
list7 = [[1] * 3, [2] * 2,  [1], [1], [1] * 3]
# print(list7)  # output: [[1, 1, 1], [2, 2], [1], [1], [1, 1, 1]]
# print(list7[0].count(1))  # output: 3


# extend(iterable)，扩展列表
# extend接受一个可迭代对象，并将可迭代对象的每一个元素依次添加到list中
# 如果iterable是dict，那么会依次添加dict的key到list中
list8 = [1, 2, 3, 4]
list8.append('abc')
# print(list8)  # output: [1, 2, 3, 4, 'abc']
list8.extend(['def'])
# print(list8)  # output: [1, 2, 3, 4, 'abc', 'def']
list8.extend('ipo')
# print(list8)    # output: [1, 2, 3, 4, 'abc', 'def', 'i', 'p', 'o']
list8.extend({'name': 'nzh', 'age': 18})
# print(list8)      # output: [1, 2, 3, 4, 'abc', 'def', 'i', 'p', 'o', 'name', 'age']


# index(element, start, stop)，返回element在list中的索引
list9 = [1, 2, 3, 4]
index = list9.index(4)
# index函数还有其他参数start和end，用来指定索引的搜索范围
# 包括start索引，但是不包括end索引，区间是左闭右开
# 如果没有找到element，就会引发ValueError异常，提示：element is not in list
list10 = [1, 2, 3, 5, 4, 3, 2, 4, 1]
index = list10.index(1, 7, len(list10))
# print(len(list10))
# print(index)      # output: 8


# insert，在指定索引的地方添加元素，返回插入element之后的list
list11 = [1, 2, 3, 4, 5, 6, 7]
list11.insert(3, 100)
# print(list11)     # output: [1, 2, 3, 100, 4, 5, 6, 7]


# pop(index)，弹出指定索引处的元素
# 从list11中弹出最后一个元素
list11.pop(-1)
# print(list11)       # output: [1, 2, 3, 100, 4, 5, 6]


# remove(value), 删除指定的元素
# 函数返回None
list11.remove(1)
# print(list11)       # output: [2, 3, 100, 4, 5, 6]
# 当列表中有多个重复元素value时，删除第一个value
list12 = [1, 2, 1, 1]
list12.remove(1)
# print(list12)       # output: [2, 1, 1]
# 当删除一个不存在的value时，抛出ValueError异常，提示x not in list
# list12.remove(4)    # raise Exception: ValueError


# reverse()，颠倒list中的元素
# 改变原始list，返回None
list13 = [1, 2, 3, 4]
list13.reverse()

# 其他逆转list的方法
# 比如内置的reversed(list)函数，会return一个list_reverseiterator类型的对象
# 可以使用for或者列表生成式，再或者list()来生成一个新的list
# print([i for i in reversed(list13)])    # output: [1, 2, 3, 4]
# print(reversed(list13))                 # output: <list_reverseiterator object at 0x1006d95c0>
# print(list(reversed(list13)))           # output: [1, 2, 3, 4]

# 除了上述操作，使用list的切片属性也能完成list反转
# print(list13[::-1])                     # output: [1, 2, 3, 4]


# sort()，对list按照升序排序
list14 = [1, 3, 2, 1, 5, 4]
list14.sort()
# print(list14)     # output: [1, 1, 2, 3, 4, 5]
# 降序排序
list14.sort(reverse=True)
# print(list14)     # output: [5, 4, 3, 2, 1, 1]