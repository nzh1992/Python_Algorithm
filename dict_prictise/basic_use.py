"""
created by nzh
Date: 2018/9/22 下午7:41
"""


# dict基本用法
student = {
    "name": "nzh",
    "age": 18,
    "sex": "man",
    "address": "Qiqihaer"
}

# 查看dict的所有方法
print(dir(dict))


# clear()，清除所有key-value键值对
# 改变字典，返回值为None
# student.clear()
# print(student)    # output: {}


# copy()
# 返回student的浅拷贝副本
student1 = student.copy()
# print(student1)


# fromkeys(seq[, value]), 类方法
# 通过传入一个序列seq来初始化一个字典，这个seq的每个元素会作为dict的key
# value是可选参数，作用是为每个键都赋值
student2 = dict.fromkeys('abc')
student2 = dict.fromkeys({'a':1, 'b': 2, 'c': 3})
student2 = dict.fromkeys(['aa', 'bb', 'cc', 12.56])
student2 = dict.fromkeys(('aa', 'bb', 12))
# 如果通过传入一个集合来初始化的话，那么key的顺序是随机的
student2 = dict.fromkeys({'a', 'b', 'c'}, 666)
# print(student2)     # output: {'a': 666, 'c': 666, 'b': 666}


# get(key, error_message)，读取某个key对应的值
# 如果没有这个key，默认返回None，可以再传入一个字符串，表示错误信息
key = student1.get('name', 'key not exist')
# print(key)    # output: nzh
key = student1.get('a', 'key not exist')
# print(key)      # output: key not exist


# items(), 查看所有key-value，返回一个可遍历的(key, value)元组的数组
# 结构是：[(key1, value1), (key2, value2)]
# print(student1.items())   # output: dict_items([('name', 'nzh'), ('age', 18), ('sex', 'man'), ('address', 'Qiqihaer')])

# dict.items()可以用来遍历字典
for k, v in student1.items():
    # print("key:", k, ", value:", v)
    pass


# keys()，获取dict所有key。
# 返回一个dict中所有key组成的list
keys = student1.keys()
# print(keys)       # output: dict_keys(['name', 'age', 'sex', 'address'])


# pop(key)，弹出组key-value，返回修改后的dict
student1.pop('name')
# print(student1)     # output: {'age': 18, 'sex': 'man', 'address': 'Qiqihaer'}


# popitem()，弹出末尾的一对key-value
# 当dict为空时，调用popitem函数会报KeyError错误，提示dictionary is empty
student1.popitem()
# print(student1)     # output: {'age': 18, 'sex': 'man'}

# {}.popitem()


# setdefault(key, value)，设置或者获取键的值
# 当key存在于dict中时，返回key对应的value
# 当key不存在与dict中时，返回参数value的值
value = student1.setdefault("phone", "13811112222")
# print(value)     # output: 13811112222
value = student1.setdefault("age", 30)
# print(value)     # output: 18


# dict1.update(dict2)，把dict2中的key-value键值对，添加到dict1的末尾
dict2 = {"university": "SWUN"}
student1.update(dict2)
# print(student1)     # output: {'age': 18, 'sex': 'man', 'phone': '13811112222', 'university': 'SWUN'}


# values()， 返回所有key所对应的value
values = student1.values()
print(values)       # output: dict_values([18, 'man', '13811112222', 'SWUN'])