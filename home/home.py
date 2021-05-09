from flask import Blueprint, render_template, session
import json
from flask_login import login_required

from dbutil import notice_util

homeBlueprint = Blueprint("home", __name__, static_folder="static", template_folder="template", url_prefix="/home")

@homeBlueprint.route("/")
@login_required
def homeIndex():
    name = session.get('name')
    user_type = session.get('user_type')
    notice_list = notice_util.getNotice()
    return render_template("home.html",name=name,user_type=user_type,notice_list=notice_list)

@homeBlueprint.route("/getNotice", methods=['POST','GET'])
@login_required
def getNotice():
    noticeList=notice_util.getNotice()
    # 使用lambda序列化
    data = json.dumps({"notice_list": noticeList}, default=lambda obj: obj.__dict__,
                      sort_keys=False)

    return data