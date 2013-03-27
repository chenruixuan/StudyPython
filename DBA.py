__author__ = 'ruixuan'
import MySQLdb
connection=MySQLdb.connect(user='root',passwd='123456',db='python',charset='utf8')
cursor=connection.cursor()
cursor.execute("select * from python")
for v in cursor.fetchall():
    print(v[1])