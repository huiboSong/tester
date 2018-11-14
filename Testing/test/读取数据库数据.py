import sqlite3
conn = sqlite3.connect('mytest.db')
cursor=conn.cursor()
# 该例程创建一个 cursor，将在 Python 数据库编程中用到。
conn.row_factory = sqlite3.Row  # 可访问列信息
# 可访问列信息
cursor.execute('select name,passwd from students')
# 该例程执行一个 SQL 语句
rows=cursor.fetchall()
print(rows)
print(type(rows))

# 该例程获取查询结果集中所有（剩余）的行，返回一个列表。当没有可用的行时，则返回一个空的列表。
