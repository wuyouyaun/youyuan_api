import pytest
# from mysql_test.connect_my import configuration
import requests

# @pytest.fixture(scope="session")
#
# def connect_fixture():
#     print("连接数据库前先连接配置项")
#     db=configuration()
#     return db

@pytest.fixture(scope="session")
def unlogin_fixture():
    s=requests.session()
    return s

