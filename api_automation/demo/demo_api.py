


# def loginFun(username,pwd):
#     #print(username)
#     print(pwd)
#     return "token"

# a="hello_world_yoyo"
# b=a.split("_")
# print(b)
import re
import requests
s=requests.session()
url="http://49.235.92.12:6009/admin/login/"
r=s.get(url)
#print(r1.text)
csrf_token=re.findall(r"name='csrfmiddlewaretoken' value='(.+?)'",r.text)
print(csrf_token[0])
# print(s.cookies)
# print(dict(s.cookies))
url2="http://49.235.92.12:6009/admin/login/?next=/admin/"
body={
    "csrfmiddlewaretoken":csrf_token[0],
    "username":"admin",
    "password":"yoyo123456",
    "next":"/admin/"
    }

print("333")
r1=s.post(url2,data=body)
print(r1.text)
print(s.cookies)

assert "Site administration | Django site admin" in r1.text





















































