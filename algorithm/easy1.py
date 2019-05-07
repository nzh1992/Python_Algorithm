"""
created by nzh
Date: 2019/5/5 4:09 PM
"""
# 简单算法练习

# 1. 给定字典d={‘a’:24，’g’:52，’l’:12，’k’:33}
# 请按照value的升序进行排序，返回排序后的字典
def sort_dict(dictionary, asc=True):
    if asc:
        d = sorted(dictionary.items(), key=lambda x: x[1])
    else:
        d = sorted(dictionary.items(), key=lambda x: x[1])
        d = reversed(d)

    return dict(d)

# test case
# d = {'a': 24, 'g': 52, 'l': 12, 'k': 33}
# dict_sort_asc = sort_dict(d, True)
# dict_sort_desc = sort_dict(d, False)
# print(dict_sort_asc)
# print(dict_sort_desc)


# 2.反转字符串 'aStr'
def reverse_string1(string):
    """
    把string转为list，使用list的reverse()方法反转，最后用空字符串join拼接起来
    """
    string_to_list = list(string)
    string_to_list.reverse()
    return ''.join(string_to_list)

def reverse_string2(string):
    """
    使用切片反转
    """
    return string[::-1]

test_string = "string"
print(reverse_string2(test_string))
