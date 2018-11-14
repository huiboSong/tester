# coding=utf-8
__author__ = 'zhangxue'

import unittest


class MyTestCase(unittest.TestCase):

    def test_something(self):
        xx = {"111":None,"23456":{"33333":"0000","22222":9999,"list":["3333","4444","111"]}}
        yy = {"111":None,"23456":{"22222":9999,"33333":"0000","list":["111","3333","4444"]}}
        # xx = {"111":None,"23456":{"22222":9999,"33333":"0000","list":[3333,4444,111]}}
        # yy = {"111":None,"23456":{"22222":9999,"33333":"0000","list":[111,3333,4444]}}
        print  self.cmp_dict(xx,yy)


    def cmp_dict(self ,src_data,dst_data):
        assert type(src_data) == type(dst_data),"type: '{}' != '{}'".format(type(src_data), type(dst_data))
        if isinstance(src_data,dict):
            assert len(src_data) == len(dst_data),"dict len: '{}' != '{}'".format(len(src_data), len(dst_data))
            for key in src_data:
                assert dst_data.has_key(key)
                self.cmp_dict(src_data[key],dst_data[key])
        elif isinstance(src_data,list):
            assert len(src_data) == len(dst_data),"list len: '{}' != '{}'".format(len(src_data), len(dst_data))
            print zip(sorted(src_data))
            print sorted(dst_data)
            for src_list, dst_list in zip(sorted(src_data), sorted(dst_data)):
                self.cmp_dict(src_list, dst_list)
        else:
            assert src_data == dst_data,"value '{}' != '{}'".format(src_data, dst_data)

        return True
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
