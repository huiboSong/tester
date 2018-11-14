# coding=utf-8
import io
import json
import random
import re
import time
import base64
import hashlib

#from lxml import etree

from core import logger


__author__ = 'zhangxue'


class CommonUtils:
    logs = logger.Logger()

    def createphone(self):
        '''
        随机创建一个手机号码
        :return:
        '''
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                   "153", "155", "156", "157", "158", "159", "186", "187", "188"]

        txt = random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))
        self.logs.info(txt)
        return txt

    def create_password(self, n=6):
        '''
        随机创建一个密码。英文字母和数字随机混合（含有数字和英文）。
        :param n: 默认创建8位 英文6位，数字2位
        :return:
        '''
        txt = self.create_str_num(n) + self.create_num(2)
        self.logs.info(txt)
        return txt

    def create_email(self, n=11):
        '''
        随机创建一个邮箱，
        :param n:
        :return:
        '''
        list = ["163", "qq", "co-mall"]
        txt = self.create_str_num(n) + '@' + random.choice(list) + '.com'
        self.logs.info(txt)
        return txt

    def create_IDNum(self):
        '''
        随机生成新的18为身份证号码
        :return:
        '''
        ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
        LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')

        t = time.localtime()[0]
        x = '%02d%02d%02d%04d%02d%02d%03d' % (random.randint(10, 99),
                                              random.randint(1, 99),
                                              random.randint(1, 99),
                                              random.randint(t - 80, t - 18),
                                              random.randint(1, 12),
                                              random.randint(1, 28),
                                              random.randint(1, 999))
        y = 0
        for i in range(17):
            y += int(x[i]) * ARR[i]
        txt = '%s%s' % (x, LAST[y % 11])
        self.logs.info(txt)
        return txt

    def img_to_base64(self, path):
        '''
        把图片转换成base64位编码

        :param path:图片地址 例如：D:\apk\apppic-ch.png
        :return:
        '''
        imgF = open(path, 'rb')  # 二进制方式打开图文件
        ls_f = base64.b64encode(imgF.read())  # 读取文件内容，转换为base64编码
        self.logs.info(ls_f)

        imgF.close()

        return ls_f

    def base64_to_img(self, strs, path):
        '''
        把base64位编码转换成图片。
        :param strs:base64 编码
        :return:
        '''
        imgdata = base64.b64decode(strs)
        file = open(path, 'wb')
        file.write(imgdata)
        file.close()


    def create_num(self, n=8):
        '''
        随机创建一个数字集
        :param n:  默认创建8位
        :return:
        '''
        return "".join(random.choice("0123456789") for i in range(n))

    def create_str_num(self, n=8):
        '''
        随机创建一个字符串。英文字母和数字随机混合(可能只有英文或只含有数字)。
        :param n:默认创建8位
        :return:
        '''
        return "".join(
            random.choice("QAZWSXEDCRFVTGBYHNUJMIKOLPqazwsxedcrfvtgbyhnujmikolp1234567890") for i in range(n))

    def create_str(self, n=8):
        '''
        随机创建一个字符串。英文字母。
        :param n:默认创建8位
        :return:
        '''
        return "".join(
            random.choice("QAZWSXEDCRFVTGBYHNUJMIKOLPqazwsxedcrfvtgbyhnujmikolp") for i in range(n))

    def check_json_format(self, raw_msg):
        """
        用于判断一个字符串是否符合Json格式
        :param self:
        :return:
        """
        if isinstance(raw_msg, basestring):  # 首先判断变量是否为字符串
            try:
                json.loads(raw_msg, encoding='utf-8')
            except ValueError:
                return False
            return True
        else:
            return False

    def check_xml_format(self, raw_msg):
        '''
        用于判断一个字符串是否符合xml格式
        :param raw_msg:
        :return:
        '''
        try:
            etree.fromstring(raw_msg)
            return True
        except Exception as e:
            return False

    def pitchstr(self, sub, start, end):
        '''
        截取字符串在开始start和end的字符串之间的部分
        :param sub:
        :param start:要截取的字符串之前的字符
        :param end: 要截取的字符串之后的字符
        :return:要截取的字符
        '''
        return re.findall('.*' + start + '(.*)' + end + '.*', sub)

    def img_prefix(self):
        return  time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))

    def del_a_key(self, sub, keyname):
        '''
        删除字典中指定的key
        :param sub:
        :param keyname:
        :return:
        '''
        if str(type(sub)) == "<type 'str'>":
            msub = eval(sub)
            if str(type(msub)) == "<type 'dict'>":
                if msub.has_key(keyname):
                    msub.pop(keyname)
                    return msub
                else:
                    return "key fail"
            else:
                return "data type not <type 'dict'>"
        elif str(type(sub)) == "<type 'dict'>":
            if sub.has_key(keyname):
                sub.pop(keyname)
                return sub
            else:
                return "key fail"
        else:
             return "data type not <type 'dict'> or <type 'str'>"



    def list_comjson_difforder(self, coma, comb, orderby=None):
        '''
         list类型数据比较json字符串是否相等（内容相同,排序不同）
        :param coma:
        :param comb:
        :param orderby:
        :return:
        '''
        if str(type(coma)) == "<type 'str'>" and str(type(coma)) == "<type 'str'>":
            mcoma = eval(coma)
            mcomb = eval(comb)
            if type(mcoma) == type(mcomb):
                if str(type(mcoma)) == "<type 'list'>":
                    if orderby != None:
                        mcoma.sort(key=lambda x: x[orderby])
                        mcomb.sort(key=lambda x: x[orderby])
                        if mcoma == mcomb:
                            return True
                        else:
                            return False
                    else:
                        orderby = str(mcoma[0].keys()[0])
                        mcoma.sort(key=lambda x: x[orderby])
                        mcomb.sort(key=lambda x: x[orderby])
                        if mcoma == mcomb:
                            return True
                        else:
                            return False
                elif str(type(mcoma)) == "<type 'dict'>":
                    tcoma = json.loads(coma)
                    tcomb = json.loads(comb)
                    mcoma = sorted(tcoma.items(), key=lambda d: d[0])
                    mcomb = sorted(tcomb.items(), key=lambda d: d[0])
                    # 也可以用这种方式排序,one 替换成tcoma
                    # sorted(one,key = lambda e:e.__getitem__('id'))
                    if mcoma == mcomb:
                        return True
                    else:
                        return False

                else:
                    print (self.__class__.__name__ + "暂时只提供数据类型为list和dict的比较")
            else:
                print (self.__class__.__name__ + "数据【解析后】类型不同,无法比较")
                return False
        else:
            print (self.__class__.__name__ + "数据【传入】类型不是【str类型】,无法比较")

    def cmp_dict(self ,src_data,dst_data):
        assert type(src_data) == type(dst_data),"type: '{}' != '{}'".format(type(src_data), type(dst_data))
        if isinstance(src_data,dict):
            assert len(src_data) == len(dst_data),"dict len: '{}' != '{}'".format(len(src_data), len(dst_data))
            for key in src_data:
                assert dst_data.has_key(key)
                self.cmp_dict(src_data[key],dst_data[key])
        elif isinstance(src_data,list):
            assert len(src_data) == len(dst_data),"list len: '{}' != '{}'".format(len(src_data), len(dst_data))
            for src_list, dst_list in zip(sorted(src_data), sorted(dst_data)):
                self.cmp_dict(src_list, dst_list)
        else:
            assert src_data == dst_data,"value '{}' != '{}'".format(src_data, dst_data)
			
    def is_valid_date(self, strdate):
        '''''判断是否是一个有效的日期字符串'''
        try:
            if ":" in strdate:
                time.strptime(strdate, "%Y-%m-%d %H:%M:%S")
            else:
                time.strptime(strdate, "%Y-%m-%d")
            return True
        except:
            return False

    def compare_time(self, start_t, end_t):
        s_time = time.mktime(time.strptime(start_t, "%Y-%m-%d %H:%M:%S"))  # get the seconds for specify date
        e_time = time.mktime(time.strptime(end_t, "%Y-%m-%d %H:%M:%S"))
        # log_time = time.mktime(time.strptime(l_time, '%Y-%m-%d %H:%M:%S'))
        if (float(s_time) >= float(e_time)):
            return True
        return False

    def creat_float(self, n=2):
        '''
        从0-2--中创建一个随机浮点数。小数点后面为两位
        :return:返回一个浮点数
        '''

        num_long = random.uniform(0, 200)
        num = round(num_long, n)
        return num

    # 把json转成字符串,宝洁项目提交请求时,需要使用
    def dict_to_str(self, json_data):
        to_str = ""
        keys = json_data.keys()
        keys.sort()
        for key in keys:
            if isinstance(json_data.get(key), dict):
                to_str += "&" + key + "={" + self.dict_to_str(json_data.get(key)) + "}"
            elif isinstance(json_data.get(key), list):
                to_str += "&" + key + "=[" + self.list_to_str(json_data.get(key)) + "]"
            else:
                to_str += "&" + key + "=" + json_data.get(key)
        return to_str[1:]

    # 把list数组转成字符串,宝洁项目提交请求时,需要使用
    def list_to_str(self, list_data):
        to_str = ""
        list_data.sort()
        for value in list_data:
            if isinstance(value, dict):
                to_str += "{" + self.dict_to_str(value) + "},"
            else:
                to_str += "{" + str(value) + "},"
        return to_str[0:-1]

    # md5加密,传入字符串,返回加密后的32位密文
    def md5(self, str):
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()

    # 返回unix时间戳,秒级
    def now_unix_time(self):
        t = time.time()
        return t

    # 返回unix时间戳,豪秒级
    def now_unix_time_ms(self):
        t = time.time()
        return int(round(t * 1000))

    # 读取json文件,并转成json对象返回
    @staticmethod
    def get_json_file(file_path):
        f = open(file_path)
        j = json.load(f)
        f.close()
        return j
