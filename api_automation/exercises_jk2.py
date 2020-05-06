#coding:utf-8
import requests
url="http://49.235.92.12:9000/admin/login/"
s=requests.session()
# 模拟第一次打开登录页面
r1=s.get(url)
print(r1.text)
import re
#获取页面隐藏参数csrf_token
csrf_token=re.findall("name='csrfmiddlewaretoken' value='(.+?)' />",r1.text)
print(csrf_token[0])

print(s.cookies)
print(dict(s.cookies))

# body={"username":"test",
#       "password":"123456",
#       ""
import re
a="hello_world"

newq=re.findall(r'o_(.+?)$',a)
print(newq)



