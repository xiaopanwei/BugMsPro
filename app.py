from flask import Flask
from flask_login import LoginManager
from flask_apscheduler import APScheduler

from admin import admin
from bugdetail import bugdetail
from dbutil.mybug_util import getUnResultEmail
from home import home
from login import login
from login.User import User, query_user
from logout import logout
from mybug import mybug
from remind import remind, email_send
from search import search
from upload import upload

app = Flask(__name__)
# 定時任務
scheduler = APScheduler()
class Config(object):  # 创建配置，用类
    # 任务列表
    JOBS = [
        {
            'id': 'job',
            'func': 'app:email_job',  # 方法名
            'args': None,
            'trigger': 'interval',  # interval表示循环任务
            'seconds': 10800
        }
    ]
app.config.from_object(Config)

app.secret_key = '258258'
app.register_blueprint(login.loginBlueprint)
app.register_blueprint(upload.uploadBlueprint)
app.register_blueprint(search.searchBlueprint)
app.register_blueprint(mybug.mybugBlueprint)
app.register_blueprint(home.homeBlueprint)
app.register_blueprint(logout.logoutBlueprint)
app.register_blueprint(admin.adminBlueprint)
app.register_blueprint(bugdetail.bugDetailBlueprint)
app.register_blueprint(remind.remindBlueprint)
login_manager = LoginManager()  # 实例化登录管理对象
login_manager.login_view = '/'  # 设置用户登录视图函数 endpoint
login_manager.init_app(app)  # 初始化应用

@login_manager.user_loader
def load_user(user_id):
    if query_user(user_id) is not None:
        curr_user = User()
        curr_user.id = user_id
        return curr_user


@app.route("/")
def index():
    return login.loginIndex()


if __name__ == "__main__":
    # todo 定時任務
    # scheduler.init_app(app)
    # scheduler.start()
    app.run(debug=True)



def email_job():
    emailList=getUnResultEmail()
    for email in emailList:
        email_send.sendemail(email,"您有一个Bug已经超时了")







