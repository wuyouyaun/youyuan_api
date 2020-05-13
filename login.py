#coding:utf-8

import requests
#
def login_znw(s,name="zhaolei",password="123456a"):
    url="http://seedtest.ap-ec.cn/SSO-SERVER/authentication/form"
    body={"username":name,
          "password":password,
          "imageCode":"mxny",
          "deviceid":"59f0b30b-9456-45f0-8d93-821f300ba883",
          "loginType":"json",
          "days":7,
          "aesKey":"",
          "aesIv":""
          }
    r=s.post(url,json=body,verify=False)
    token=r.json()['data']["tokenInfo"]["token"]
    # print(token)

    head={
            "Authorization":"bearer %s"%token
    }

    s.headers.update(head)
   # print(s.headers)

    return r

def add_personal(s,userId=1000005635,phone="18571519920"):
    url="http://seedtest.ap-ec.cn/ACCOUNT-SERVICE/userAccount/editUserAccount.magpie"
    body={"id":"35444617658576960",
         "userId":userId,
         "accountAlias":"交易员",
         "roleIds":"29102930349031488",
         "phone":phone,
         "remark":"新增组织时同步管理员账号",
         "accountType":"ADMIN",
         "userLevel":"1"
          }
    r=s.post(url,json=body,verify=False)
    #print(r.json())
    return r


def add_acconut(s,accountAlias="测试",phone="18571519920"):
    url="http://seedtest.ap-ec.cn/ACCOUNT-SERVICE/userAccount/addUserAccount.magpie"
    body={"id":"",
         "userId":"1000005635",
         "accountAlias":accountAlias,
         "roleIds":"29103862963798080",
         "phone":phone,
         "remark":"",
         "password":"123456a",
         "accountType":"TRADER",
         "userLevel":"2"
         }
    #s=requests.session()
    add_account1=s.post(url,json=body,verify=False)
   # print(add_account1.json())
    return add_account1



if __name__=="__main__":
    s=requests.session()
    logins=login_znw(s,name="zhaolei",password="123456a")
    print(logins.json())
    addtest=add_personal(s,userId=1000005635,phone="18571519920")
    print(addtest.text)
    add_account1=add_acconut(s,accountAlias="测试10")
    print(type(add_account1))
    print(add_account1.text)


























