from flask import Blueprint, render_template, session, url_for
from flask_login import login_required
from werkzeug.utils import redirect

from dbutil.mybug_util import getmybuglist, getmybuglist_count

mybugBlueprint = Blueprint("mybug", __name__, static_folder="static", template_folder="template",
                            url_prefix="/mybug")


@mybugBlueprint.route("/mybug/<page>")
@login_required
def mybugIndex(page):
    pageSize = 10
    user_id = session.get('user_id')
    buglist=getmybuglist(user_id,page, pageSize)
    count= getmybuglist_count(user_id)
    return render_template("mybug.html",count=count,buglist=buglist,page=int(page), pageSize=pageSize)


@mybugBlueprint.route("/bugdetails/<bug_id>")
@login_required
def bugdetails(bug_id):
    return render_template("bugdetails.html")

