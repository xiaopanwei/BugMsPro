from flask import Flask
from flask_login import LoginManager

from admin import admin
from bugdetail import bugdetail
from home import home
from login import login
from login.User import User, query_user
from logout import logout
from mybug import mybug
from remind import remind
from search import search
from upload import upload

app = Flask(__name__)
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
    app.run(debug=True)
