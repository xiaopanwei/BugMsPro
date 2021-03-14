from db import get_connection

# 查看是否存在该用户
from modal import userinfo


def is_exist(name):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT count(*) FROM bugfk_user WHERE user_name=%s"
    try:
        cursor.execute(sql, (name))
        for c in cursor:
            count = c['count(*)']
    finally:
        conn.close()
    return count

def find_user_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()
    user=userinfo()
    sql = "SELECT * FROM bugfk_user WHERE user_name=%s"
    try:
        cursor.execute(sql, (name))
        for c in cursor:
            user.id=c['user_id']
            user.username=c['user_name']
            user.password = c['user_password']
            user.type=c['user_type']
            user.email=['user_email']
            user.phone=['user_phone']
    finally:
        conn.close()
    return user