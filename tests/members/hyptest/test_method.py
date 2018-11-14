import unittest

from logs.tests.members.hyptest.DataGenerate import *


class A(unittest.TestCase):
    c = DataGenerate()

    def test_one(self):
        a = self.c.create_phonenum()
        print a

        e = self.c.create_num(3)
        print e


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(A)
    result = unittest.TextTestRunner(verbosity=2).run(suite)