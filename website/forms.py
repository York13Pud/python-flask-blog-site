from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField


class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    text = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Create Post")

    
class CreateCommentForm(FlaskForm):
    text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Create Comment")


class RegisterAccountForm(FlaskForm):
    email = EmailField("Email Address", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    password1 = PasswordField("Enter Password", validators=[DataRequired()])
    password2 = PasswordField("Enter Password Again", validators=[DataRequired()])
    submit = SubmitField("Register")
    
    
class LoginForm(FlaskForm):
    email = EmailField("Username", validators=[DataRequired()])
    password = PasswordField("Enter Password", validators=[DataRequired()])
    submit = SubmitField("Login")