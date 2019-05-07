"""
created by nzh
Date: 2019/4/21 2:19 PM
"""

# 1.zip函数
# 将两个list中的元素打包成tuple，最终返回一个zip对象
# python2中返回的是list, 而python3返回的是一个zip对象，可以使用list()构造函数转为list

# 当list1和list2中的元素个数相同时
list1 = [1, 2, 3, 4]
list2 = [6, 7, 8, 9]
zip_list = zip(list1, list2)
# print(zip_list)
# print(list(zip_list))

# 当list1和list2中元素个数不相同时
# zip()返回的元素个数，是list元素个数最小的那个
list3 = [1, 2, 3]
list4 = [1, 4]
zip_list2 = zip(list4, list3)
# print(list(zip_list2))

# 使用*zip_list可以解压，返回二维矩阵
zip_ele = [*zip_list]
# print(zip_ele)


zip_dict = dict(zip_list2)
# print(zip_dict)


# 2.range()
# python2中range()函数可以创建一个整数列表
# python3中range()函数返回一个range对象，可以将range对象转化为list，tuple，set对象
r = range(10)
# print(type(r))
# print(list(r))
# print(set(r))
# print(tuple(r))


# 3.range()和xrange()的区别
# 只有python2中，这两个方法共存。
# 区别在于，range()函数返回一个整数列表，xrange()函数返回一个生成器


# 4.random.shuffle()
# shuffle()函数用于将所有元素随机排序
# 注意，并非返回一个新对象，而是打乱原有序列
# import random
#
# l = [1, 2, 3, 4, 5, 6, 7]
# random_list = random.shuffle(l)
# print(l)


# 5. map()
# map(function, iterable)


# 6. filter(function, iterable)
origin_list = [1, 2, 3, 4, 5, 6, 7]


def is_in_small_list(element):
    if element not in [1, 2, 3]:
        return element


new_list = filter(is_in_small_list, origin_list)
# print(list(new_list))

# 7. reduce()
# python2中为内置函数，python3被放入了functools库
from functools import reduce

r = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(r)