# coding:utf-8
import requests
s=requests.session()

url="http://open.ap88.com/auth-server/user/key.magpie"
h={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/76.0.3809.100 Safari/537.36"}
body={
    "userName":"zhaolei"
      }
print(s.cookies)
c=requests.cookies.RequestsCookieJar()
c.set("sensorsdata2015jssdkcross","%7B%22distinct_id%22%3A%22374259244421186%22%2C%22%24device_id%22%3" \
                                  "A%2216da978d4ed26b-0e6640f3260c43-396a4507-2073600-16da978d4ee9b5%22%2C%22p" \
                                  "rops%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_traffic_sourc" \
                                  "e_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_k" \
                                  "eyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2216da978d4ed26b-" \
                                  "0e6640f3260c43-396a4507-2073600-16da978d4ee9b5%22%7D")
c.set("accessKeyId","STS.NUVJkjXyMwj8dZWTkCST6xJ2L")
c.set("accessKeySecret","6G1ZsdJcz1gGts1sCx6KWr7W8PsQsHJ1hshdaNeaL2k1")
c.set("JSESSIONID","node011bl65dapncfx1l1o9k7pa44562021.node0")
c.set("securityToken","CAIS+gF1q6Ft5B2yfSjIr5bjAdHetaZswKjTZnzmsGsWX9sal4+Zrjz2IHhIeHZoBOkfv/g0mW9V5/sblqVoRoReREvCKM1565kPH6t6jXiH6aKP9rUhpMCPOwr6UmzWvqL7Z+H+U6muGJOEYEzFkSle2"
                      "KbzcS7YMXWuLZyOj+wMDL1VJH7aCwBLH9BLPABvhdYHPH/KT5aXPwXtn3DbATgD2GM+qwMmsf/gnJXDuiCz1gOqlrUnwK3qOYWhYsVWO5Nybsy4xuQedNCaiHIMtEAXrf4n0PcZpmqW44iHcFBV4gSbNe3P6cFoL"
                      "wJ/aaU8FrRNsP/mj/p8t/w1WBWbGoABDk7bjs1sePDHKBzXGJuPlMQSE4ObvztHoJZiKPvk1Ti5OqlrHic2SCX+IHYV/4jyMX8BJNdZJ8qzAVJ4qMTYMeWlxmdyv4it3YEYTDPtAviC5Y52eIqtMHDM9jIJxd6OLId"
                      "3oQaI/ASA2MjrYEOkPqB/X55Gid6zAE3JU6YYzNs=")
c.set("AuthorizationSSO","USER_INFO={}")
s.cookies.update(c)
print(s.cookies)

r=s.post(url,json=body,headers=h)
print(r.text)


print(type(r.json()["data"]["key"]))
salt=r.json()["data"]["salt"]

import hashlib
data = '123456a'
x=hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
print(x)
newpassword=x+salt
newpassword=hashlib.md5(newpassword.encode(encoding='UTF-8')).hexdigest()
print(newpassword)

url2="http://open.ap88.com:8900/SSO-SERVER/authentication/form2"

body={"userKey":r.json()["data"]["key"],
      "password":newpassword,
      "loginType":"json"
      }
r=s.post(url2,json=body)
print(r.text)

m=r.json()["data"]["tokenInfo"]["token"]
print(m)

url2="http://open.ap88.com/BASE-DYNAMICFORM/mgtdf/addTempAttrFromTempAttr.magpie"
h={"Authorization":"bearer %s"%m

   }
print(s.headers)
s.headers.update(h)
print(s.headers)
body={"sourceTempAttrId":"34781703353487424",
      "targetTempId":"34710382496481344",
      "sourceTempId":"34691601736224832"
    }
r=s.post(url2,json=body)
print(r.text)

















































































# url="http://open.ap88.com:8900/SSO-SERVER/authentication/form2"
# c=requests.cookies.RequestsCookieJar()
# c.set("sensorsdata2015jssdkcross","%7B%22distinct_id%22%3A%22374259244421186%22%2C%22%24device_id%22%3" \
#                                   "A%2216da978d4ed26b-0e6640f3260c43-396a4507-2073600-16da978d4ee9b5%22%2C%22p" \
#                                   "rops%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_traffic_sourc" \
#                                   "e_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_k" \
#                                   "eyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2216da978d4ed26b-" \
#                                   "0e6640f3260c43-396a4507-2073600-16da978d4ee9b5%22%7D")
# c.set("accessKeyId","STS.NUVJkjXyMwj8dZWTkCST6xJ2L")
# c.set("accessKeySecret","6G1ZsdJcz1gGts1sCx6KWr7W8PsQsHJ1hshdaNeaL2k1")
# c.set("JSESSIONID","node011bl65dapncfx1l1o9k7pa44562021.node0")
# c.set("securityToken","CAIS+gF1q6Ft5B2yfSjIr5bjAdHetaZswKjTZnzmsGsWX9sal4+Zrjz2IHhIeHZoBOkfv/g0mW9V5/sblqVoRoReREvCKM1565kPH6t6jXiH6aKP9rUhpMCPOwr6UmzWvqL7Z+H+U6muGJOEYEzFkSle2"
#                       "KbzcS7YMXWuLZyOj+wMDL1VJH7aCwBLH9BLPABvhdYHPH/KT5aXPwXtn3DbATgD2GM+qwMmsf/gnJXDuiCz1gOqlrUnwK3qOYWhYsVWO5Nybsy4xuQedNCaiHIMtEAXrf4n0PcZpmqW44iHcFBV4gSbNe3P6cFoL"
#                       "wJ/aaU8FrRNsP/mj/p8t/w1WBWbGoABDk7bjs1sePDHKBzXGJuPlMQSE4ObvztHoJZiKPvk1Ti5OqlrHic2SCX+IHYV/4jyMX8BJNdZJ8qzAVJ4qMTYMeWlxmdyv4it3YEYTDPtAviC5Y52eIqtMHDM9jIJxd6OLId"
#                       "3oQaI/ASA2MjrYEOkPqB/X55Gid6zAE3JU6YYzNs=")
# c.set("AuthorizationSSO","USER_INFO={}")
# s.cookies.update(c)
# print(s.cookies)
# body={"userKey":"zhaolei",
#       "password":"123456a",
#       "loginType":"json"
#       }
# r=s.post(url,json=body)
# print(r.text)
