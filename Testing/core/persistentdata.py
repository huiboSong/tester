# coding=utf-8
import pickle
import pprint
import config


__author__ = 'zhangxue'


class PersistentData:
    datapath=config.base_dir+r"core\\data.pkl"
    def setData(self, key, value, isupdate=False):
        '''
        存储数据  键值对
        :param key:  key
        :param value:  存储的值
        :param isupdate:  如果有相同的key  是否更新原来的key值。默认不更新
        :return: 是否有相同的key值
        '''
        res = False
        data = {key: value}
        try:
            output_old = open(self.datapath, 'rb')
            data_o = pickle.load(output_old)
            res = data_o.has_key(key)
            if res:
                if isupdate:
                    data_o[key] = value
                    data.update(data_o)
                else:
                    data.update(data_o)
            else:
                data.update(data_o)
        except IOError:
            print (IOError)
        else:
            output_old.close()

        output = open(self.datapath, 'wb')
        pickle.dump(data, output)
        output.close()
        pprint.pprint(data)
        return res


    def getData(self, key):
        try:
            pkl_file = open(self.datapath, 'rb')
            data = pickle.load(pkl_file)

        except IOError:
            print ("Error 文件读取错误")
            value = 'Error'
        else:
            pprint.pprint(data)
            res = data.has_key(key)
            if res:
                value = data[key]
            else:
                value = 'Error'

            pkl_file.close()
        return value


if __name__ == "__main__":
    PersistentData().setData('name2', 'zhangxue2')
    str1 = PersistentData().getData('name10')
    print  (str1)
    PersistentData().setData('name2', 'zhangxue9', True)
    PersistentData().setData('name2', 'zhangxue10')
