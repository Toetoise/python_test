import pymysql


class DataBaseHandle(object):
    def __init__(self):
        self.db = pymysql.connect(
                host='192.168.20.188',
                port=3306,
                user='root',
                passwd='zdsoft',
                db='squirreldb',
                charset='utf8'
        )

    def insertDB(self, sql):
        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()
        try:
            # 使用execute()方法执行SQL查询
            self.cursor.execute(sql)
            # 想要数据生效，就要commit
            self.db.commit()
        except Exception as e:
            print('insert data error:', e)
            # 发生错误，需要进行回滚，刚才执行的插入语句就不会生效
            self.db.rollback()
        finally:
            self.cursor.close()

    def deleteDB(self, sql):
        self.cursor = self.db.cursor()
        try:
            # 使用execute()方法执行SQL查询
            self.cursor.execute(sql)
            # 想要数据生效，就要commit
            self.db.commit()
        except Exception as e:
            print('delete data error:', e)
            # 发生错误，需要进行回滚，刚才执行的插入语句就不会生效
            self.db.rollback()
        finally:
            self.cursor.close()

    def updateDB(self, sql):
        self.cursor = self.db.cursor()
        try:
            # 使用execute()方法执行SQL查询
            self.cursor.execute(sql)
            # 想要数据生效，就要commit
            self.db.commit()
        except Exception as e:
            print('update data error:', e)
            # 发生错误，需要进行回滚，刚才执行的插入语句就不会生效
            self.db.rollback()
        finally:
            self.cursor.close()

    def selectDB(self, sql):
        self.cursor = self.db.cursor()
        try:
            # 使用execute()方法执行SQL查询
            self.cursor.execute(sql)
            # 想要数据生效，就要commit
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            print('select data error:', e)
        finally:
            self.cursor.close()

    def closeDB(self):
        self.db.close()


if __name__ == '__main__':
    db = DataBaseHandle()
    data = db.selectDB('select * from sys_options where id = "1"')
    print(data)