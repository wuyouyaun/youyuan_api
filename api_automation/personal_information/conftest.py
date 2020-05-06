import pytest
import requests
from personal_information.common_fuction import login,update_info,get_info

@pytest.fixture(scope="session")
def login_fixture():
    print("\n输入账号密码先登录")
    s=requests.session()
    login(s,username="test",password="123456")
    yield s        #相当于return
    print("后置操作")
    s.close()     #关闭session




@pytest.fixture(scope="session")

def unLogin_fixture():
    print("\n不登录")
    s=requests.session()
    return s












