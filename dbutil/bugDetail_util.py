from db import get_connection
from dbutil.upload_util import get_client_map, get_solve_state_map
from modal import buginfo


def get_bug_detail(bugId):
    conn = get_connection()
    cursor = conn.cursor()
    bug = buginfo()
    sql = "SELECT * FROM bugfk_bug " \
          "LEFT JOIN bugfk_bug_sort  on bugfk_bug.belong_bug_sort =bugfk_bug_sort.sort_id " \
          "LEFT JOIN bugfk_project on bugfk_bug.belong_project=bugfk_project.project_id " \
          "LEFT JOIN bugfk_market ON bugfk_bug.market=bugfk_market.id  " \
          "LEFT JOIN bugfk_user ON bugfk_bug.solve_person=bugfk_user.user_id  " \
          "WHERE bug_id=%s"
    cursor.execute(sql, (bugId))
    try:
        for c in cursor:

            bug.bug_id = c['bug_id']
            bug.client_type = c['client_type']
            bug.client_type_name =get_client_map().get(bug.client_type)

            bug.belong_project = c['belong_project']
            bug.belong_project_name = c['project_name']

            bug.belong_bug_sort = c['belong_bug_sort']
            bug.belong_bug_sort_name = c['sort_name']

            bug.bug_title = c['bug_title']
            bug.bug_content = c['bug_content']
            bug.solve_state = c['solve_state']
            bug.solve_state_name = get_solve_state_map().get(bug.solve_state)
            bug.solve_method = c['solve_method']
            bug.submit_person = c['submit_person']
            bug.solve_person = c['solve_person']
            bug.solve_person_name=c['user_name']
            bug.submit_time = c['submit_time']
            bug.solve_time = c['solve_time']
            bug.reject_reason = c['reject_reason']
            bug.version = c['version']
            bug.flag = c['flag']
            bug.market = c['market']
            bug.market_name = c['market_name']
    finally:
        conn.close()
    return bug


def updata_bug_detail(bug_id,client_type,market,belong_bug_sort,bug_title,bug_content,reject_reason,belong_project,solve_state,
                      solve_person):
    conn = get_connection()
    cursor = conn.cursor()
    sql="UPDATE bugfk_bug SET client_type=%s,market=%s,belong_bug_sort=%s,bug_title=%s,bug_content=%s,reject_reason=%s," \
        "belong_project=%s,solve_state=%s,solve_person=%s WHERE bug_id=%s"
    try:
        cursor.execute(sql, ((int)(client_type),int(market),int(belong_bug_sort),bug_title,bug_content,reject_reason,int(belong_project),int(solve_state),
                             (int)(solve_person),bug_id))
        conn.commit()
    finally:
        conn.close()