# coding=utf-8
from ddt import ddt, unpack, data
import time
import xlrd
import comall
import config
from core import commonutils
from setting.zx_test import setting
from setting.zx_test import el
from setting.zx_test.data import TestData

__author__ = 'zhangxue'

import unittest


@ddt
class MyTestCase(unittest.TestCase):


    def setUp(self):
        pass
        # # 创建Comall对象
        # self.dr = comall.Comall(setting.driver_type)
        # # 最大化窗口
        # self.dr.max_window()
    def test_work(self):
        # 打开文件
        workbook = xlrd.open_workbook(r'..\testdata.xlsx')
        # 获取所有sheet
        print workbook.sheet_names()  # [u'sheet1', u'sheet2']

        # 根据sheet索引或者名称获取sheet内容
        sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始
        # sheet1_0 = workbook.sheet_by_name('sheet1')
        # sheet1 = workbook.sheet_names()[0]

        # sheet的名称，行数，列数
        print sheet1.name, sheet1.nrows, sheet1.ncols

        # # 获取整行和整列的值（数组）
        rows = sheet1.row_values(3)  # 获取第四行内容
        cols = sheet1.col_values(0)  # 获取第三列内容
        print int(rows[0])
        print cols
        #
        # 获取单元格内容
        print sheet1.cell(2, 0).value #第0列 第3行
        print sheet1.cell_value(11, 0)#第0列 第13行
        print sheet1.row(11)[0].value#第0列 第12行


        #
        # # 获取单元格内容的数据类型
        # print sheet2.cell(1,0).ctype

        # dr = self.dr
        # dr.open("http://www.w3school.com.cn/tiy/t.asp?f=jseg_confirm")
        # dr.switch_to_frame_by_xpath('//*[@id="result"]/iframe')
        # dr.click('xpath','/html/body/div/input')
        # time.sleep(10)



    # def tearDown(self):
    #     # 关闭dr
    #     self.dr.quit()
    #     pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
