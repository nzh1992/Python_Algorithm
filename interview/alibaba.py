"""
created by nzh
Date: 2019/5/13 5:35 PM
"""

# 1.尽量列举python列表的成员方法，并给出下列操作的答案
a = [1, 2, 3, 4, 5]
# print(a[::2])     # output: [1, 3, 5]
# print(a[-2:])     # output: [4, 5]

# list切片语法是list[start:end:step],step为间隔，默认是1，如果负数代表逆向。

# 2.一行代码实现对列表a中的偶数位置的元素进行加3后求和。
total = sum([a[i] + 3 for i in range(len(a)) if i % 2 == 0])
# print(total)

# 3.将列表a的顺序打乱，再对列表a进行排序得到列表b，然后把a和b按顺序进行构造一个字典d
from random import shuffle
from copy import deepcopy


def build_dict(a):
    raw_a = deepcopy(a)
    shuffle(a)
    b = sorted(a)
    return {a[i]: b[i] for i in range(len(a))}


# d1 = build_dict(a)
# print(d1)

# 本题考察random.shuffle()函数用法，shuflle函数会改变原始list，而非返回一个新的list，所以需要拷贝原始list
# 如果参数a中的元素有可变对象，应该使用深拷贝。


# 4.实现统计一篇英文文章内每个单词的出现频率，并返回出现频率最高的10个单词以及其出现次数。并解答以下问题。
article_content = """
Make an iterator that aggregates elements from each of the iterables.

Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator. Equivalent to:
"""

# 方法一：借助collections.Counter.most_common()函数
from collections import Counter
import re


def get_most_freqency_word(content):
    count = Counter(re.split(r'\W+', article_content))
    result = count.most_common(10)

    return result


# r = get_most_freqency_word(article_content)
# print(r)


# 5.解释文件对象f的readlines和xreadlines的区别？
# file_path = '/Users/nzh/Desktop/test.txt'
# with open(file_path, 'r') as f:
#     # content = f.readlines()
#     content = f.xreadlines()
#
# print(content)


# 6.使用多线程/单线程抓取网页程序，并对性能进行分析

# 单线程
import time
import requests


def get_page(url):
    rep = requests.get(url)
    content = rep.content


def main1():
    start_time = time.time()
    url = "http://www.baidu.com"
    for i in range(100):
        get_page(url)

    print("爬取100次，共耗时{}秒".format(time.time() - start_time))


# 多线程(非线程池)
import threading


def main2():
    start_time = time.time()
    url = "http://www.baidu.com"
    for i in range(100):
        t = threading.Thread(target=get_page, args=(url,))
        t.start()
        t.join()

    print("爬取100次，共耗时{}秒".format(time.time() - start_time))


# 多线程(线程池)
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED


def main3():
    start_time = time.time()
    url = "http://www.baidu.com"
    executor = ThreadPoolExecutor(max_workers=10)
    all_task = []
    for i in range(100):
        all_task.append(executor.submit(get_page, (url)))

    wait(all_task, return_when=ALL_COMPLETED)
    print("爬取100次，共耗时{}秒".format(time.time() - start_time))


# 7.实现一个线程安全的单例模式
# 使用装饰器实现
def singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)

        return _instance[cls]

    return _singleton


@singleton
class A(object):
    def __init__(self, x=0):
        self.x = x
