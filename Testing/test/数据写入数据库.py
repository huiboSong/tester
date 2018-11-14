import random
import sqlite3
    # 打开数据库连接
db = sqlite3.connect('mytest.db')
    # 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# try:
#         # 使用 execute()  方法执行 SQL 查询
#     cursor.execute("SELECT * from  students ")
#     # 使用 fetchall() 方法获取所有数据，获取结果是一个二维tuple
#     data = cursor.fetchall()
# except BaseException as e:
#     print(e)
#         # 发生错误时回滚
#     db.rollback()
    # 关闭数据库连接
# db.close()

name = input("请输入用户名：")
username = input('请输入密码：')
idi = ''.join(random.choice('1234567890')for i in range(6))
sql = ''' insert into students
             (name, username,id)
             values
             (:userid, :passwd,:idi)'''

try:
        # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sql,{"userid":name,"passwd":username,"idi":idi})
    # 使用 fetchall() 方法获取所有数据，获取结果是一个二维tuple
    db.commit()
except BaseException as e:
    print(e)
    db.rollback()


# print(data)



