#coding=utf-8
__author__ = 'co-mall'
from selenium import webdriver
import os,time

browser = webdriver.Chrome()
browser.get("http://zmsy-web-main-dev.dev.co-mall/login")
Username=browser.find_element_by_xpath("/html/body/div[2]/form/div[2]/div/input").send_keys("root")
time.sleep(1)
Password=browser.find_element_by_xpath("//*[@id='txt_password']").send_keys("123456")
time.sleep(1)
browser.find_element_by_id("btn_login").click()
time.sleep(2)
browser.close()