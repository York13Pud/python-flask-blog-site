# --- Import the required modules:
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    """This function creates the flask app and any required configuration setting that are used by the app."""
    
    
    # --- Import the required modules / blueprints used specifically by this function:
    from website.views import views
    from website.auth import auth
    from website.models import User
    
    # --- Setup the actual flask app and any required settings:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "testing"
    
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    
    # --- Initialise and create the database (if it's not found):
    db.init_app(app)
    create_database(app)
    
    
    # --- This section will be used to register the views with the app:
    app.register_blueprint(views, url_prefix = "/")
    app.register_blueprint(auth, url_prefix = "/")
        
    
    login_manager = LoginManager()
    login_manager.login_view = "auth.login" # If not logged in, which view should you be redirected to.
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    
    @app.context_processor
    def jinja_reusable_variables():
        from datetime import date
        
        current_year = date.today().year
        company_name = "My Blog Site"
        
        return dict(year=current_year, 
                    company = company_name)
        
    
    return app


def create_database(app):
    if not path.exists(f"website/{DB_NAME}"):
        db.create_all(app=app)
        print("Created Database!")
