from flask import Blueprint, url_for
from flask_login import login_required
from werkzeug.utils import redirect

from dbutil.bugDetail_util import get_bug_detail
from remind import email_send

remindBlueprint = Blueprint("remind", __name__, static_folder="static", template_folder="template",
                            url_prefix="/remind")

@remindBlueprint.route("/<bug_id>/<page>")
@login_required
def remind(bug_id,page):
    bug=get_bug_detail(bug_id)
    email_send.sendemail("949888408@qq.com", "bugId:"+str(bug.bug_id)+"  Bug内容："+bug.bug_content+"   等待处理")
    return redirect(url_for('mybug.mybugIndex',page=page))