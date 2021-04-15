import pymysql

db = pymysql.connect(
    host='192.168.20.188',
    port=3306,
    user='root',
    passwd='zdsoft',
    db='squirreldb',
    charset='utf8'
)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute()方法执行SQL查询
cursor.execute("CREATE INDEX idex_user_id_unit_id_type ON sq_user_third_party_notice (user_id,unit_id,type)")
data = cursor.fetchone()
# print("Database version : %s " % data)

db.close()