from flask import Blueprint, render_template, session, request, redirect, url_for
from flask_login import login_required

from dbutil import admin_util, notice_util

adminBlueprint = Blueprint("admin", __name__, static_folder="static", template_folder="template",
                            url_prefix="/admin")


@adminBlueprint.route("/")
@login_required
def adminIndex():
    name = session.get('name')
    return render_template("admin.html",name=name)

#发布公告
@adminBlueprint.route("/notice")
@login_required
def noticeIndex():
    notice_list=notice_util.getNotice()
    return render_template("notice.html",notice_list=notice_list)


@adminBlueprint.route("/releaseNotice",methods=['POST','GET'])
@login_required
def releaseNotice():
    notice_title=request.args.get('notice_title')
    notice_url = request.args.get('notice_url')
    state=admin_util.addNotice(notice_title,notice_url)
    if state=='0':
        return '{"state":0,"msg":"发布成功"}'
    else:
        return '{"state":1,"msg":"发布失败"}'

@adminBlueprint.route("/deleteNotice/<notice_id>",methods=['POST','GET'])
@login_required
def deleteNotice(notice_id):
    notice_util.deleteNotice(notice_id)
    return redirect(url_for('admin.noticeIndex'))
#添加用户
@adminBlueprint.route("/addUser")
@login_required
def addUser():
    return render_template("addUser.html")

#添加用户
@adminBlueprint.route("/doAddUser",methods=['POST','GET'])
@login_required
def doAddUser():
    user_name = request.args.get('user_name')
    user_password = request.args.get('user_password')
    user_email = request.args.get('user_email')
    user_phone = request.args.get('user_phone')
    user_type = request.args.get('user_type')
    state = admin_util.addUser(user_name, user_password,user_email,user_phone,user_type)
    if state == '0':
        return '{"state":0,"msg":"添加产品成功"}'
    else:
        return '{"state":1,"msg":"添加产品失败"}'


#添加产品
@adminBlueprint.route("/addProject")
@login_required
def addProject():
    return render_template("addProject.html")


@adminBlueprint.route("/doAddProject",methods=['POST','GET'])
@login_required
def doAddProject():
    project_name = request.args.get('project_name')
    PC = request.args.get('PC')
    Android = request.args.get('Android')
    IOS = request.args.get('IOS')
    if (PC== "undefined" and IOS == "undefined" and Android == "undefined" ):
        return '{"state":2,"msg":"至少选择一个客户端"}'
    if(PC=='0'):
        admin_util.addProject(project_name, PC)
    if (Android == '1'):
        admin_util.addProject(project_name, Android)
    if (IOS == '2'):
        admin_util.addProject(project_name, IOS)

    return '{"state":0,"msg":"添加成功"}'


#添加产品分类
@adminBlueprint.route("/addSort")
@login_required
def addSort():
    return render_template("addSort.html")

@adminBlueprint.route("/doAddSort",methods=['POST','GET'])
@login_required
def doAddSort():
    sort_name = request.args.get('sort_name')
    PC = request.args.get('PC')
    Android = request.args.get('Android')
    IOS = request.args.get('IOS')
    if (PC== "undefined" and IOS == "undefined" and Android == "undefined" ):
        return '{"state":2,"msg":"至少选择一个客户端"}'
    if(PC=='0'):
        admin_util.addSort(sort_name, PC)
    if (Android == '1'):
        admin_util.addSort(sort_name, Android)
    if (IOS == '2'):
        admin_util.addSort(sort_name, IOS)

    return '{"state":0,"msg":"添加成功"}'


