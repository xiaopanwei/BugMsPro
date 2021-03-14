import time

from db import get_connection
from modal import client, market, project, bug_sort, deal_state, userinfo


# 获取客户端列表
def get_client_list():
    return [client(0, 'PC端'), client(1, 'Android端'), client(2, 'IOS端')]

def get_solve_state_list():
    return [deal_state(0,'未处理'),deal_state(1,'处理中'),deal_state(2,'已驳回'),deal_state(3,'处理完成'),deal_state(4,'暂时搁置')]
# 获取客户端列表map
def get_client_map():
    return{0:'PC端',1:'Android端',2:'IOS端'}

def get_solve_state_map():
    return {0: '未处理', 1: '处理中', 2: '已驳回', 3: '处理完成', 4: '暂时搁置'}

#获取市场列表
def get_market_list():
    conn = get_connection()
    cursor = conn.cursor()
    market_list = []
    sql = "SELECT * FROM bugfk_market WHERE flag=0"
    try:
        cursor.execute(sql, )
        for c in cursor:
            marketinfo = market()
            marketinfo.id = c['id']
            marketinfo.market_name = c['market_name']

            market_list.append(marketinfo)
    finally:
        conn.close()

    return market_list


#获取产品列表
def get_project_list(client_id):
    conn = get_connection()
    cursor = conn.cursor()
    project_list = []
    sql = "SELECT * FROM bugfk_project WHERE flag=0 and project_client_type=%s"
    try:
        cursor.execute(sql, client_id)
        for c in cursor:
            projectinfo = project()
            projectinfo.project_id = c['project_id']
            projectinfo.project_name = c['project_name']
            project_list.append(projectinfo)
    finally:
        conn.close()

    return project_list


#获取bug分类列表
def get_bug_sort_list(client_id):
    conn = get_connection()
    cursor = conn.cursor()
    bug_sort_list = []
    sql = "SELECT * FROM bugfk_bug_sort WHERE flag=0 and sort_type=%s"
    try:
        cursor.execute(sql, client_id)
        for c in cursor:
            bug_sortinfo = bug_sort()
            bug_sortinfo.sort_id = c['sort_id']
            bug_sortinfo.sort_name = c['sort_name']
            bug_sort_list.append(bug_sortinfo)
    finally:
        conn.close()
    return bug_sort_list


#上传
def upload(client_type,belong_project,belong_bug_sort,bug_title,bug_content,market,submit_person):
    submit_time = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO bugfk_bug (client_type,belong_project,belong_bug_sort,bug_title,bug_content,market," \
          "submit_person,submit_time,flag,solve_state) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    try:
        cursor.execute(sql, (client_type,belong_project,belong_bug_sort,bug_title,bug_content,market,submit_person,submit_time,0,0))
        conn.commit()
    finally:
        conn.close()


def get_solve_people_list():
    conn = get_connection()
    cursor = conn.cursor()
    user_list = []
    sql = "SELECT * FROM bugfk_user WHERE user_type= 0"
    try:
        cursor.execute(sql, )
        for c in cursor:
            user = userinfo()
            user.id = c['user_id']
            user.username = c['user_name']
            user_list.append(user)
    finally:
        conn.close()

    return user_list