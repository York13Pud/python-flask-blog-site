from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_required, current_user
from website import db
from website.models import Post, User


# --- Setup the views Blueprint:
views = Blueprint(name = "views",
                  import_name = __name__,
                  template_folder = "templates")


@views.route("/")
@views.route("/home")
def home():
    """This is the view for the home page."""
    posts = Post.query.all()
    return render_template("index.html", user = current_user, posts = posts)


@views.route("/post/<int:post_id>", methods=["GET"])
def read_post(post_id):
    return redirect(url_for("views.home"))


@views.route("/posts/<string:username>")
def posts(username):
    """This is the view for a particular user / authors blog posts."""
    user = User.query.filter_by(username = username).first()
    
    if not user:
        flash(f"Username does not exist.", category = "error")
        return redirect(url_for("views.home"))
    
    posts = Post.query.filter_by(author = user.id).all()
        
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
    post_to_delete = Post.query.filter_by(id=post_id).first()
    
    if not post_to_delete:
        flash(f"Post {post_id} does not exist.", category = "error")
        
    elif post_to_delete.author == current_user.id:
        db.session.delete(post_to_delete)
        db.session.commit()
        flash(f"Post {post_id} has been deleted.", category = "success")
    
    else:
        flash(f"You are not authorised to delete that post.", category = "error")
    
    return redirect(url_for("views.home"))


@views.route("/edit/<int:post_id>", methods=["GET"])
@login_required
def edit_post(post_id):
    return redirect(url_for("views.home"))