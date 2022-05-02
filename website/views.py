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
        title = request.form.get("title")
        
        if not text:
            flash("Post is blank. Please enter some text.", category = "error")
        
        elif not title:
            flash("Title is blank. Please enter a title.", category = "error")
            
        else:
            new_post = Post(title = title, text = text, author = current_user.id)
            
            db.session.add(new_post)
            db.session.commit()
            flash("Post created.", category = "success")
            
            return redirect(url_for("views.home"))
            
    return render_template("create_post.html", user=current_user)

@views.route("/delete/<int:post_id>", methods=["GET"])
@login_required
def delete_post(post_id):
    post_to_delete = Post.query.get(post_id)
    
    if post_to_delete.author == current_user.id:
        
        db.session.delete(post_to_delete)
        db.session.commit()
        flash(f"Post {post_id} has been deleted.", category = "success")
    
        return redirect(url_for("views.home"))
    
    else:
        flash(f"You are not authorised to delete that post.", category = "error")
        return redirect(url_for("views.home"))


@views.route("/edit/<int:post_id>", methods=["GET"])
@login_required
def edit_post(post_id):
    return redirect(url_for("views.home"))


@views.route("/post/<int:post_id>", methods=["GET"])
@login_required
def read_post(post_id):
    return redirect(url_for("views.home"))