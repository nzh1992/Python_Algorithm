"""
created by nzh
Date: 2019/5/13 10:08 AM
"""

# 迭代器协议
# 对象提供next方法，要么返回迭代器的下一项，要么引发StopIteration异常，终止迭代。


# 生成器
# 1.生成器函数
# 2.生成器表达式

def gen_squares(n):
    for i in range(n):
        yield i ** 2


# for i in gen_squares(5):
#     print(i)

# gen_obj = gen_squares(5)
# print(gen_obj)
#
# print(gen_obj.__next__())
# print(next(gen_obj))
# print(next(gen_obj))
# print(next(gen_obj))
# print(next(gen_obj))
# print(next(gen_obj))


