import pymysql.cursors


def get_connection():
    connection = pymysql.connect(
        host='rm-bp1ns8gwl0a1ihnyzro.mysql.rds.aliyuncs.com', port=3306,
        user='xpw',
        password='xpw0524!',
        db='xpw_bugpro',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
    return connection
