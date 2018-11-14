# coding=utf-8


import math
import random
import sys
reload(sys)


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


sys.setdefaultencoding('gbk')
files = "players.txt"
count = 1
while count > 0:
    select = input(unicode('请选择王牌对王牌比赛要进行的流程:\n1.报名 2.抽签 3.统计淘汰人员 4.统计比赛总轮次\n', 'utf-8').encode('gb2312'))
    mtd = Methods()
    if select == 1:
        print u"进入报名环节："
        flag = mtd.sign_up(files)
        count = 1
        while count > 0:
            if flag == "true":
                choice = input(unicode('请选择是否继续报名：1.继续 2.退出\n', 'utf-8').encode('gb2312'))
                if choice == 1:
                    flag = mtd.sign_up(files)
                else:
                    print u"您已退出报名环节！"
                    break
    elif select == 2:
        print u"进入抽签环节："
        flag = mtd.draw_lots(files)
        count = 1
        while count > 0:
            if flag == "true":
                choice = input(unicode('请选择是否继续抽签：1.继续 2.退出\n', 'utf-8').encode('gb2312'))
                if choice == 1:
                    flag = mtd.draw_lots(files)
                else:
                    print u"您已退出抽签环节！"
                    break
    elif select == 3:
        print u"进入轮次比赛结果公布环节："
        flag = mtd.statistical_loser(files)
        count = 1
        while count > 0:
            if flag == "true":
                choice = input(unicode('请选择是否继续统计淘汰人员：1.继续 2.退出\n', 'utf-8').encode('gb2312'))
                if choice == 1:
                    flag = mtd.statistical_loser(files)
                else:
                    print u"您已退出统计淘汰人员环节！"
                    break
    elif select == 4:
        print u"进入计算比赛总轮次环节："
        flag = mtd.calculation_round(files)
        count = 1
        while count > 0:
            if flag == "true":
                choice = input(unicode('请选择是否继续计算比赛总轮次：1.继续 2.退出\n', 'utf-8').encode('gb2312'))
                if choice == 1:
                    flag = mtd.calculation_round(files)
                else:
                    print u"您已退出计算比赛总轮次环节！"
                    break
    choice = input(unicode('是否要进行其他比赛环节：1.是 2.否\n', 'utf-8').encode('gb2312'))
    if choice == 1:
        count += 1
    else:
        print u"您已放弃其他比赛环节的选择！"
        break
