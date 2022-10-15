# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 16:02:41 2022

@author: meena
"""

cnt=int(input("How many numbers?"))
numbers =[]
for index in range(cnt):
    numbers.append(int(input("enter the number")))  
def getEncryptedNumber(numbers):
    temp=[]     
    if len(numbers)<=1:
        return(numbers[0])
    while (len(numbers!=2)):
        for i in range(len(numbers)-1):
            j=numbers[i] +numbers[i+1]
            if j>9:
                j=j%10
            temp.append(j)
        numbers=temp
        temp=[]
    return (str(numbers[0])+ str(numbers[1]))
    print(str(numbers[0])+ str(numbers[1]))