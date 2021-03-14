from flask import Blueprint, render_template, url_for, session
from flask_login import login_user
from werkzeug.utils import redirect

from dbutil import login_util
from login.User import User, addusers

loginBlueprint = Blueprint("login", __name__, static_folder="static", template_folder="template", url_prefix="/login")


@loginBlueprint.route("/login")
def loginIndex():
    return render_template("login.html", ss="display:none;")


@loginBlueprint.route("/loginResult/<name>/<pwd>", methods=['POST'])
def loginResult(name, pwd):
    if int(login_util.is_exist(name)) > 0:
        if login_util.find_user_by_name(name).password == pwd:
            return '{"state":0,"msg":"账号密码正确"}'
        else:
            return '{"state":1,"msg":"密码不正确"}'
    else:
        return '{"state":2,"msg":"账号不存在"}'


@loginBlueprint.route("/loginSucess/<name>/<pwd>")
def loginSucess(name, pwd):
    curr_user = User()
    curr_user.id = name
    addusers({'id': name, 'username': name, 'password': pwd})
    user=login_util.find_user_by_name(name)
    session['name'] = name
    session['user_id'] = user.id
    session['user_type'] =user.type
    # 通过Flask-Login的login_user方法登录用户
    login_user(curr_user)
    if user.type=='1':
        return redirect(url_for('home.homeIndex'))
    else:
        return redirect(url_for('admin.adminIndex'))
