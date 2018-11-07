"""
created by nzh
Date: 2018/9/25 上午12:44
"""
import re

# 针对任意多的分隔符拆分字符串
# 使用re.split()
line = "dafd fjkl; jkljk, jkljkl,jkljl,     foo"
result = re.split(r'[;,\s]\s*', line)
# print(result)

# 括号捕捉器
result = re.split(r'(;,\s)\s*', line)
# print(result)

# 检查字符串是否以substr开头
url = "http://www.baidu.com/v2/apps"
is_http = url.startswith('http')
print(is_http)

