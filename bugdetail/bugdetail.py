import calendar
import os
import shutil
import time
import oss2
from flask import Blueprint, render_template, session, request, jsonify, make_response, url_for
from flask_login import login_required
from werkzeug.utils import secure_filename, redirect

from dbutil import upload_util, bugDetail_util, image_util
from dbutil.bugDetail_util import get_bug_detail
from modal import ossModal

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
    image_path= image_util.find_image_by_bugid(bugId)
    return render_template("bugDetail.html",client_list=client_list,market_list=market_list,bugDetail=bugDetail,
                           canEdit=canEdit,solve_state_list=solve_state_list,solve_people_list=solve_people_list,image_path=image_path)


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
    solve_method=request.args.get('solve_method')
    version=request.args.get('version')
    bugDetail_util.updata_bug_detail(bug_id,client_type,market,belong_bug_sort,bug_title,bug_content,reject_reason,
                                     belong_project,solve_state,solve_person,version,solve_method)
    return '{"state":0,"msg":"更新成功"}'


@bugDetailBlueprint.route("/loadimage/<bugid>", methods=['POST'])
def imageload(bugid):
    if request.method == 'POST':
        f = request.files['file']
        if not (f and allowed_file(f.filename)):
            return jsonify({"error": 1001, "msg": "请检查上传的图片类型，仅限于png、PNG、jpg、JPG、bmp"})
        ossmodal=ossModal()
        # 秒级时间戳
        imagename = str(bugid)+"_"+str(calendar.timegm(time.gmtime()))+ "." + f.filename.rsplit('.', 1)[1]
        auth=oss2.Auth(ossmodal.keyId,ossmodal.keySecret)
        bucket=oss2.Bucket(auth,ossmodal.url,"xpw-pro")
        # 查看阿里云官方文档
        bucket.put_object(imagename,f)
        image_util.insertimage(bugid,ossmodal.public_url+imagename)
        # 上传到服务器本地
        # upload_path = os.getcwd() +'/static/image/'+secure_filename(imagename)  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        # f.save(upload_path)
        #
        # image_data = open(upload_path, "rb").read()
        # response = make_response(image_data)
        # response.headers['Content-Type'] = 'image'
        # print(response)
        return jsonify({"error": 0, "msg": "上传图片成功"})


@bugDetailBlueprint.route("/deleteImage/<bug_id>/<image_id>")
def doDelete(bug_id ,image_id):
    image_util.delbyimageid(image_id)
    # imagename=image_util.find_imagename_by_id(image_id)
    # path= os.getcwd() +'/static/image/'+secure_filename(imagename)
    # if os.path.exists(path):
    #     nowtime=str(int(time.time()))
    #     imagename=imagename.rsplit('.', 1)[0]+'_'+nowtime+'.'+imagename.rsplit('.', 1)[1]
    #     targetPath = os.getcwd() + '/static/deleteImage/' + secure_filename(imagename)
    #     shutil.move(path, targetPath)
    #     print('正在移动文件...')
    #
    #
    # # 循环处理完后
    # print('处理完成！')
    return redirect(url_for('bugDetail.bugDetailIndex',bugId=bug_id))


# 设置允许的文件格式
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS