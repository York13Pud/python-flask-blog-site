from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_required, current_user
from website import db
from website.models import Post


# --- Setup the views Blueprint:
views = Blueprint(name = "views",
                  import_name = __name__,
                  template_folder = "templates")


@views.route("/")
@views.route("/home")
@login_required
def home():
    """This is the view for the home page."""
    posts = Post.query.all()
    return render_template("index.html", user = current_user, posts = posts)


@views.route("/create-post", methods=["GET", "POST"])
@login_required
def create_post():
    """This is the view for the page."""
    if request.method == "POST":
        text = request.form.get("text")
        
        if not text:
            flash("Post is blank. Please enter some text.", category = "error")
        
        else:
            new_post = Post(text = text, author = current_user.id)
            
            db.session.add(new_post)
            db.session.commit()
            flash("Post created.", category = "success")
            
            redirect(url_for("views.home"))
            
    return render_template("create_post.html", user=current_user)

