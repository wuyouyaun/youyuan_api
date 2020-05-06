# coding:utf-8
import requests

a = [1, 3, 5, 7]
# c=sum(a)   # 内建函数
# print(c)
def qiuhe(a):
    # print("1111")
    s = 0
    for i in a:
        s = s + i
    # r=2222
    # b=1111
    # s=r+b
    print(s)
    return s


b=qiuhe(a)
#print(s)
print(qiuhe(a))
# # def ass():
# #     k=add()+88
# #     return k
# # #print(k)
#
#
# print(dir(__builtins__))
# #  print(dir(__build_class__))



def printme( str ):
   "打印任何传入的字符串"
   print (str)
   return

#调用printme函数
printme("eref")
































