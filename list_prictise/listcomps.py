"""
created by nzh
Date: 2018/11/11 下午3:55
"""

# 列表推导式，list comprehension
# 简称listcomps
x = 'ABC'
dummy = [ord(x) for x in x]
print(x)
print(dummy)


# 使用列表推导式，生成笛卡尔积
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)


# 生成器表达式
# 生成器表达式和列表推导式十分类似，只不过把[]换成()


