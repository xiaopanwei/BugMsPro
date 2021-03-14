from flask import Blueprint, render_template, session, request
from flask_login import login_required

from dbutil import upload_util, bugDetail_util
from dbutil.bugDetail_util import get_bug_detail

bugDetailBlueprint = Blueprint("bugDetail", __name__, static_folder="static", template_folder="template",
                            url_prefix="/bugDetail")


@bugDetailBlueprint.route("/<bugId>")
@login_required
def bugDetailIndex(bugId):
    bugDetail=get_bug_detail(bugId)
    canEdit='0'
    if bugDetail.submit_person == session.get('user_id') or session.get('user_type')=='0':
        canEdit='1'
    client_list = upload_util.get_client_list()
    market_list = upload_util.get_market_list()
    solve_state_list=upload_util.get_solve_state_list()
    solve_people_list = upload_util.get_solve_people_list()
    return render_template("bugDetail.html",client_list=client_list,market_list=market_list,bugDetail=bugDetail,
                           canEdit=canEdit,solve_state_list=solve_state_list,solve_people_list=solve_people_list)


@bugDetailBlueprint.route("/update",methods=['POST','GET'])
@login_required
def bugDetailUpdate():
    client_type = request.args.get('client_type')
    belong_bug_sort= request.args.get('belong_bug_sort')
    market = request.args.get('market')
    bug_title = request.args.get('bug_title')
    bug_content = request.args.get('bug_content')
    reject_reason = request.args.get('reject_reason')
    belong_project = request.args.get('belong_project')
    solve_state = request.args.get('solve_state')
    solve_person = request.args.get('solve_person')
    bug_id=request.args.get('bug_id')
    bugDetail_util.updata_bug_detail(bug_id,client_type,market,belong_bug_sort,bug_title,bug_content,reject_reason,belong_project,solve_state,solve_person)
    return '{"state":0,"msg":"更新成功"}'