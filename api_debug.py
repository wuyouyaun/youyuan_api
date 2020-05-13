#coding:utf-8
import requests
from commodity.login import  login_znw
from urllib.parse import quote
#

# s=requests.session()
def add_personal(s,userId=1000005635):
    url="http://seedtest.ap-ec.cn/ACCOUNT-SERVICE/userAccount/editUserAccount.magpie"
    body={"id":"35444617658576960",
         "userId":userId,
         "accountAlias":"交易员",
         "roleIds":"29102930349031488",
         "phone":"",
         "remark":"新增组织时同步管理员账号",
         "accountType":"ADMIN",
         "userLevel":"1"
          }
    r=s.post(url,json=body,verify=False)
    #print(r.json())
    return r

# def add_acconut(s,accountAlias="测试"):
#     url="http://seedtest.ap-ec.cn/ACCOUNT-SERVICE/userAccount/addUserAccount.magpie"
#     body={"id":"",
#          "userId":"1000005635",
#          "accountAlias":accountAlias,
#          "roleIds":"29103862963798080",
#          "phone":"",
#          "remark":"",
#          "password":"123456a",
#          "accountType":"TRADER",
#          "userLevel":"2"
#          }
#     #s=requests.session()
#     add_account1=s.post(url,json=body,verify=False)
#    # print(add_account1.json())
#     return add_account1

if __name__=="__main__":
    s=requests.session()
    login_znw(s)
    add_person=add_personal(s,userId=1000005635)
    print(add_person.json())
    # add_account1=add_acconut(s,accountAlias="测试1")
    # print(add_account1.json())





















# b="\u4ea4\u6613\u5458"
# print(quote(b))
