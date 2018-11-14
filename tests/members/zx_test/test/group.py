# coding=utf-8
import random

__author__ = 'zhangxue'

import unittest


class MyTestCase(unittest.TestCase):
    a_group = ['1', '2', '3', '4']
    b_group = []
    c_group = []
    d_group = []

    def test_grouping(self):

        name = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
        for num in range(0, 16):
            if not self.is_already_group(name[num]):
                remain_group = self.checkgroupLen()
                if str(len(remain_group)) > 0:
                    ran_group = random.choice(remain_group)
                    if ran_group == 'a':
                        self.a_group.append(name[num])
                    elif ran_group == 'b':
                        self.b_group.append(name[num])
                    elif ran_group == 'c':
                        self.c_group.append(name[num])
                    elif ran_group == 'd':
                        self.d_group.append(name[num])
                else:
                    print "组已经分满组了呦"
            else:
                print name[num] + "你已经分好组了呦"
        print "a_group" + str(self.a_group)
        print "b_group" + str(self.b_group)
        print "c_group" + str(self.c_group)
        print "d_group" + str(self.d_group)

    def is_already_group(self, name):
        if (name in self.a_group) or (name in self.b_group ) or (name in self.c_group ) or (name in self.d_group ):
            return True
        else:
            return False

    def checkgroupLen(self):
        group = 'abcd'
        if self.a_group.__len__() >= 4:
            group = group.replace('a', '')
        if self.b_group.__len__() >= 4:
            group = group.replace('b', '')
        if self.c_group.__len__() >= 4:
            group = group.replace('c', '')
        if self.d_group.__len__() >= 4:
            group = group.replace('d', '')
        return group


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
