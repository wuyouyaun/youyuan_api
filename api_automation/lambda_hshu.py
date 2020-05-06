#coding:utf-8
import requests
def func(a,b):  # 自定义函数
    return a*b
print(func(a=1,b=2))

f=lambda x,y: x*y   #匿名函数，实现一些简单的功能
print(f(2,5))



def fund(**kwargs):         # 类似有些接口参数会很长
    print("不定长参数:%s"%kwargs)
    h={                                             # 字典的形式传值
        "aaa":"sssss",
        "k1":"bbbb",
        "m1":"kkkk"

}

#print(fund(**h))
print(fund(aaa="ssss2",k1="bbbb2",m1="kkkk2"))
#return fund(aaa="sssss",k1="bbbb",m1="kkkk")
# # def printinfo(*bch,**kwargs):     #以字符串的形式
# #     print("传入的参数:%s"%str(bch))
# # #     m={"aaa":"bgbgbg",
# # #     "k1":"bbbb",
# # #     "m1":"kkkk"
# # # }
# # printinfo(1,5,8,aaa="bgbgbg",bbb="djjfd")
#
def printinfo(*bchs,**kwargs):
    print("返回的参数：%s"%str(bchs))
    print("返回的参数：%s"%kwargs)
    return "ddd"
a=[3,56,11]
printinfo(*a,k=2,b=3)



# def login(username,pwd):
#     print(username)
#     print(pwd)
#     return"token"



















































