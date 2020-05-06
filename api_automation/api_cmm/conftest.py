import requests
import pytest
from api_cmm.commom_hfpt import loginQ,login,buyiness



@pytest.fixture(scope="session")
# def loginQ_fixture():
#     '''登录前获取的key'''
#     s=requests.session()
#     loginQ(s)
#     return s
def login_fixture():
    '''登录用的加密账号和密码'''
    print("输入账号先登录")
    s=requests.session()
    r=loginQ(s,userName="KA600001")
    salt=r.json()["data"]["salt"]
    keys=r.json()["data"]["key"]
    k=login(s,userKey=keys,salt=salt)
    return s



