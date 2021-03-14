from db import get_connection
from dbutil.upload_util import get_solve_state_map
from modal import buginfo


def getmybuglist(userid,page, pageSize):
    conn = get_connection()
    cursor = conn.cursor()
    limit = (int(page) - 1) * pageSize
    buglist = []
    sql = "SELECT * FROM bugfk_bug " \
          "LEFT JOIN bugfk_project on bugfk_bug.belong_project=bugfk_project.project_id "\
          "WHERE submit_person=%s  limit %s,%s"
    try:
        cursor.execute(sql, (userid,limit,pageSize))
        for c in cursor:
            bug = buginfo()
            bug.bug_id = c['bug_id']
            bug.client_type = c['client_type']

            bug.belong_project = c['belong_project']
            bug.belong_project_name = c['project_name']

            bug.belong_bug_sort = c['belong_bug_sort']

            bug.bug_title = c['bug_title']
            bug.bug_content = c['bug_content']

            bug.solve_state = c['solve_state']
            bug.solve_state_name = get_solve_state_map().get(bug.solve_state)

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


def getmybuglist_count(userid):
    conn = get_connection()
    cursor = conn.cursor()
    count=0
    sql = "SELECT count(*) FROM bugfk_bug " \
          "LEFT JOIN bugfk_project on bugfk_bug.belong_project=bugfk_project.project_id "\
          "WHERE submit_person=%s"
    try:
        cursor.execute(sql, (userid))
        for c in cursor:
            count=c['count(*)']
    finally:
        conn.close()
    return count
