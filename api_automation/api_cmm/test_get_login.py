import requests
from api_cmm.commom_hfpt import loginQ,login,buyiness

def test_get_login01(login_fixture):
    s=login_fixture
    nm=buyiness(s,quantity="100")
    assert nm.json()["errorMsg"]== '请求成功'

def test_get_login02(login_fixture):
    s=login_fixture
    # r=loginQ(s,userName="KA600001")
    # salt=r.json()["data"]["salt"]
    # keys=r.json()["data"]["key"]
    # k=login(s,userKey=keys,salt=salt)
    # print(k.json())
    nm=buyiness(s,quantity="100",pickUpUserName="")
    assert nm.json()["errorMsg"]== "提货联系人{pickUpUserName}不能为空;"
