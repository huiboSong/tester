__author__ = 'songhuibo'
import time

from setting.test_test import setting

A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
print(A0)
A1 = range(10)
print(A1)

# 备注测试提交111

timestamp = int(time.strftime('%S%H%M', time.localtime())) * 7 - 1995
print(timestamp)
if timestamp > 0:
    # 更新params[dict格式]的值方便其他请求调用
    setting.params.update(
        {'timestamp': int(time.strftime('%S%H%M', time.localtime())) * 7 - 1995}
    )
else:
    print("Error, HTTP params[dict] key[timestamp] value is not updated.")
print(setting.params)

print((time.time()))
print(time.localtime(1544063641.8100593))
print((time.strftime('%S%H%M', time.localtime())))
print('测试')
# import datetime
# i = datetime.datetime.now()
# print ("当前的日期和时间是 %s" % i)
# print ("ISO格式的日期和时间是 %s" % i.isoformat() )
# print ("当前的年份是 %s" %i.year)
# print ("当前的月份是 %s" %i.month)
# print ("当前的日期是  %s" %i.day)
# print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
# print ("当前小时是 %s" %i.hour)
# print ("当前分钟是 %s" %i.minute)
# print ("当前秒是  %s" %i.second)
list = {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}
for a in list:
    if int(a) % 3 == 0:
        print('测试', a)
        if int(a) % 5 == 0:
            print('ceshi2', a)
    elif int(a) % 2 == 0:
        print('测试1', a)
        if int(a) % 5 == 0:
            print('ceshi2', a)
    elif int(a) % 5 == 0:
        print('ceshi2', a)
    else:
        print(a)
print(20 + 5)
print(20 - 5)
print(20 * 5)
print(20 / 5)
print(20 % 5 == 0)
print(20 ** 5)
print(21 // 5)
count = 0
while count < 21:
    count += 1
    if count % 3 == 0:
        print('整除3', count)
        if count % 5 == 0:
            print('整除5', count)
    elif count % 2 == 0:
        print('整除2', count)
        if count % 5 == 0:
            print('整除5', count)
    elif count % 5 == 0:
        print('整除5', count)
    else:
        print(count)
for letter in 'Python':
    if letter == 'h':
        break
    print('当前字母 :', letter)

i = 1
while i > 0:
    i = i - 1
    if i == 0 or i == 5:
        continue
    print(i)
print("Good bye!")
