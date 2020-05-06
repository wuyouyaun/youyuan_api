import requests
import hashlib
#
def loginQ(s,userName="KA600001"):
    url="http://seedtest.ap-ec.cn/auth-server/user/appKey.magpie"
    body={
           "userName":userName,
           "marketId":"10606"
         }
    r=s.post(url,json=body)
    print(r.json())
    return r
    # keys=r.json()["data"]["key"]
    # print(keys)
    # salt=r.json()["data"]["salt"]
    # print(salt)

def login(s,userKey,salt):
    url2="http://seedtest.ap-ec.cn/SSO-SERVER/app/encryptToken"
    b="123456a"
    x=hashlib.md5(b.encode(encoding='UTF-8')).hexdigest()
    print(x)
    newpassword=x+salt
    newpassword=hashlib.md5(newpassword.encode(encoding='UTF-8')).hexdigest()
    print(newpassword)

    body={
        "userKey":userKey,
        "password":newpassword,
        "loginType": "json"
          }
    r=s.post(url2,json=body)
    # token=s.token()
    # print(token)
    headers=r.json()["data"]["tokenInfo"]["token"]
    h={
        "Content-Type": "application/json",
        "Authorization":"bearer %s"%headers
    }

    s.headers.update(h)
    print(headers)
    return r

def buyiness(s,quantity="100",pickUpUserName="吴"):
    url="http://seedtest.ap-ec.cn/wholesaler-app/business/reserve.magpie"
    body={
        "tenderId":"35688213693861888",
          "quantity":quantity,
          "pickUpUserName":pickUpUserName,
          "pickUpPhone":"18571519920",
          "clearingForm":"ONLINE"}
    r=s.post(url,json=body)
    #print(r.json())
    return r

if __name__=="__main__":
    s=requests.session()
    r=loginQ(s,userName="KA600001")
    salt=r.json()["data"]["salt"]
    keys=r.json()["data"]["key"]
    k=login(s,userKey=keys,salt=salt)
    #print(k.json())
    nm=buyiness(s,quantity="100",pickUpUserName="")
    #assert nm.json()["errorMsg"]== '请求成功'
    print(nm.json()["errorMsg"])
































