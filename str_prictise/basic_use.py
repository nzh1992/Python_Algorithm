"""
created by nzh
Date: 2018/9/22 下午11:44
"""

# 字符串str，基本用法
# 查看所有str的所有方法
print(dir(str))


# capitalize()
# 把str中的首字母变为大写，其他字母变成小写
# 返回值为修改后的str
str1 = "helLo woRld"
# print(str1.capitalize())  # output: Hello world


# casefold()
# 把str中的每个字母变成小写的
str2 = "PYTHON"
# print(str2.casefold())      # output: python

# lower()
# 把str中的每个字母变成小写的
# print(str2.lower())         # output: python

# 可以看到lower函数和casefold函数功能基本上是一样的，那么他们有什么区别呢？
# lower函数只是针对ASCII有效，处理场景是英语和汉语。
# casefold函数可以将所有语言转换成小写，一般在国际化时会比lower更有用。


# center(width[, fillchar])
# width表示总宽度，fillchar表示要填充空余的位置的字符，默认是空格
# 返回一个总长度确定的新的str，让原来的str居中，其余的位置可以用指定字符填充。
str3 = "HTML"
# print(str3.center(10, '*'))     # output: ***HTML***

# 如果给定的width小于字符串的长度，那么就不会填充，仅仅返回原有字符串
# print(str3.center(1, '*'))      # output: HTML


# count(substr[, start[, end]])
# 返回substr出现的次数。注意区分大小写。
# start和end为可选参数，分别表示搜索的起始位置和结束位置
str4 = "HHHTTML"
# print(str4.count('H'))    # output: 3


# encode(encoding[, errors])
# 给字符串指定一种编码格式，默认格式是utf-8，errors表示自定义错误提示。
# print(str4.encode('utf-8', errors="编码错误"))    # output: b'HHHTTML'
# print("中国".encode('utf-8', errors="编码错误"))   # output: b'\xe4\xb8\xad\xe5\x9b\xbd'
# print("中国".encode('utf-8'))
# print(type("中国".encode('utf-8')))


# endswith(suffix[, start[, end]])
# 判断str是否以suffix结尾
# start和end表示搜索范围
str5 = "I'm a programmer"
is_suffix = str5.endswith("mmer")
# print(is_suffix)      # output: True


# expandtabs([tabsize=8])
# 把str中的'\t'转换成空格。
# tabsize表示把\t换成几个空格，0就是没有空格，默认是8个空格。
str6 = "\tabcd\tefg\thigk\tlmnabc"
re = str6.expandtabs(tabsize=1)
# print(re)     # output:  abcd efg higk lmn


# find(sub[, start[, end]])
# 查找str中的sub子字符串，如果存在则返回子字符串的第一个字符的索引，不存在返回-1
# 如果存在多个相同的sub，那么返回第一个sub的第一个字符的索引。
index = str6.find('l')
# print(index)        # output: 15
index = str6.find('abc')
print(index)


# 字符串中的占位符
# 可以替代变量在str中的位置。
age = 18
# print("your age is %d" %age)      # output: your age is 18


# format()
# python3中更常用的一种格式化字符串的函数
# 第一种用法，位置映射，按照一对一的顺序映射到{}中
str7 = "{} is a {}".format('mike', 'coder')
# print(str7)       # output: mike is a coder
# 第二种用法，索引映射，按照format中参数的索引映射到{}
str8 = "{0} is a {1}".format('mike', 'coder')
# print(str8)       # output: mike is a coder
# 第三种关键字映射
str9 = "{name} is a {position}".format(name="mike", position="coder")
# print(str9)         # output: mike is a coder
# format还支持传入其他参数，比如说tuple
str10 = "{0[0]} is a {0[1]}".format(('mike', 'coder'))
# print(str10)        # output: mike is a coder
# format还支持填充对齐
# 比如2*3=6，我们想让结果6变成06(这是右对齐)
str11 = "{0}*{1}={2:0>2}".format(2, 3, 2*3)
# print(str11)        # output: 2*3=06
# 也可以左对齐，就拿浮点数来说，299.99一共是6个字符(算上小数点)
# 要显示小数点后4位，不足的补0，那么应该左对齐9位
str12 = "the clothes' price is {0:0<9}".format('299.99')
# print(str12)      # output: the clothes' price is 299.99000

# 更方便的做法是使用占位符%f
price = 299.99
str13 = "the clothes' price is %.4f" %price
# print(str13)      # output: the clothes' price is 299.9900
# format函数也支持指定精确度
str14 = "the clothes' price is {:.4f}".format(299.99)
# print(str14)        # output: the clothes' price is 299.9900


# format_map()  # TODO
str13.format_map()
