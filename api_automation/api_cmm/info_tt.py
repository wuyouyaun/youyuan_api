# coding:utf-8
#from api_cmm.login import loginFun

# a=loginFun("wyy","123456a")
# print(a)

# from demo import demo_api
# a=demo_api.loginFun("e","jjj")
# print(a)
#print(__name__)


def add(a=2,b=5):
    a=a
    b=b
    c=a+b
    return a
def sdk(m,k=0):
    m=m
    k=add()+1
    kd=k+m
    return (kd)

if __name__=="__main__":
    m=add(a=3,b=5)
    print(m)
    ll=sdk(m=3)
    print(ll)
