# coding=utf-8


import unittest
from core.databaseDriver import SqlDriver
from setting.wwjtest import database_setting
from setting.wwjtest.database_data import TestData as TD


class Test(unittest.TestCase):
    # 参数化数据获得
    d1 = TD().get("db_select")
    d2 = TD().get("db_insert")
    d3 = TD().get("db_delete")
    d4 = TD().get("db_update")

    def test_sql_select(self):
        """数据库查询支付方式操作"""
        mysql = SqlDriver(database_setting.host, database_setting.port, database_setting.user, database_setting.password, database_setting.database)
        params_name = self.d1.get('params_name')
        table_name = self.d1.get('table_name')
        where = self.d1.get('where')
        results = mysql.exec_mysql_query(params_name, table_name, where)
        count = results[0]
        data = results[1]
        for i in range(0, count-1):
            print "id=%s, name=%s" % (data[i][0], data[i][1])

    def sql_insert(self):
        """数据库增加支付方式操作"""
        mysql = SqlDriver(database_setting.host, database_setting.port, database_setting.user, database_setting.password, database_setting.database)
        table_name = self.d2.get('table_name')
        values = self.d2.get('values')
        results = mysql.exec_mysql_insert(table_name, values)
        print results

    def sql_delete(self):
        """数据库删除支付方式操作"""
        mysql = SqlDriver(database_setting.host, database_setting.port, database_setting.user, database_setting.password, database_setting.database)
        table_name = self.d3.get('table_name')
        where = self.d3.get('where')
        results = mysql.exec_mysql_delete(table_name, where)
        print results

    def sql_update(self):
        """数据库修改支付方式操作"""
        mysql = SqlDriver(database_setting.host, database_setting.port, database_setting.user, database_setting.password, database_setting.database)
        table_name = self.d4.get('table_name')
        update_values = self.d4.get('update_values')
        where = self.d4.get('where')
        results = mysql.exec_mysql_update(table_name, update_values, where)
        print results

# 下面是脚本单独调试所需代码
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    result = unittest.TextTestRunner(verbosity=2).run(suite)


