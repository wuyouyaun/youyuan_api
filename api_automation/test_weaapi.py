import requests

def wea_get(city,key):
    url="http://apis.juhe.cn/simpleWeather/query"
    params={
        "city":city,
        "key":key
            }
    r1=requests.get(url,params=params)
    print(r1.text)
    reason=r1.json()["reason"]
    print(reason)
    error_code=r1.json()["error_code"]
    print(error_code)
    return r1
    #print(r1)



def test_wea01():
    '''天气：输入正确的城市，key必传且正确'''
    r1=wea_get(city="武穴",key="5a731258401fc3af244873d094ac6564")
    # reason=r1.json()["reason"]
    error_code=r1.json()["error_code"]
    assert r1.json()["reason"]=="查询成功!"
    assert error_code==0

def test_wea02():
    '''天气：输入正确的城市，key为空'''
    r1=wea_get(city="武穴",key="")
    # reason=r1.json()["reason"]
    # print(reason)
    # error_code=r1.json()["error_code"]
    # print(error_code)
    assert r1.json()["reason"]=="错误的请求KEY"
    assert r1.json()["error_code"]==10001

def test_wea03():
    '''天气：城市为空，key必传且正确'''
    # url="http://apis.juhe.cn/simpleWeather/query"
    # params={
    #     "city":"。。",
    #     "key":"5a731258401fc3af244873d094ac6564"
    #
    #
    #         }
    # r1=requests.get(url,params=params)
    r1=wea_get(city="",key="5a731258401fc3af244873d094ac6564")
    assert r1.json()["reason"]=="城市不能为空或暂不支持该城市"
    assert r1.json()["error_code"]==207301


























