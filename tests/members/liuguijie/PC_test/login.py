# coding:utf-8
__author__ = 'halloween'
from selenium import webdriver
import time
dr = webdriver.Chrome()
dr.get("http://www.365autogo.com/")  # 进入福田前台
time.sleep(2)
dr.maximize_window()             # 窗口最大化
# time.sleep(1)
dr.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[2]/div[3]/div/a[1]").click()   # 点击“请登录”
time.sleep(1)
dr.find_element_by_xpath('//*[@id="username"]').click()              # 点击“用户名输入框”
dr.find_element_by_xpath('//*[@id="username"]').send_keys('13381253931')     # 输入用户名
time.sleep(1)
dr.find_element_by_xpath('//*[@id="password"]').click()                # 点击“密码输入框”
dr.find_element_by_xpath('//*[@id="password"]').send_keys('liuguijie')         # 输入密码
time.sleep(1)
dr.find_element_by_xpath('//*[@id="fm1"]/section[3]/p/input[4]').click()      # 点击“登录”

s1 = dr.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/div[3]/div/span').text    # 获取“[退出]”
print s1

if s1 == u"您好，13381253931！":
    print u"登录成功"
else:
    print u"登录失败"
time.sleep(2)
dr.close()
