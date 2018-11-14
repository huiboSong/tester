# coding=utf-8

import math
import random


class Methods(object):

    """报名"""
    @staticmethod
    def sign_up(files):
        name = raw_input(unicode('请输入王牌对王牌比赛报名人员名单:\n', 'utf-8').encode('gb2312'))
        file_old = open(files)
        text = file_old.read().decode("gbk")
        file_old = open(files, 'a')
        if len(text) == 0:
            file_old.write(name.encode("gbk"))
        else:
            file_old.write((u'，'+name).encode("gbk"))
        file_old = open(files)
        try:
            text = file_old.read().decode("gbk")
            players = text.split(u'，')
            players = list(set(players))
            file1 = open(files, 'w')
            num = len(players)
            for i in players:
                if i == players[num-1]:
                    file1.write(i.encode("gbk"))
                else:
                    file1.write((i+u'，').encode("gbk"))
            print u"您已报名成功，请好好准备比赛！"
            return "true"
        finally:
            file_old.close()

    """计算比赛总轮次"""
    @staticmethod
    def calculation_round(files):
        file_old = open(files)
        try:
            text = file_old.read().decode("gbk")
            players = text.split(u'，')
            num = len(players)
            if num >= 4:
                b = 1
                for i in range(0, num):
                    if b < num <= b*2:
                        print u"比赛总共进行的轮次为 %s 轮" % int(math.log(b*2, 2))
                        break
                    else:
                        b *= 2
            else:
                print u"报名人数不够，比赛无法进行！"
            return "true"
        finally:
            file_old.close()

    """抽签"""
    @staticmethod
    def draw_lots(files):
        file_old = open(files)
        try:
            text = file_old.read().decode("gbk")
            players = text.split(u'，')
            total = len(players)
            print u"本轮对决对手匹配如下："
            num = total-1
            if (total % 2) == 0:
                for i in range(0, total/2):
                    playCouple = ""
                    for j in range(0, 2):
                        tag = random.randint(0, num)
                        num -= 1
                        if j == 1:
                            playCouple += players[tag]
                        else:
                            playCouple += players[tag] + u"，"
                        del players[tag]
                    print u"第%s组选手:%s" % (i+1, playCouple)
            else:
                tag = random.randint(0, num)
                print u"本轮轮空选手：%s" % (players[tag])
                del players[tag]
                num -= 1
                for i in range(0, (total-1)/2):
                    playCouple = ""
                    for j in range(0, 2):
                        tag = random.randint(0, num)
                        num -= 1
                        if j == 1:
                            playCouple += players[tag]
                        else:
                            playCouple += players[tag] + u"，"
                        del players[tag]
                    print u"第%s组选手:%s" % (i+1, playCouple)
            return "true"
        finally:
            file_old.close()

    """统计比赛淘汰人员"""
    @staticmethod
    def statistical_loser(files):
        name = raw_input(unicode('请输入上轮比赛中淘汰人员名单:\n', 'utf-8').encode('gb2312'))
        losers = name.split(u'，')
        file_old = open(files)
        try:
            text = file_old.read().decode("gbk")
            players = text.split(u'，')
            for i in losers:
                if i in players:
                    players.remove(i)
            num = len(players)
            file1 = open(files, 'w')
            for i in players:
                if i == players[num-1]:
                    file1.write(i.encode("gbk"))
                else:
                    file1.write((i+u'，').encode("gbk"))
            file1 = open(files)
            text = file1.read().decode("gbk")
            print u"本轮未淘汰人员：%s" %text
            return "true"
        finally:
            file_old.close()

