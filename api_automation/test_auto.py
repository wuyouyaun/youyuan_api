#coding:utf-8


def test_func():
    print("hell,world")
    return

# print(test_func())

class TestDemo():


    def test_fun1(self):
        print("11111")

    def test_fun2(self):
        print("333333")
import requests





def qq_get(key,qq):
    url="http://japi.juhe.cn/qqevaluate/qq"
    par = {
    "key": key,  # appkey需要注册申请
    "qq":  qq
    }
    r=requests.get(url,params=par)
    print(r.text)
    return r

    # error_code=r.json()["error_code"]
    # # print(error_code)
    # reason=r.json()["reason"]








def test_qq01():
    '''输入正确的QQ号，必填项为key，输入正确的keyid,请求成功'''

    r=qq_get(key="8dbee1fcd8627fb6699bce7b986adc45",qq="353558733")
    error_code=r.json()["error_code"]
    # print(error_code)
    reason=r.json()["reason"]
    # print(reason)
    assert error_code==0
    assert reason=="success"

def test_qq02():
    '''必填项为空，请求失败，提示：KEY ERROR'''
    r=qq_get(key="",qq="353558733")

    error_code=r.json()["error_code"]
    # print(error_code)
    reason=r.json()["reason"]
    # print(reason)
    assert error_code==10001
    assert reason=="KEY ERROR!"












