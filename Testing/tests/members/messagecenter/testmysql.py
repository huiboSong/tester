__author__ = 'co-mall'

import MySQLdb

def mysql_test():
    try:
        conn=MySQLdb.connect(host='10.90.26.122',user='root',passwd='comall2014',db='cybershop_test',port=3306)
        print "conn=",conn;
        cur=conn.cursor()
        print "cur=",cur;
        cur.execute('select * from cs_member')
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])

###############################################################################
if __name__=="__main__":
    mysql_test();
