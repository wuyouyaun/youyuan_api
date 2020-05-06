#coding:utf-8
import requests
# '''输入正确的QQ号，必填项为key，输入正确的keyid,请求成功'''
# url="http://japi.juhe.cn/qqevaluate/qq"
# par = {
#     "key": "8dbee1fcd8627fb6699bce7b986adc45",  # appkey需要注册申请
#     "qq":  "353558733"
#     }
# r=requests.get(url,params=par)
# print(r.text)
#
# error_code=r.json()["error_code"]
# # print(error_code)
# reason=r.json()["reason"]
# # print(reason)
# assert error_code==0
# assert reason=="success"



'''必填项为空，请求失败，提示：KEY ERROR'''
url="http://japi.juhe.cn/qqevaluate/qq"
par = {
    "key": "",  # appkey需要注册申请
    "qq":  "353558733"
    }
r=requests.get(url,params=par)
print(r.text)

error_code=r.json()["error_code"]
# print(error_code)
reason=r.json()["reason"]
# print(reason)
assert error_code==10001
assert reason=="KEY ERROR!"

















