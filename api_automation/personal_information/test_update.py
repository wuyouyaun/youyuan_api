from personal_information.common_fuction import login,update_info,get_info
import requests
# s=requests.session()
# def setup_module():   #模块级别
#     """前置操作，整个模块开始用例前只执行一次"""
#     login(s)
#     print("前置操作，整个模块开始用例前只执行一次")
# def setup_function():        #函数级别，前置操作
#     print("前置操作，每个用例前只执行一次")
#
# def teardown_function():     #函数级别，后置操作
#     print("后置操作，每个用例前只执行一次")
#
# def teardown_module():
#     print("后置操作，整个模块开始用例前只执行一次")
def test_get_info(login_fixture):
    #s=requests.session()
    """成功"""
    # login(s)  # 登录
    s=login_fixture
    infos=update_info(s,name="test",mail="99999999@qq.com")  #修改
    print(infos)
    assert infos['data']['mail']=='99999999@qq.com'
    #assert get_in['data'][0]['mail']=='99999999@qq.com'
def test_get_info_1(login_fixture):
    """修改他人信息"""
    #s=requests.session()
    # login(s)  # 登录
    s=login_fixture
    infos=update_info(s,name="yyyy",mail="99999999@qq.com")  #修改
    print(infos)
    #get_in=get_info(s)     #查询
    #print(get_in)
    assert infos['message']=='无权限操作'
#assert get_in['data'][0]['mail']=='99999999@qq.com'



