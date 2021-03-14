import fenci
from db import get_connection

# 获取搜索结果列表
from modal import buginfo

#获取搜索结果
def get_search_list(client_type, belong_project, belong_bug_sort, bug_title, market, page, limit):
    conn = get_connection()
    cursor = conn.cursor()
    print(bug_title)
    bug_title_list = fenci.get_search_list(bug_title)
    print(bug_title_list)
    sqllike = ""
    # 多条件模糊查询 使用正则表达式  替换like
    for bug_title_info in bug_title_list:
        sqllike = sqllike + bug_title_info + "|"

    buglist = []
    try:
        if client_type == '':
            sql = "SELECT *  FROM bugfk_bug WHERE solve_state=3 limit %s,%s"
            cursor.execute(sql, ([((int(page) - 1) * int(limit)), int(limit)]))
        elif bug_title == '':
            sql = "SELECT * FROM bugfk_bug WHERE client_type=%s and belong_project=%s and belong_bug_sort=%s and market=%s and solve_state=3 limit %s,%s"
            cursor.execute(sql, (
            client_type, belong_project, belong_bug_sort, market, ((int(page) - 1) * int(limit)), int(limit)))
        else:
            sql = "SELECT * FROM bugfk_bug WHERE client_type=%s and belong_project=%s and belong_bug_sort=%s and market=%s and solve_state=3 and bug_title regexp %s limit %s,%s"
            # sqllike末尾不能多  | 否则会出错
            cursor.execute(sql, (
            client_type, belong_project, belong_bug_sort, market, sqllike[:-1], ((int(page) - 1) * int(limit)),
            int(limit)))

        for c in cursor:
            bug = buginfo()
            bug.bug_id = c['bug_id']
            bug.client_type = c['client_type']
            bug.belong_project = c['belong_project']
            bug.belong_bug_sort = c['belong_bug_sort']
            bug.bug_title = c['bug_title']
            bug.bug_content = c['bug_content']
            bug.solve_state = c['solve_state']
            bug.solve_method = c['solve_method']
            bug.submit_person = c['submit_person']
            bug.solve_person = c['solve_person']
            bug.submit_time = c['submit_time']
            bug.solve_time = c['solve_time']
            bug.reject_reason = c['reject_reason']
            bug.version = c['version']
            bug.flag = c['flag']
            bug.market = c['market']

            buglist.append(bug)
    finally:
        conn.close()
    return buglist

#获取搜索的数量
def get_search_list_count(client_type, belong_project, belong_bug_sort, bug_title, market):
    conn = get_connection()
    cursor = conn.cursor()
    print(bug_title)
    bug_title_list = fenci.get_search_list(bug_title)
    print(bug_title_list)
    sqllike = ""
    # 多条件模糊查询 使用正则表达式  替换like
    for bug_title_info in bug_title_list:
        sqllike = sqllike + bug_title_info + "|"

    count = 0
    try:
        if client_type == '':
            sql = "SELECT count(*)  FROM bugfk_bug WHERE solve_state=3"
            cursor.execute(sql, )
        elif bug_title == '':
            sql = "SELECT count(*) FROM bugfk_bug WHERE client_type=%s and belong_project=%s and belong_bug_sort=%s and market=%s and solve_state=3"
            cursor.execute(sql, ( client_type, belong_project, belong_bug_sort, market))
        else:
            sql = "SELECT count(*) FROM bugfk_bug WHERE client_type=%s and belong_project=%s and belong_bug_sort=%s and market=%s and solve_state=3 and bug_title regexp %s"
            # sqllike末尾不能多  | 否则会出错
            cursor.execute(sql, (client_type, belong_project, belong_bug_sort, market, sqllike[:-1]))

        for c in cursor:
            count = c['count(*)']
    finally:
            conn.close()
    return count
