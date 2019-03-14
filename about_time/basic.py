"""
created by nzh
Date: 2019/3/14 11:01 AM
"""
# 关于python中的时间
# python内置了time，datetime, calendar模块
# 第三方包有pytz
# 常见类型有UTC，GMT。
# 下面是这些有关时间以及时区的一些常见用法


# 概念：
# 理想时间(naive-time): 认为一天就是24 * 60 * 60秒
# 真实时间(real-time): 真实情况是还需考虑到闰秒，以GMT换算而来。
# 夏令时：
# 每年从4月中旬第一个星期日的凌晨2点(北京时间),将时钟拨快1小时。
# 到每年9月中旬第一个星期日的凌晨2点(北京时间),将时钟回拨1小时。
# 时间戳：
# 一个能表示一份数据在某个特定时间之前已经存在的，完整的，可验证的数据.
# 通常是一个字符串序列，唯一地标识某一刻的时间。
# 具体是指 格林威治时间(1970年1月1日0时0分0秒)(北京时间1970年1月1日8时0分0秒)
# 到现在的总秒数。


import time
import datetime
import calendar
import pytz

# 获取当前时间戳
current_time_stamp = time.time()
print(current_time_stamp, type(current_time_stamp))


# 时间元组
# 很多python函数用一个元组将9组数字包起来，用来处理时间.
# 格式：(4位年份, 月, 日, 时, 分, 秒, 周几, 本年第几天, 夏令时)
# struct_time = (tm_year, tm_mon, tm_day, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst)

# 把时间戳转为时间元组
localtime_tuple = time.localtime(time.time())
print(localtime_tuple, type(localtime_tuple))

# 从一个时间元组中获取可读的时间模式
localtime_readalbe = time.asctime(localtime_tuple)
print(localtime_readalbe, type(localtime_readalbe))

# 格式化日期
localtime_format = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
print(localtime_format, type(localtime_format))

# time.clock()用户衡量不同程序的耗时，返回的是cpu时间
clock_time = time.clock()
print("clock_time:", clock_time)

# 获取gmt,time.gmtime(float), 返回struct_time格式
gmt = time.gmtime()
print("gmt:", gmt)

# 获取当地时间, time.lcoaltime(s)，返回struct_time格式
localtime_gmt = time.localtime()
print("本地gmt:", localtime_gmt)

# 时间元组 转 时间戳
time_stamp = time.mktime(time.localtime())
print("时间戳:", time_stamp)
