"""
created by nzh
Date: 2019/4/21 2:00 PM
"""

# Python 3.6.6
# OS: Mac OSX 10.14.1

# 本章复习python中的变量

# 1.python中可以修改不可变变量么？
# 不可以，不可变对象一旦创建就不可修改，一旦尝试修改会引发TypeError异常。


# 2.a=1, b=2, 在不使用中间变量的情况下，交换a和b的值
# 第一种：使用python的解包
a, b = 1, 2
# a, b = b, a
# print(a, b)

# 第二种：求和
# a = a + b
# b = a - b
# a = a - b
# print(a, b)

# 第三种：按位异或
# 异或 ^: 规则是先将a，b转换为二进制，然后对应位置的二进制数字相同为0，不同为1
# 本题来看，2 -> 10, 1 -> 01, 1^2 = 11 = 3(十进制)
# a = a ^ b       # a = 11 = 3
# b = b ^ a       # b = 10 ^ 11 = 01 = 1
# a = a ^ b       # a = 11 ^ 01 = 10 = 2


# 3.阅读下面代码，写出A0~A6的最终值
A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), ('1', '2', '3', '4', '5')))
# print(A0)

A1 = range(10)
# print(A1)

A2 = [i for i in list(A1) if i in A0]
# print(A2)

A3 = [A0[s] for s in A0]
# print(A3)

A4 = [i for i in A1 if i in A3]
# print(A4)

A5 = {i: i * i for i in A1}
# print(A5)

A6 = [[i, i * i] for i in A1]
# print(A6)


# 4.思考下面代码的结果，并解释为什么？
l = []
a = {'num': 0}
for i in range(10):
    a['num'] = i
    l.append(a)

# print(l)
# 切记，操作可变对象时，对象的状态是动态变化的。


# 5.下面程序的输出
# # range(start_index, end_index, step)
# for i in range(5, 0, -1):
#     print(i)


# 6.4G的内存，如何读取5G的数据？
# 方法一：通过生成器，分多次读取，依次处理每次读取的数据
# 方法二：可以使用f.read(chunk_size)
# with open(file_path) as f:
#     f.read(chunk_size)
# 方法三：linux的split命令


# 7.如何判断两个对象是否指向同一块内存地址
# 只有赋值引用的时候才是True，否则为False
# a = [1,2,3]
# b = a
# print(a is b)
#
# c = [1,2,3]
# d = [1,2,3]
# print(c is d)


# 8. 如果只想判定两个对象的地址是否相同用id()


# 9. 浅拷贝
# 浅拷贝的特点是：虽然外层元素的地址不同(并非同一对象),但是内层元素是同一个对象。
# 但是浅拷贝有个问题，如果内层元素时一个嵌套可变对象(比如list),当修改这个可变对象时，也会引起改变。
# 浅拷贝有三种形式：
# 第一种：切片操作
# a = list(range(10))
# b = a[:]
# print(a, b)
# print(id(a), id(b))
# for i in a:
#     print(id(i), end=' ')
#
# print("")
# for i in b:
#     print(id(i), end=' ')

# 第二种：工厂操作
# b = list(a)

# 第三种：copy.copy()


# 10. 深拷贝
# 只有一种: copy.deepcopy()


# 11. 给定一个日期，判断是当年的第几天
# from datetime import date
#
# year, month, day = 2019, 2, 1
# d = date(year=year, month=month, day=day)
# d1 = d.timetuple()
# print(d1)
# print(d1.tm_yday)


# 12. os.path和sys.path
# os.path应用于系统文件路径的操作
# sys.path应用于python解释器环境参数的操作
# import os, sys
# print(os.path)
# print(sys.path)


# 13. python3中一些方法不在返回list对象，而是返回函数类对象
# 比如：dict的keys(), values(), items(), 还有zip(), map(), filter()
# 返回的对象可以通过list进行强转
d = {'a': 1, 'b': 2, 'c': 3}
# print(d.keys())
# print(list(d.keys()))
# print(d.values())
# print(list(d.values()))
# print(d.items())
# print(list(d.items()))


# 14. 检查文件类型
import io
# file = io.IOBase(__name__)
# print(file.writable())
# print(file.fileno())


# 15. 字典推导式
dict_conprehension = {key: value for (key, value) in [(1,2), (3,4)]}
print(dict_conprehension)


