"""
created by nzh
Date: 2019/2/27 11:01 PM
"""

# set, 集合的基本用法

# 1. 创建集合，由于set的特性是无序，不重复的，所以会自动帮你去除重复的项
# 创建空集合使用set()，而不能使用{}，以内{}表示一个空字典。
s = {1, 2, 2, 3, 4}
# print(s)

# 2. 获取集合的长度
s_length = len(s)

# 3. 判断某一项是否在集合中，使用in运算符
if 2 in s:
    pass

# 4. 遍历集合
# 由于set是无序的，所以遍历的顺序取决于集合的类型
for i in s:
    pass

# 5. 获取集合的字符串表示
# 结果是这样的：'{1, 2, 3, 4}'
str_set = str(s)

# 6. 比较两个集合是否相等
s1 = {1, 2, 3}
s2 = {3, 2, 1, 4, None}
# print(s1 == s2)


# 7. 连接两个集合
s3 = s1 and s2
# print(s3)

# 8. 插入一项
s1.add(5)

# 9. 删除一项
s1.remove(5)

# 10. 去交集
s4 = {1, 2, 3}
s5 = {2, 4}
# print(s4 - s5)

# 11. 类型转换
# set -> list
s6 = list(s5)
# set -> tuple
s7 = tuple(s5)


