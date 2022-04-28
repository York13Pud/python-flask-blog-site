from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from website import db
from website.models import User
from werkzeug.security import generate_password_hash, check_password_hash

# --- Setup the auth Blueprint:
auth = Blueprint(name = "auth",
                  import_name = __name__,
                  template_folder = "templates/auth")


@auth.route("/login", methods = ["GET", "POST"])
def login():
    """This is the view for the login page. No parameters/arguments are defined/required."""
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("logged in.", category = "success")
                login_user(user, remember = True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect password.", category = "error")
        else:
            flash("Email does not exist.", category = "error")
    
    return render_template("login.html")


@auth.route("/logout", methods = ["GET", "POST"])
@login_required
def logout():
    """This is the view for the logout page. No parameters/arguments are defined/required."""
    logout_user()
    return redirect(url_for("views.home"))


@auth.route("/register", methods = ["GET", "POST"])
def register():
    """This is the view for the register page. No parameters/arguments are defined/required."""
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()
        
        if email_exists:
            flash("This email address is already in use.", category = "error")
        elif username_exists:
            flash("The username is already in use.", category = "error")
        elif password1 != password2:
            flash("The passwords do not match.", category = "error")
        elif len(username) < 5:
            flash("The username is too short (5 or more charecters needed).", category = "error")
        elif len(password1) < 6:
            flash("The username is too short (5 or more charecters needed).", category = "error")
        else:
            new_user = User(email = email,
                            username = username,
                            password = generate_password_hash(password1, method = "sha256"))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember = True)
            flash("User created!")
            return redirect(url_for("views.home"))
            
                           
    return render_template("register.html")