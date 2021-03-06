#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb
from subprocess import Popen,PIPE  

#         host='localhost',
#         port = 3306,
#         user='root',
#         passwd='123456',
#         db ='sanguogame',

# CREATE TABLE `sanguogame`.`new_table` (
#   `id` INT NOT NULL AUTO_INCREMENT,
#   `name` VARCHAR(45) NOT NULL,
#   `class` VARCHAR(45) NOT NULL,
#   `age` VARCHAR(45) NOT NULL,
#     PRIMARY KEY (`id`, `name`));


class mysqlTool():
    def __init__(self,addr = 'localhost',port = 3306,usname = 'root',uspw = '7668150Tt00',defDB = 'test'):
        self.mysqladdr = addr           #mysql地址
        self.mysqlport = port           #mysql端口
        self.mysqlusername = usname     #mysql登陆用户名
        self.mysqlpassword = uspw       #mysql登陆密码
        self.mysqlDefaleDB = defDB      #mysql默认登陆数据库
        self.connectManger = None       #mysql连接管理器
        self.mysqlcursor = None         #mysql消息收发器
        self._connectMysql()            #连接mysql数据库
    def __del__(self):
        self.closeCursor()
        self.closeConnect()
    def _connectMysql(self):
        self.connectManger = MySQLdb.connect(
                                             host = self.mysqladdr,
                                             port = self.mysqlport,
                                             user = self.mysqlusername,
                                             passwd = self.mysqlpassword,
                                             db = self.mysqlDefaleDB,
                                             charset="utf8"
                                             )
        self.mysqlcursor = self.connectManger.cursor()
    #调用mysql命令
    def execute(self,cmdstr):
        if self.mysqlcursor:
            return self.mysqlcursor.execute(cmdstr)
        else:
            return -999#mysql 未连接
    def inPutDataWithSqlFile(self,sqlfilepath):
        process = Popen('/usr/local/mysql/bin/mysql -h%s -P%s -u%s -p%s %s'  %(self.mysqladdr, self.mysqlport, self.mysqlusername, self.mysqlpassword, self.mysqlDefaleDB), stdout=PIPE, stdin=PIPE, shell=True)  
        output = process.communicate('source '+sqlfilepath)
        print output
    def getOneDat(self):
        return self.mysqlcursor.fetchone()
    def getAllDat(self):
        return self.mysqlcursor.fetchall()
    def getMangDat(self,n = 1):
        return self.mysqlcursor.fetchmany(n)
    def closeCursor(self):
        self.mysqlcursor.close()
    def closeConnect(self):
        self.connectManger.close()
    
#在数据库中查找某行数据
#select * from test id not in('2','3');#id不含2,3或者去掉not表示含有
#查数据
# select * from test;  #取所有数据
# select * from test limit 0,2;  #取前两条数据 
# select * from test email like '%qq%' #查含有qq字符 _表示一个 %表示多个
# select * from test order by id asc;#降序desc
# select * from test id not in('2','3');#id不含2,3或者去掉not表示含有
# select * from test timer between 1 and 10;#数据在1,10之间
#  
# #---------------------------表连接知识------------------------------
# #等值连接又叫内链接 inner join 只返回两个表中连接字段相等的行
# select * from A inner join B on A.id = B.id; #写法1
# select * from A,B where A.id = B.id; #写法2
# select a.id,a.title from A a inner join B b on a.id=b.id and a.id=1;#写法3 表的临时名称
# select a.id as ID,a.title as 标题 from A inner join B on A.id=B.id;#添加as字句
#  
# #左连接又叫外连接 left join 返回左表中所有记录和右表中连接字段相等的记录
# select * from A left join B on A.id = B.id;
# select * from A left join (B,C,D) on (B.i1=A.i1 and C.i2=A.i2 and D.i3 = A.i3);#复杂连接
# #右连接又叫外连接 right join 返回右表中所有记录和左表中连接字段相等的记录
# select * from A right join B on A.id = B.id;
# #完整外部链接 full join 返回左右表中所有数据
# select * from A full join B on A.id = B.id;
# #交叉连接 没有where字句 返回卡迪尔积
# select * from A cross join B;
