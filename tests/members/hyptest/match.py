# coding=utf-8

# import unittest
# class match(unittest.TestCase):

   # def test_xxx(self):
f = open('out.txt','a')
name = raw_input("请输入参赛人员名称: ")
f.write(name)
f.close()
li =[]
f = open("out.txt", "rb")
li = f.read().split(",")
print li

# 下面是脚本单独调试所需代码
# if __name__ == "__main__":
#     suite = unittest.TestLoader().loadTestsFromTestCase(match)
#     result = unittest.TextTestRunner(verbosity=2).run(suite)