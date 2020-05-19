import pytest
# from mysql_test.connect_my import inquire,configuration
from mysql_test.connect_my import execute_sql
from mysql_test.common_fuction import register
from mysql_test.connect_my import execute_sql
# def test_inquire(connect_fixture):
#     db=connect_fixture
#     # print("1111")
#     # print(db)
#     cursor=db.cursor()
#    # print(cursor)
#     sql="select * from uc_users_full"
#     inquires=inquire(cursor=cursor,sql=sql)
#     print(inquires)
@pytest.fixture(scope="function")
def delete_register():
    '''执行删除操作'''
    sql='DELETE from auth_user WHERE username = "test335";'
    execute_sql(sql)
    yield
    print("后置操作处理")

def test_register(unlogin_fixture,delete_register):
    s=unlogin_fixture
   # register(s)
    r=register(s)
    # print(r)
    assert r.json()['msg']=='注册成功!'
    assert r.json()['code']==0

def test_register1(unlogin_fixture,delete_register):
    s=unlogin_fixture
    r=register(s)
    print(r.json())
    assert r.json()['msg']=='注册成功!'
    assert r.json()['code']==0
    r2=register(s)
    assert '用户已被注册'in  r2.json()['msg']
    assert r2.json()['code']==2000




