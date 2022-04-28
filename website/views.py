from flask import Blueprint, render_template
from flask_login import login_required, current_user

# --- Setup the views Blueprint:
views = Blueprint(name = "views",
                  import_name = __name__,
                  template_folder = "templates")


@views.route("/")
@views.route("/home")
@login_required
def home():
    """This is the view for the home page. No parameters/arguments are defined/required"""
    return render_template("index.html", name = current_user.username)