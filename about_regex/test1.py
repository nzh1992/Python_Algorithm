"""
created by nzh
Date: 2019/3/18 4:30 PM
"""
import requests

# test marathon put api
# url = 'http://172.16.5.11:8080/v2/apps/msgldemo' + '?force=true'
# data = {'instances': 0}
#
# reponse = requests.put(url, json=data)
# print(reponse.status_code, '\n', reponse.content)


# test function
import time
from datetime import datetime

struct_time = time.gmtime(1498521600)
naive_time = datetime.fromtimestamp(1498521600)
print(naive_time)