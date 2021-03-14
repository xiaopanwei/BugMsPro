from flask import Blueprint, render_template, session
from flask_login import login_required

homeBlueprint = Blueprint("home", __name__, static_folder="static", template_folder="template", url_prefix="/home")

@homeBlueprint.route("/")
@login_required
def homeIndex():
    name = session.get('name')
    user_type = session.get('user_type')
    return render_template("home.html",name=name,user_type=user_type)