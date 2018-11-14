def login(username, password):
    """
    用于用户名和密码的验证
    :param username:用户名
    :param paaword:密码
    :return:True,用户验证成功；False，用户验证失败
    """
    try:
        f = open("users", "r", encoding="utf-8")
        for line in f:
            line = line.strip()  # 清除换行符
            # 无参数时移除两侧空格，换行符
            # 有参数时移除两侧指定的字符
            line_list = line.split(":")
            if line_list[0] == username and line_list[1] == password:
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
    with open("users", "a", encoding="utf-8") as f:
        temp = "\n" + username + ":" + password
        f.write(temp)
        return True


def user_exist(username):
    """
    检测用户名是否存在
    :param username:要检测的用户名
    :return: True：用户名存在；False：用户名不存在
    """
    # 一行一行的去查找，如果用户名存在，return True：False
    try:
        with open("users", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                line_new = line.split(":")
                if line_new[0] == username:
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
                print("成功")
                break
            else:
                print("失败")
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