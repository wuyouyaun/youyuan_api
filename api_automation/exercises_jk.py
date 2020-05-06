#coding:utf-8
import requests
s=requests.session()
url="http://49.235.92.12:9000/api/v1/login"
# h={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                 "Chrome/76.0.3809.100 Safari/537.36"}
# s.headers.update(h)
# print(h)

r=s.get(url)
#print(r.text)
print(s.headers)
# print(s.verify)
# s.verify=False
# print(s.verify)
# r1=s.get("https://www.baidu.com")
# print(r1)
