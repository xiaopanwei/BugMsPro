import json

from flask import Blueprint, render_template, request, session, url_for
from werkzeug.utils import redirect

from dbutil import upload_util

uploadBlueprint = Blueprint("upload", __name__, static_folder="static", template_folder="template", url_prefix="/upload")

@uploadBlueprint.route("/")
def uploadIndex():
    client_list = upload_util.get_client_list()
    market_list = upload_util.get_market_list()
    return render_template("upload.html", client_list=client_list, market_list=market_list)


@uploadBlueprint.route("/upload",methods=['POST'])
def upload():
    client_type = request.form.get('client_type')
    belong_project = request.form.get('belong_project')
    belong_bug_sort = request.form.get('belong_bug_sort')
    bug_title = request.form.get('bug_title')
    bug_content = request.form.get('bug_content')
    market = request.form.get('market')
    submit_person = session.get('user_id')
    upload_util.upload(client_type,belong_project,belong_bug_sort,bug_title,bug_content,market,submit_person)
    return redirect(url_for('home.homeIndex'))


@uploadBlueprint.route("/getprojectlist/<client_id>", methods=['POST','GET'])
def getprojectlist(client_id):
    project_list = upload_util.get_project_list(client_id)
    bug_sort_list=upload_util.get_bug_sort_list(client_id)
    #使用lambda序列化
    data=json.dumps({"project_list": project_list, "bug_sort_list": bug_sort_list},default=lambda obj:obj.__dict__,sort_keys=False)
    return data