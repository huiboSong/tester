__author__ = 'Administrator'
import random
idi = ''.join(random.choice('1234567890')for i in range(6))
print(type(idi))
print(idi)

from selenium import webdriver
import math
def add(x, y):
   """相加"""

   return x + y

def subtract(x, y):
   """相减"""

   return x - y

def multiply(x, y):
   """相乘"""

   return x * y

def divide(x, y):
   """相除"""

   return x / y

# 用户输入
print("选择运算：")
print("+、相加")
print("-、相减")
print("×、相乘")
print("÷、相除")

choice = input("输入你的选择(+/-/×/÷):")
# try:
#    for num1 in (0, 9):
#       num1 = int(input("输入第一个数字: "))
#       if num1 >= 0:
#          break
# except ValueError:
#       print("请输入数字")

# for num2 in (0,9):
#    try:
#       num2 = int(input("输入第二个数字: "))
#    except ValueError:
#       print("请输入数字")
#    if num2 >= 0:
#       break
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))
if choice == '+':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '-':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '×':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '÷':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("非法输入")

