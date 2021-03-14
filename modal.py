class userinfo:
    def __init__(self):
        self.id = ""
        self.username = ""
        self.password = ""
        self.type = ""  # 0 管理员 1操作员
        self.email = ""
        self.phone = ""


# 通过添加与其他表id 对应的制的参数  类似 belong_project_name参数，来减少页面代码
class buginfo:
    def __init__(self):
        self.bug_id = ""
        self.client_type = ""  # 0.pc端 1.安卓端 2.ios端
        self.client_type_name = ""  # 0.pc端 1.安卓端 2.ios端

        self.belong_project = ""  # 所属产品(关联联产品表)
        self.belong_project_name = ""  # 所属产品(关联联产品表)

        self.belong_bug_sort = ""  # 所属BUG分类（关联bug分类表
        self.belong_bug_sort_name = ""  # 所属BUG分类（关联bug分类表

        self.bug_title = ""  # bug标题
        self.bug_content = ""  # bug详情

        self.solve_state = ""  # 0.未处理 1.处理中 2.已驳回 3.处理完成 4.暂时搁置
        self.solve_state_name = ""  # 0.未处理 1.处理中 2.已驳回 3.处理完成 4.暂时搁置

        self.solve_method = ""  # 处理办法

        self.submit_person = ""  # 反馈人id（关联用户表）
        self.submit_person_name = ""  # 反馈人id（关联用户表）

        self.solve_person = ""  # 处理人id（关联用户表）
        self.solve_person_name = ""  # 处理人id（关联用户表）

        self.submit_time = ""  # 反馈时间
        self.solve_time = ""  # 处理时间（更新状态时更新时间
        self.reject_reason = ""  # 驳回原因
        self.version = ""  # 程序版本号
        self.flag = 0

        self.market = ""  # 市场（关联市场表） 默认新加坡
        self.market_name = ""  # 市场（关联市场表） 默认新加坡


# 客户端
class client:
    def __init__(self, id, name):
        self.id = id
        self.name = name
# 处理状态
class deal_state:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# 产品
class project:
    def __init__(self):
        self.project_id = ''
        self.project_name = ''


class market:
    def __init__(self):
        self.id = ''
        self.market_name = ''


class bug_sort:
    def __init__(self):
        self.sort_id = ''
        self.sort_name = ''
