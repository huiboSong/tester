# coding=utf-8

from selenium import  webdriver
from time import sleep
import os
if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']
dr = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('from.html')
print file_path

dr.get(file_path)
dr.find_element_by_id('').click()

dr.find_element_by_name('').click()

print dr.find_element_by_tag_name('').get_attribute('class')

e = dr.find_element_by_class_name('')
dr.execute_script('$(argument[0]).fadeOut().fadeIn()',e)
sleep(2)

link = dr.find_element_by_link_text('register')
dr.execute_script('$(arguments[0]).fadeOut().fadeIn()',link)
sleep(2)

link = dr.find_element_by_partial_link_text('reg')
dr.execute_script('$(arguments[0]).fadeOut().fadeIn()',link)
sleep(2)

div = dr.find_element_by_css_selector('.controls')
dr.execute_script('$(arguments[0]).fadeOut().fadeIn()',div)
sleep(2)

dr.find_element_by_xpath('').click()
sleep(2)



url = 'http://www.baidu.com'
dr.get(url)
print "title of current page is %s" %(dr.title)
print "url of current page is %s" %(dr.current_url)
time.sleep(3)
dr.quit()