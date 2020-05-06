from personal_information.common_fuction import login,update_info,get_info
import requests

def test_get_info():
    s=requests.session()
    login(s)  # 登录
    infos=update_info(s,name="test",mail="99999999@qq.com")  #修改
    print(infos)
    get_in=get_info(s)     #查询
    print(get_in)
    assert infos['data']['mail']=='99999999@qq.com'
    assert get_in['data'][0]['mail']=='99999999@qq.com'
