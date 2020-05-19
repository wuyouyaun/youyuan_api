import pytest
import requests
from commodity.login import login_znw


@pytest.fixture(scope="session")
def login_fixture():
    """登录后台"""
    print('先前登录')
    s=requests.session()
    login_znw(s)
    yield s
    print("\n后置登录")
    s.close()
    #print("后置条件")
    #print("xxxx")