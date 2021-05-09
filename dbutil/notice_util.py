from db import get_connection
from modal import noticeInfo

def getNotice():
    conn = get_connection()
    cursor = conn.cursor()
    noticeList=[]

    sql = "SELECT * FROM bugfk_notice WHERE flag=0 "
    try:
        cursor.execute(sql)
        for c in cursor:
            notice = noticeInfo()
            notice.id=c['notice_id']
            notice.notice_content = c['notice_title']
            notice.notice_url = c['notice_url']
            noticeList.append(notice)
    finally:
        conn.close()
    return noticeList

def deleteNotice(notice_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE bugfk_notice SET flag=1 WHERE notice_id=%s"
    try:
        cursor.execute(sql, (notice_id))
        conn.commit()
    finally:
        conn.close()