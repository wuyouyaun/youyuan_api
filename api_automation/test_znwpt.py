# coding:utf-8
import requests


def znw_Login(s,username,password):
    url="http://seedtest.ap-ec.cn/SSO-SERVER/authentication/form"
    h={
        "Cookie":"CNZZDATA1275799644=1876347011-1572233200-%7C1572576238; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22348772270026821%22%2C%22%24device_id%22%3A%2216e106c733e820-0a132d8e51fec-7220633d-352800-16e106c733f1ee%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22first_id%22%3A%2216e106c733e820-0a132d8e51fec-7220633d-352800-16e106c733f1ee%22%7D; acw_tc=784c10e815862269250653237eff520551bc09b2153e5e87bbb844ef2083af;"
                 " USER_INFO={%22userStatus%22:%221%22%2C%22systemCodes%22:[%22001%22%2C%22002%22%2C%22003%22%2C%22000%22%2C%22004%22%2C%22005%22%2C%22006%22%2C%22007%22%2C%22DAAPP%22%2C%22009%22%2C%22baasApply%22%2C%22008%22%2C%22010%22%2C%22011%22%2C%22012%22%2C%22bpm%22%2C%22020%22%2C%22021%22]%2C%22userPhone%22:%2213026681274%22%2C%22roleCodes%22:[]%2C%22marketIds%22:%22-1%22%2C%22userName%22:%22%E8%B5%B5%E9%9B%B7%22%2C%22userId%22:%2201311832681161250%22%2C%22tagList%22:[%22silk%22%2C%22apple%22%2C%22plates%22%2C%22grain%22%2C%22whiteSugar%22%2C%22KA%22%2C%221%22%2C%22x%22]%2C%22roleIdsStr%22:%220%22%2C%22roleIds%22:[%220%22]%2C%22deptNames%22:"
                 "%22%E7%A0%94%E5%8F%91%E4%B8%AD%E5%BF%83%22%2C%22dtFlag%22:%221%22%2C%22userAccount%22:%22zhaolei%22%2C%22deptIds%22:%2219340847%22%2C%22resetPwdFlag%22:%221%22%2C%22marketCodes%22:[%22DF%22%2C%2210303%22%2C%22000%22%2C%2210102%22%2C%2210505%22%2C%2290901%22%2C%2210606%22%2C%2210506%22%2C%2290201%22%2C%2210601%22%2C%2290202%22%2C%2211801%22]}; AppAuthorization=bearer%20eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50SWQiOiIzNTE2OTcyOTgzMTA0NzIzMiIsInVzZXJfbmFtZSI6IjE3NjIwMzU1MzA3Iiwic2NvcGUiOlsiYXBwIl0sImNvbXBhbnkiOiJhcGVjIiwidXNlclR5cGUiOiJjbGllbnQiLCJleHAiOjE1ODgzMTQ0NTgsInVzZXJJZCI6IjEwMDAwMDU1NDMiLCJhdXRob3JpdGllcyI6WyIzNDg1MjU0NTUx"
                 "MTU1NTEzNiIsIjM1MTY5NzgzNDMyNjc1MzkyIl0sImp0aSI6IjJhNjk4NjEyLTQwNGYtNGE2Yi05NjJmLWQ3OWMwMjc1ZTM2MSIsImNsaWVudF9pZCI6ImFwcCJ9.FfMlGFp0uGDiqHxiAX8-mtrmsYdJiN_fK78T3exA7dA; AppUserInfo={%22userId%22:%221000005543%22%2C%22userType%22:%22mchtType02%22%2C%22userName%22:%22%E4%BD%95%E4%BA%BF%E7%8F%8D%22%2C%22marketCodes%22:[%2210606%22]%2C%22marketId%22:%2210606%22%2C%22mobile%22:%2217620355307%22%2C%22account%22:%22KA600010%22%2C%22customerId%22:%2235169747598155840%22%2C%22isOauth%22:%221%22};"
                 " JSESSIONID=node01804huszu020g1y11o9lqwukho396.node0"
    }
    body={  "username":username,
            "password":password,
            "imageCode":"g74n",
            "deviceid":"278d7e1c-7a77-499b-a756-3de8c3c89633",
            "loginType":"json",
            "days":7,
            "aesKey":"",
            "aesIv":""
            }
    #s=requests.session()
    r2=s.post(url,json=body,headers=h,verify=False)
    newToken = r2.json()["data"]["tokenInfo"]["token"]
    print(newToken)
    h={"Authorization":"bearer %s"%newToken
        }
    s.headers.update(h)
    return(r2)
    # print(type(r2.json()))
    # print(r2.json()["data"]["tokenInfo"]["refreshToken"])
    #
    #newToken = r2.json()["data"]["tokenInfo"]["token"]
    # print(newToken)

def test_add01(s,id=35169729831047232,userId=1000005543,phone=17620355306):
    url2="http://seedtest.ap-ec.cn/ACCOUNT-SERVICE/userAccount/editUserAccount.magpie"
    h={
        "User-Agent":"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) QQ/9.2.2.26571"
                     " Chrome/43.0.2357.134 Safari/537.36 QBCore/3.43.1284.400 QQBrowser/9.0.2524.400",

    }

    s.headers.update(h)
    print(h)
    body2={"id":id,
          "userId":userId,
          "accountAlias":"",
          "roleIds":"35169783432675392",
          "phone":phone,
          "remark":"app register",
          "accountType":"ADMIN",
          "userLevel":"1"
          }
    r2=s.post(url2,json=body2)
    #print(r2.text)
    #print(str(r2.text))
    b=str(r2.text)
    #print(b)
    import re

    data=re.findall(r"er(.+?)de",r2.text)
    #print(data)
    return data

if __name__=="__main__":
    s=requests.session()
    b=znw_Login(s,username="zhaolei",password="123456a")
    print(b)
    m=test_add01(s)
    print(22222)
    print(m)
