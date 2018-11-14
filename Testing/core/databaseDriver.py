# -*- coding: utf-8 -*-
from core.logger import Logger

__author__ = 'wwj'
__data__ = '2017-01-06'

import pymysql
import sqlite3

class SqlDriver(object):
    def __init__(self, host, port, user, password, databaseName):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = databaseName

    # 执行Mysql连接操作
    def exec_mysql_connection(self):
        try:
            conn = pymysql.connect(host=self.host,
                                   port=self.port,
                                   user=self.user,
                                   passwd=self.password,
                                   db=self.database,
                                   charset="utf8"
                                   )
            print (conn)
            if conn:
                Logger().info("Success: Mysql Connection Success")
                print("连接成功")
                return conn

        except Exception as e:
            Logger().error(str(e))
            print ("没有连接成功")

    # 执行Mysql查询
    def exec_mysql_query(self, params_name, table_name, where):
        conn = self.exec_mysql_connection()
        cur = conn.cursor()
        try:
            sql = 'select %s from %s where %s' % (params_name, table_name, where)
            effect_count = cur.execute(sql)
            data = cur.fetchall()
            Logger().info("Success: Mysql query Success")
            return effect_count, data
        except Exception as e:
            Logger().error(str(e))
            print("数据库查询失败原因:"+str(e))

    # 执行Mysql查询
    def exec_mysql_query1(self, params_name, table_name, inner, where):
        conn = self.exec_mysql_connection()
        cur = conn.cursor()
        try:
            sql = 'select %s from %s inner join %s where %s' % (params_name, table_name, inner, where)
            print (sql)
            effect_count = cur.execute(sql)
            data = cur.fetchall()
            Logger().info("Success: Mysql query Success")
            print (sql)
            print (effect_count, data)
            return effect_count, data
        except Exception as e:
            self.t.info("Error:" + str(e))
        # 关闭连接
        conn.close()

    # 执行Mysql增加
    def exec_mysql_insert(self, table_name, values):
        conn = self.exec_mysql_connection()
        cur = conn.cursor()
        try:
            sql = 'insert into %s values %s' % (table_name, values)
            effect_count = cur.execute(sql)
            conn.commit()
            Logger().info("Success: Mysql insert Success")
            return effect_count
        except Exception as e:
            Logger().error(str(e))
            print ("数据库新增失败原因："+str(e))
        # 关闭连接
        conn.close()

    # 执行Mysql删除
    def exec_mysql_delete(self, table_name, where):
        conn = self.exec_mysql_connection()
        cur = conn.cursor()
        try:
            sql = 'delete from %s where %s' % (table_name, where)
            effect_count = cur.execute(sql)
            conn.commit()
            Logger().info("Success: Mysql delete Success")
            return effect_count
        except Exception as e:
            Logger().error(str(e))
            print ("数据库删除失败原因："+str(e))
        # 关闭连接
        conn.close()

    # 执行Mysql修改
    def exec_mysql_update(self, table_name, update_values, where):
        conn = self.exec_mysql_connection()
        cur = conn.cursor()
        try:
            sql = 'update %s set %s where %s' % (table_name, update_values, where)
            effect_count = cur.execute(sql)
            conn.commit()
            Logger().info("Success: Mysql update Success")
            return effect_count
        except Exception as e:
            Logger().error(str(e))
            print ("数据库修改失败原因："+str(e))
        # 关闭连接
        conn.close()

class sqlite ():
    def readFronSqllite(self,name,null,sql):
        conn = sqlite3.connect()  # 该 API 打开一个到 SQLite 数据库文件 database 的链接，如果数据库成功打开，则返回一个连接对象
        cursor=conn.cursor()        # 该例程创建一个 cursor，将在 Python 数据库编程中用到。
        conn.row_factory=sqlite3.Row     # 可访问列信息
        cursor.execute()    # 该例程执行一个 SQL 语句
        rows=cursor.fetchall()      # 该例程获取查询结果集中所有（剩余）的行，返回一个列表。当没有可用的行时，则返回一个空的列表。
        return rows