import requests




class Restaurant(object):

    def __init__(self,restaurant_name,cuisine_type):
        self.open_restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        # print("123")

    def describe_restaurant(self):
       # k=self.cuisine_type("dd","ds")
        print(" is now sitting")
        #return k

    def open_restaurant(self):
        print("餐馆正在营业")
        self.describe_restaurant()

# m=Restaurant(2,3)
# print(m)



#
#
#
#
#
# class People(object):
#
#     def hands(self,a,b):
#         print("有两只手")
#         return a+b
#
#     def foots(self):
#         print("有两只脚")
#         self.hands(2,3)     #self是类本身的实例参数
#
# #print(People)
# # 实例化    第一步实例化
# xiaohua=People()
# print(xiaohua)
# print("222")
# print(xiaohua.hands(2,3))
# xiaohua.foots()






class Father():
    def chezi(self,age=13):
        print("继承车子")
        self.age=age

    def fangzi(self):
        print("继承房子")

class Mother():
    def gh(self):
        print("8989")

class Son(Father,Mother):
    def mm(self):
        print("233")

hanshu=Son()   #实例化
hanshu.chezi() #继承父类中的方法
a=hanshu.age=28
print(a)
#hanshu.chezi()="ces"
hanshu.mm()
hanshu.gh()





















































