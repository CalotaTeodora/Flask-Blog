from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "helloworld"
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database_name.db"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Post

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    # access information from a user given the my database
    # store the id of a user that is loge in
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(
            int(id)
        )  # try to find something and get the user object that matches the id

    return app
