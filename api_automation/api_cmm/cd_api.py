#coding:utf-8
import requests

def login():
    url="http://49.235.92.12:8080/zentao/user-login.html"
    body={
        "account":"admin",
        "password":"Yoyo123456",
        "passwordStrength":"1",
        "referer":"/zentao/",
        "verifyRand":"1905733664",
        "keepLogin":"1"
            }
    s=requests.session()
    r=s.post(url,data=body)
    print(r.text)

def test_xingz01(s):
    url="http://web.juhe.cn:8080/constellation/getAll?consName=%E7%8B%AE%E5%AD%90%E5%BA%A7&type=" \
        "today&key=cde5e16435cd0217f505a88898b60707"
    r=s.get(url)
    assert r.json()["error_code"]==0
    assert r.json()["resultcode"]=="200"

def test_xingz02(s):
    url2="http://web.juhe.cn:8080/constellation/getAll?consName=%E7%8B%AE%E5%AD%90%E5%BA%" \
         "A7&type=today&key="
    r=s.get(url2)
    print(r.text)
    assert r.json()["error_code"]==10001
    assert r.json()["reason"]=="KEY ERROR!"

def  test_xingz03(s):
    url3="http://web.juhe.cn:8080/constellation/getAll?consName=%AD%90%E5%BA%A7&type=today&key=cde" \
         "e16435cd0217f505a88898b60707"
    r=s.get(url3)
    print(r.text)
    assert r.json()["error_code"]==10001
    assert r.json()["reason"]=="KEY ERROR!"















