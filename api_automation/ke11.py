#coding:utf-8
###   统计在一个队列中的数字，有多少个正数，多少个负数，如[1, 3, 5, 7, 0, -1, -9, -4, -5, 8]

# a=[1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
# b=str(a)
# m=0
# n=0
# for i in a:
#     #print(i)
#     if i>=0:
#         m=m+1
#         print(m)
#     elif i<0:
#         n=n+1
# print("正整数的个数为:%s"%m)
# print("正整数的个数为:%s"%n)
# # print(a[0])
# # print(type(b))
#
# # for i in a:
# #     print(i)
# #     if i>=0:
# #         print(len(a[i]))
# #
#
#
#        #  print len(i)
#        # #print(len(a))
#
#
#
#
#
# import hashlib     #MD5加密
# data = '123456a'
# x=hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
# print(x)
#
#
# def fun(a,b):
#     "返回的值"
#     a=111
#     b=222
#     r=a+b
#     return("ddd")
#
# print(fun(a=11,b=12))











#
#
#
# kk=[1, 3, 5, 7, 0, -1, -9, -4, -5, 8]                 #统计在一个队列中的数字，有多少个正数，多少个负数
# m=[]
# k=[]
# for i in kk:
#     if i>=0:
#         #print(i)
#         m.append(i)
#         print(list(m))
#         print(len(m))
#     elif i<0:
#         k.append(i)
#         print(len(k))
# print("队列中正整数个数为:%s"%len(m))
# print("队列中正整数个数为:%s"%len(k))




# #  已知一个字符串为“hello_world_yoyo”, 如何得到一个队列 ["hello","world","yoyo"]
# import re
# import json
# m="hello_world_yoyo"
# newm=re.findall(r"^(.+?)_w",m)
# newm=json.dumps(newm)
# # nems=(json.dumps(newm))
# print(newm)
# new1=re.findall(r'o_(.+?)_y',m)
# # print(type(new1))
# # print(new1)
# h=json.dumps(new1)
# print(h)
# #new1=new1.json()[2:7]
# #print(new1)
# new2=re.findall(r'd_(.*)',m)
# new2=json.dumps(new2)
#
# #new2=json.dumps(new2)
# print(type(new2))
#
# # new3=(m[12:])
# # j=str(new3)
# # print(type(j))
#
# nm=newm+h+new2
# print(nm)










import json

#  已知一个字符串为“hello_world_yoyo”, 如何得到一个队列 ["hello","world","yoyo"]

# l="hello_world_yoyo"
# n=l.split("_")
# print(n)
# print(type(n))
# # k=(json.dumps(n))
# print(k)
# print(type(k))
# print(json.loads(k))









# 如果有一个列表a=[1,3,5,7,11]
# 问题：1如何让它反转成[11,7,5,3,1]
# 2.取到奇数位值的数字，如[1,5,11]

# a=[1,3,5,7,11]
# b=a[::-1]
# print(b)
#
# c=a[::2]
# print(c)


# for i in range(1,10,2):
#     print(i)







# a = "hello_world_yoyo"
# b = a.split("_")
# print(b)
# print(json.dumps(b))





# python作业5-如何判断一个数组是对称数组：
# 要求：判断数组元素是否对称。例如[1，2，0，2，1]，[1，2，3，3，2，1]这样的都是对称数组
# 用Python代码判断，是对称数组打印True，不是打印False,如：
#x = [1, "a",  0, "2", 0, "a", 1]


# 有一个数据list of dict如下
a = [
    {"yoyo1": "123456"},
    {"yoyo2": "123456"},
    {"yoyo3": "123456"},
]
# 写入到本地一个txt文件，内容格式如下：
# yoyo1,123456
# yoyo2,123456
# yoyo3,123456
import os
filename="E:\ces.text"
with open (filename,"w") as f:
    for b in a:
        for name,value in b.items():
            #f.write("name,value\n".format("name","value","\n"))
            f.write("name"+","+"value"+"\n")
            f.write(name+","+value+"\n")
            print("1111")
with open(filename,"r") as f:
    print(f.read())

