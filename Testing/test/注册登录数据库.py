import sqlite3
import random
# 打开数据库连接
db = sqlite3.connect('mytest.db')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
db.row_factory = sqlite3.Row  # 可访问列信息
cursor.execute('select username,password from students')
# 该例程执行一个 SQL 语句

def login(username, password):
    """
    用于用户名和密码的验证
    :param username:用户名
    :param paaword:密码
    :return:True,用户验证成功；False，用户验证失败
    """
    try:
        rows = cursor.fetchall()
        db.close()
        for line in rows:
            # line = line.strip()  # 清除换行符
            # # 无参数时移除两侧空格，换行符
            # # 有参数时移除两侧指定的字符
            # line_list = line.split(":")
            if line[0] == username and line[1] == password:
                # print("成功")
                return True
        return False
    except IOError:
        return False


def register(username, password):
    """
    注册用户
    1、打开文件
    2、用户名$密码
    :param username:用户名
    :param password:密码
    :return:True：注册成功；
    """
    id = ''.join(random.choice('1234567890') for i in range(6))
    sql = ''' insert into students
                 (username, password,id)
                 values
                 (:userid, :passwd)'''
    try:
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute(sql,{"userid": username, "passwd": password,"id":id})
        # 使用 fetchall() 方法获取所有数据，获取结果是一个二维tuple
        db.commit()
    except BaseException as e:
        print(e)
        db.rollback()
        db.close()
        return True


def user_exist(username):
    """
    检测用户名是否存在
    :param username:要检测的用户名
    :return: True：用户名存在；False：用户名不存在
    """
    # 一行一行的去查找，如果用户名存在，return True：False
    try:
        row = cursor.fetchall()
        db.close()
        for line in row:
            # line = line.strip()
            # line_new = line.split(":")
            if line[0] == username:
                return True
            return False
    except IOError:
        return False

def main():
    while True:
        print("欢迎登录xxx系统")
        arg = input("1:登录，2：注册")

        if arg == "1":
            uer = input("请输入用户名:")
            pwd = input("请输入密码:")
            if login(uer, pwd):
                print("登录成功")
                break
            else:
                print("登录失败")
        elif arg == "2":
            user = input("请输入用户名:")
            pwd = input("请输入密码:")
            is_exist = user_exist(user)
            if is_exist:
                print("用户名已经存在，注册失败")
            else:
                if register(user, pwd):
                    print("注册成功")
                    continue
                else:
                    print("注册失败")
        else:
            print("输入错误，请重新输入")

main()