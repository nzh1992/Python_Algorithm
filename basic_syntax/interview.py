"""
created by nzh
Date: 2019/1/26 12:41 PM
"""

# python三元表达式
# 语法: result1 if <expression> else result2
# 如果expression表达式的结果为真，则返回result1，否则返回result2
# a = True if 1<2 else False
# print(a)


# 判断某个字符是否是大写字母
# string.isupper()
# is_upper = 'A'.isupper()
# print(is_upper)


# 随机打乱列表中的元素位置
# 可以使用random包中的shuffle函数
# import random
# l = [1,2,3,4,5]
# random.shuffle(l)
# print(l)


# join()函数和split()函数的区别
# char.join(string)是将一个字符char加入到一个string字符换中
# number_string = "12345"
# char = ','
# print(char.join(number_string))
# string.split(char)是用char来分隔string字符串, 结果生成一个list
# string = "fjkd,lsj,aigo"
# res = string.split(',')
# print(res)


# 使用多个变量并赋值
# a,b,c = (1,2,3)
# print(a,b,c)


# 使用集合删除list中重复元素
l = [1,1,2,3,2,2,4]
print(list(set(l)))

