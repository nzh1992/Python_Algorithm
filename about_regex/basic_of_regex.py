"""
created by nzh
Date: 2019/3/18 10:01 AM
"""
import re


# python中的正则表达式
# 正则表达式，用一种描述性语言定义字符串的规则。


# 特别注意：
# python字符串中的特殊符号也需要转义，所以会在正则表达式中有一些不同，比如：
s1 = 'ABC\\-001'  # python字符串
s2 = 'ABC\-001'   # 对应的正则表达式

# 为了解决这种不匹配的情况，可以使用python的r前缀，表示原始字符串，禁止转义
s3 = r'ABC\-001'


# 现在可以开始使用re模块了
# re.match(regex, str)
# match方法判断regex和str是否匹配，如果匹配则返回一个Match对象，否则返回None。
regex1 = '^\d{3}\-\d{8}'
str1 = r'010-12345678'
is_match = re.match(regex1, str1)
# print(is_match)

# 常见判断格式
str2 = r'010-12345678'
regex2 = '^\d{3}\-\d{8}'
if re.match(regex2, str2):
    # print("is match, and you can process your logic in here")
    pass
else:
    # print("not match, process other logic")
    pass


# 切分字符串
# re.split(regex, str)
# re模块重写了字符串的split方法，更加智能和灵活
# 比如：'a b     c'
str3 = 'a b     c'
# str_split = str3.split(' ')
# print(str_split)        # output: ['a', 'b', '', '', '', '', 'c']
# str_re_split = re.split(r'\s+', str3)
# print(str_re_split)     # output: ['a', 'b', 'c']

# 对比：
# str.split(split_str) 方法只能指定某个字符串来切分字符串，格式固定，不够灵活
# re.split(regex, str) 方法可以指定分割符的格式，这里我们就指定了一个或者多个空格作为分隔符。

# 我们再来尝试一个较为复杂的例子
# 给字符串加入, 其实我们只需要重写我们正则表达式来匹配这种规则即可。
str4 = 'a b,,,   c , , d'
str_split = str4.split(',')
# print(str_split)
str_re_split = re.split(r'[\s\,]+', str4)
# print(str_re_split)


# 分组
# 用()表示组Group
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')

# m.groups()用来表示分组的内容，数据结构是元祖
# print(m.groups())

# 如果正则表达式中定义了组的概念，那么就可以在Match对象上使用group()方法提取出子串来。
# m.group(0) 获取原始字符串
# print(m.group(0))
# m.group(1) 获取第一个子串
# print(m.group(1))
# m.group(2) 获取第二个子串，以此类推...
# print(m.group(2))

# 当你只分了两个组，也就是只有两个子串的时候。
# 你如果查询了第三个子串会引发IndexError异常(no such group)
# print(m.group(3))


# 贪婪匹配 和 非贪婪匹配
# 所谓贪婪匹配就是尽可能多的匹配字符串，反之则是非贪婪匹配

# 贪婪匹配
m = re.match(r'^(\d+)(0*)$', '1023000')
print(m)
print(m.group(0), m.group(1), m.group(2))

# 非贪婪匹配(在+或*后面加个?)
m2 = re.match(r'^(\d+?)(0*)$', '1023000')
print(m2)
print(m2.group(0), m2.group(1), m2.group(2))

# 通过上述对比不难发现，贪婪匹配会把1023后面的000都匹配到第一组中了，所以第二组中没有任何内容
# 而非贪婪匹配则不同，它只匹配了1023部分放入第一组，把000放入了第二组中。


# 预编译
# 在python中使用re库时会干两件事：
# 1.编译正则表达式
# 2.用编译后的正则表达式匹配字符串

# 当一个正则表达式需要重复使用很多次的时候(几百次几千次甚至更多的时候)
# 我们可以先预编译该正则表达式，这样以后的步骤都不要编译了，直接进行匹配
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')

m3 = re_telephone.match('010-12345678')
print(m3.groups())

m4 = re_telephone.match('021-1234567')
print(m4.groups())
