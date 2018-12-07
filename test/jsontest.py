import csv
import json
import random

prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "153",
           "155", "156", "157", "158", "159", "186", "187", "188"]
a = random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))
# print(a)
c = "".join(random.choice("0123456789") for i in range(8))
test = {'1': '2'}
m = '测试文案保存'
print(type(test))
n = ("".join(random.choice("abcdefghijk0123456789") for i in range(10)))
print(n)
with open(r"test.xml", "a") as a:
    a.write('1,1,2,3,4,5,5,6')

with open('data.txt', 'a') as f:
    f.write('hello world1')

test = open('data.txt', )
print(test)
with open('data.txt', encoding='utf-8') as f:
    line = f.readline()
    while line:
        # print(line)
        line = f.readline()


def fileload():
    csvfile = open(test.csv, encoding='utf-8')
    data = csv.reader(csvfile)
    dataset = []
    for line in data:
        dataset.append(line)
    csvfile.close()
    return dataset


# 随机的选取一个字符
# print (random.choice('abcde./;[fgja13ds2d'))

# 随机的选取n个字符
# print (random.sample('abcdefghijk0123456789',5))

# 返回指定范围的一个随机整数，包含上下限
# print(random.randint(5, 10))

dict = {'name': 'bobo', 'sex': '男', 'age': 21}
# 序列化
dic_str = json.dumps(dict)
print(type(dic_str), type(dict))
# 反序列化
obj = json.loads(dic_str)
print(type(obj))

dic = {'age': 23, 'job': 'student', '文案': '测试很长的文案，我需要保存'}
# 序列化
with open('abc.json', 'w', encoding='utf-8') as f:
    json.dump(dic, f)
    print(f)
# 反序列化
with open('abc.json', encoding='utf-8') as e:
    obj = json.load(e)
    print(e)

f = lambda x: x ** 2
print(f(5))  # 25
i = 0
while i < 12:
    i = + 1
    if i % 2 > 0:
        break
    print(i)
