"""
created by nzh
Date: 2018/9/21 上午11:01
"""

from datetime import datetime

# 检测函数运行时间
def consume_time(func):
    starttime = datetime.now()
    func()
    endtime = datetime.now()
    print("{0}函数执行了{1}秒", str(func), str(starttime-endtime))