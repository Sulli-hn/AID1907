# """
# 操作数据库基本流程
# """
# import pymysql
# # 连接数据库
# db = pymysql.connect(host = 'localhost',
#                     port = 3306,
#                     user = 'root',
#                     password = '123456',
#                     database = 'stu',
#                     charset = 'utf8')
# # 获取游标
# cur = db.cursor()
# # 执行sql语句
# sql = "insert into class values (12,'Suil',25,'w',96);"
# cur.execute(sql)
# # 提交到数据库
# db.commit()
# # 关闭游标
# cur.close()
# # 关闭数据库
# db.close()

# """
# 读操作演示
# """
# import pymysql
# # 连接数据库
# db = pymysql.connect(user = 'root',
#                      password = '123456',
#                      database = 'stu',
#                      charset = 'utf8')
# # 获取游标
# cur = db.cursor()
# # 获取数据
# sql = "select * from interest where hobby = 'draw';"
# cur.execute(sql)
# # 第一种方法,可以直接遍历游标
# # for i in cur:
# #     print(i)
# all_now = cur.fetchall()
# print(all_now)
#
# cur.close()
# db.close()

# """
# 写操作
# """
# import pymysql
# # 连接数据库
# db = pymysql.connect(user = 'root',
#                      passwd = '123456',
#                      database = 'stu',
#                      charset = 'utf8')
# # 获取游标
# cur = db.cursor()
# # 执行语句
# name = input("Name:")
# age = input("Age:")
# gender = input("Gender:")
# score = input("Score:")
# try:
#     #sql语句的值参量可以通过execute传入
#     sql = "insert into class (name,age,gender,score) values(%s,%s,%s,%s);"
#     cur.execute(sql,[name,age,gender,score])
#     db.commit()#同步数据库
#
#     #修改操作
#     sql = "update class set score = 92 where name = 'Sulli';"
#     cur.execute(sql)
#
#     #删除操作
#     sql = "delete from class where name = 'Suil';"
#     cur.execute(sql)
# except Exception as e:
#     print(e)
#     db.rollback()
# cur.close()
# db.close()

"""
二进制文件存储
"""
import pymysql
db = pymysql.connect(
    user = 'root',
    passwd = '123456',
    database = 'photo',
    charset = 'utf8'
)
cur = db.cursor()
# 执行语句把图片存入
with open('0.jpeg','rb')as f:
    data = f.read()
sql = "insert into images values (1,%s,%s);"
cur.execute(sql,[data,'备注'])
db.commit()

cur.close()
db.close()