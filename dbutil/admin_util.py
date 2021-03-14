from db import get_connection


def addNotice(notice_title, notice_url):
    conn = get_connection()
    cursor = conn.cursor()
    #'notice_title' in dir() 判断变量是否被定义
    if (notice_title is None or notice_url is None or notice_title == "undefined" or notice_url == "undefined"):
        return '1'
    sql = "INSERT INTO bugfk_notice (notice_title,notice_url) VALUES (%s,%s)"
    try:
        cursor.execute(sql, (notice_title, notice_url))
        conn.commit()
        state = '0'
    except Exception as e:
        state = '1'
    finally:
        conn.close()
    return state


def addUser(user_name, user_password, user_email, user_phone, user_type):
    # 'user_name' in dir() 判断变量是否被定义
    if (user_name is None or user_password is None or user_email is None or user_phone is None or user_type is None
            or 'user_name' == "undefined" or 'user_password' == "undefined"or 'user_email' == "undefined"or 'user_phone'== "undefined"
        or 'user_type' == "undefined"):
        return '1'
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO bugfk_user (user_name,user_password,user_email,user_phone,user_type) VALUES (%s,%s,%s,%s,%s)"
    try:
        cursor.execute(sql, (user_name, user_password,user_email,user_phone,user_type))
        conn.commit()
        state = '0'
    except Exception as e:
        state = '1'
    finally:
        conn.close()
    return state


def addProject(project_name, client_type):

    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO bugfk_project (project_name,project_client_type) VALUES (%s,%s)"
    try:
        cursor.execute(sql, (project_name, client_type))
        conn.commit()
    finally:
        conn.close()


def addSort(sort_name, sort_type):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO bugfk_bug_sort (sort_name,sort_type) VALUES (%s,%s)"
    try:
        cursor.execute(sql, (sort_name, sort_type))
        conn.commit()
    finally:
        conn.close()
    return None