import requests
from commodity.login import login_znw,add_personal,add_acconut
import pytest
import os
from commodity.read_yaml import yaml_path
curpath=os.path.dirname(os.path.realpath(__file__))
curpathread=os.path.join(curpath,"tes_dem.yml")
yamldata=yaml_path(curpathread)['tes_add_acconut1']
print(type(yamldata))
def test_login(login_fixture):
    #s=requests.session()
    s=login_fixture
    print(s.headers)
    login_q=login_znw(s,name="zhaolei",password="123456a")
   # login_q=login_q.json()
    #print(login_q.json())
    assert login_q.json()['succeed']==True
    assert login_q.json()['errorCode']==""


def test_add_personal(login_fixture):
    #s=requests.session()
    #login_znw(s)
    s=login_fixture
    add_person=add_personal(s,userId=1000005635)
    print(add_person.json())
    assert add_person.json()['succeed']== True
    assert add_person.json()['data']==""

@pytest.mark.skip("待开发，等修复")
def test_ces():
    print("待开发")
# test_datas=[
#             ("测试5",True),
#             ("测试6",True),
#             ("测试5",)
#                     ]

@pytest.mark.parametrize("accountAlias,phone,expected",
                         yamldata,
                         ids=[
                             "修改个人信息sex=M,成功",
                             "修改个人信息sex=F,成功",
                             "修改个人信息sex=V,异常场景"
                              ]
                        )
def test_add_acconut(login_fixture,accountAlias,phone,expected):
    #s=requests.session()
    #login_znw(s)
    s=login_fixture
    add_account1=add_acconut(s,accountAlias=accountAlias,phone=phone)
    print("11111")
    print(add_account1.json())

    assert add_account1.json()["succeed"]==expected
    # assert add_account1.json()[]

