from db import get_connection
from modal import imageInfo


def insertimage(bugid, image_url):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO bugfk_image (belong_id,image_url) VALUES (%s,%s)"
    try:
        cursor.execute(sql, (bugid, image_url))
        conn.commit()
    finally:
        conn.close()


def delbyimageid(image_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE bugfk_image SET flag=1 WHERE image_id=%s"
    try:
        cursor.execute(sql, (image_id))
        conn.commit()
    finally:
        conn.close()

    return None


def find_imagename_by_id(image_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "select image_url from bugfk_image WHERE image_id=%s "
    imageurl = ""
    try:
        cursor.execute(sql, image_id)
        if conn == "":
            return ""
        for i in cursor:
            imageurl = i["image_url"]
    finally:
        conn.close()
    return imageurl

def find_image_by_bugid(bug_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "select * from bugfk_image WHERE belong_id=%s and flag=0"
    imageurl = []
    try:
        cursor.execute(sql, bug_id)
        if conn == "":
            return ""
        for i in cursor:
            imageinfo=imageInfo()
            imageinfo.image_url=i["image_url"]
            imageinfo.image_id=i["image_id"]
            imageurl.append(imageinfo)

    finally:
        conn.close()
    return imageurl