import json

from flask import Blueprint, render_template, request
from flask_login import login_required

from dbutil import upload_util, search_util

searchBlueprint = Blueprint("search", __name__, static_folder="static", template_folder="template",
                            url_prefix="/search")


@searchBlueprint.route("/searchindex")
@login_required
def searchIndex():
    client_list = upload_util.get_client_list()
    market_list = upload_util.get_market_list()
    return render_template("search.html", client_list=client_list, market_list=market_list)


@searchBlueprint.route("/searchresult",methods=['POST','GET'])
@login_required
def search():
    client_type = request.args.get('client_type')
    belong_project = request.args.get('belong_project')
    belong_bug_sort = request.args.get('belong_bug_sort')
    bug_title = request.args.get('bug_title')
    market = request.args.get('market')
    page =request.args.get('page')
    limit=request.args.get('limit')
    search_list=search_util.get_search_list(client_type, belong_project, belong_bug_sort, bug_title, market,page,limit)
    search_list_count = search_util.get_search_list_count(client_type, belong_project, belong_bug_sort, bug_title, market)

    search=json.dumps(search_list, default=lambda obj: obj.__dict__,
                      sort_keys=False)

    data = '{"code":0,"msg":"","count":'+str(search_list_count)+',"data":'+ search+'}'

    return data

