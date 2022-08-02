# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 19:07:55 2022

@author: GUAN-YING
"""

class Banks():
    def __init__(self,username):
        self.__name=username   #變數私有化，只能透過方法才能提取變數的值
        self.__balance=0       #變數私有化
        self.title="聯成銀行"  
        self.__rate=30         #變數私有化
        self.__service_charge =0.01 #變數私有化
    def deposite(self,money):
        self.__balance +=money
        print("存款:",money,"完成")
    def withdraw_money(self,money):
        self.__blance -= money
        print("提款:",money,"完成")
    def get_balance(self):
        print(self.__name,"目前餘額",self.__balance)
    def usa_to_taiwan(self,usa_d):
        self.result =self.__call_rate(usa_d)
        return self.result
    def __call_rate(self,usa_d): #私有化方法，只能在這個方法中呼叫
        return int(usa_d*self.__rate*(1-self.__service_charge))
    def bankTitle(self):
        return self.title
    
class TC_Banks(Banks):
    def __init__(self,username):
        self.title="聯成銀行-站前分行"
dBank=Banks("David")
print("David的開戶銀行是:",dBank.title)

cBank=TC_Banks("Charry")
print("Charry的開戶銀行是:",cBank.title)

