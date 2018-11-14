# coding=utf-8

__author__ = 'zhangxue'

from decimal import *


class DecimalTest(object):
    def add(self, one, two):
        '''
        二则运算加法
        :param one:加数
        :param two:被加数
        :return:结果
        '''
        result = Decimal(one) + Decimal(two)
        return result

    def sub(self, one, two):
        '''
        二则运算减法
        :param one:减数
        :param two:被减数
        :return:结果
        '''
        result = Decimal(one) - Decimal(two)
        return result

    def mul(self, one, two):
        '''
        二则运算乘法
        :param one:乘数
        :param two:被乘数
        :return:结果
        '''
        result = Decimal(one) * Decimal(two)
        return result

    def divide(self, one, two):
        '''
        二则运算除法
        :param one:除数
        :param two:被除数
        :return:结果
        '''
        result = Decimal(one) / Decimal(two)
        return result

    def setprec(self, num, prec):
        return Decimal(num).quantize(Decimal(prec), rounding=ROUND_HALF_UP)


if __name__ == '__main__':
    dec = DecimalTest()
    print (dec.add("10.8923654573", "15.94895676575", ))
    print (dec.sub("19.126456567657734", "20.8676574576484"))
    print (dec.mul("19.12657457634", "20.844567457684"))
    print (dec.divide("1", "3"))
    print (Decimal('7.3254').quantize(Decimal('.0001'), rounding=ROUND_HALF_UP))
    print (dec.setprec("7.0985953", "0.00001"))


