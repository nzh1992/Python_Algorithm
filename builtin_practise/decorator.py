# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2020/9/3
Last Modified: 2020/9/3
Description: 学习装饰器
"""

import time
from functools import wraps


def timethis(func):
    """
    Decorator that reports the execution time.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, f"{end - start}s")
        return result

    return wrapper


@timethis
def test_func(a,b):
    print("start..")
    print("param:", a, b)
    time.sleep(3)
    print("end...")


test_func(5, 10)