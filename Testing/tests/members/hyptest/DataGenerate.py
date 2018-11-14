# coding=utf-8
from random import choice

'''数据生成'''
class DataGenerate:

    '''生成手机号码的方法'''
    def create_phonenum(self):

        '''定义一个数据,包含真实有效的手机号前三位'''
        first_list = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "153", "155", "156", "157", "158", "159", "186", "187", "188"]

        '''从first_num中随机选择一个'''
        first_num = choice(first_list)

        '''从0到9中随机选择8个数字,生成后8位数字'''
        second_list = "0123456789"
        second_num = []
        for i in range(8):
            second_num.append(choice(second_list))
        last_num = "".join(second_num)

        phone_number = first_num + last_num
        return phone_number

    def create_num(self, num):

        '''从1到9中选择一个随机数'''
        first_list = [1,2,3,4,5,6,7,8,9]
        first_num = choice(first_list)

        '''从0到9中随机选择数字'''
        second_list = "0123456789"
        second_num = []

        if num >= 2:
            for i in range(num-1):
                second_num.append(choice(second_list))
                random_num_one = str(first_num) + "".join(second_num)
                '''输出一个拼接的数字串'''
            return random_num_one
        elif num == 1:
             for i in range(num):
                 second_num.append(choice(second_list))
                 random_num_two = int("".join(second_num))
                 '''输出一个数字'''
             return random_num_two
        else:
            '''输入一个小于1的非正整数提示'''
            return u"请输入一个大于0的正整数"




