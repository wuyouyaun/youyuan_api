#coding:utf-8
import requests



# '''天气：输入正确的城市，key为空'''
# url="http://apis.juhe.cn/simpleWeather/query"
# params={
#     "city":"深圳",
#     "key":""
#
#
#         }
# r1=requests.get(url,params=params)
# print(r1.text)
# reason=r1.json()["reason"]
# print(reason)
# error_code=r1.json()["error_code"]
# print(error_code)
# assert reason=="错误的请求KEY"
# assert error_code==10001

'''天气：城市为空，key必传且正确'''
url="http://apis.juhe.cn/simpleWeather/query"
params={
    "city":"。。",
    "key":"5a731258401fc3af244873d094ac6564"


        }
r1=requests.get(url,params=params)
print(r1.text)
reason=r1.json()["reason"]
print(reason)
error_code=r1.json()["error_code"]
print(error_code)
assert reason=="暂不支持该城市"
assert error_code==207301

url="http://apis.juhe.cn/simpleWeather/query"
params={
    "city":"武穴",
    "key":"5a731258401fc3af244873d094ac6564"
        }
r1=requests.get(url,params=params,indent=4)
a=r1.text


reason=r1.json()["reason"]
print(reason)
error_code=r1.json()["error_code"]
print(error_code)
assert reason=="查询成功!"
assert error_code==0

















