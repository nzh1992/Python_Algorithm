"""
created by nzh
Date: 2019/3/21 11:53 AM
"""
import time


"""
time.localtime(second=None)用法
"""
# t1 = time.time()
# print("Unix timestamp:", t1)
# # 由于时间戳t1拿到的是一个float类型
# # struct_time接受的是一个11位的数字字符串，刚好是小数点前面的内容
# # 所以我们需要去掉小数点以及后面的内容
# struct_t1 = int(t1)
# struct_time = time.localtime(struct_t1)
# print(struct_time, type(struct_time))
#
#
# t2 = time.localtime()
# print(t2, type(t2))


"""
time.gmtime(second=None)用法
"""
# t3 = time.time()
# utc_time_struct = time.gmtime(t3)
# print(utc_time_struct, type(utc_time_struct))
# print(time.gmtime(), type(time.gmtime()))


"""
time.mktime(struct_time)用法
"""
# 将struct_time转为时间戳
# local_struct_time = time.localtime()
# time_stamp = time.mktime(local_struct_time)
# print(time_stamp, type(time_stamp))


"""
time.asctime(struct_time=None)用法
"""
# 传入一个struct_time对象，返回"Sun Jun 20 23:21:05 1993"这种格式的字符串
# 不传参数，返回当前时间的这种格式的字符串
# t4 = time.asctime()
# print(t4, type(t4))


"""
time.strftime(format[,  struct_time])用法
"""
# 用于格式化struct_time对象
t5 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(t5, type(t5))


"""
time.strptime(string[, format])用法
"""
# strftime()逆向操作，从字符串转为struct_time
# 如果你不传入format参数，那么将会采用默认格式%a %b %d %H:%M:%S %Y
# 如果不符合默认格式则会引发ValueError异常
# 所以，一般我们都会指定format，跟个跟具体的需求而定
# time_str = "2019-08-02 18:49:00"
# format = "%Y-%m-%d %H:%M:%S"
# t6 = time.strptime(time_str, format)
# print(t6, type(t6))



