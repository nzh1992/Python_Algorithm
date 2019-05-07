"""
created by nzh
Date: 2019/3/18 11:50 AM
"""
import re


# regex = r'^(\w+)([:/w]?)/([a-zA-Z0-9\_]*)(:?[0-9a-zA-Z\_\-])$'
# regex = r'^\w+:5000/\w*:[0-9a-zA-Z\-]{1,14}$'
regex = r'^([\:\-\w]+)$'

str1 = "registry:5000/tranch_fdjskl:550"
str2 = "registry:5000/jifdsjaoj009kj:59-9fb5b87b98"

# m1 = re.match(regex, str2)
# print(m1.re)
# print(m1.string)
# print(m1.endpos)



regex2 = r'^([\w]+)([:]{1}[\d]{1,5}|)/([\w\_\-\/]+)([:]{1}[\w\-]{1,15}|)$'
# 正确例子
str3 = "registry:5000/jkljfdsl_fjkd/base"
str4 = "registry:5000/jklfdsjl/jfkldsj/jing"
str5 = "registry:5000/fjsdlajo-fkdlsj_jfkdl/jkljlj:10-fjdksljongw"
str6 = "registry/fjsdlajo-fkdlsj_jfkdl/jkljlj:10-fjdksljongw"
str7 = "bdperfregistry/fjsdlajo-fkdlsj_jfkdl/jkljlj:10-fjdksljongw"

# 错误的例子
str8 = "registry:/jkljfdsl_fjkd/base"
str9 = "registry5000/jklfdsjl/jfkldsj/jing"

m2 = re.match(regex2, str9)

assert m2

print("m2.gourps(): ", m2.groups())
print("m2.string: ", m2.string)
