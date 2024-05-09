from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    posts = db.relationship(
        # reference all of this post that this user have
        # and creates relationships between post and user
        "Post",
        backref="user",
        passive_deletes=True,
    )  # backref allows to write post.user then access the id of the user


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    author = db.Column(
        db.Integer,
        db.ForeignKey(
            # take the id of the user that created this post
            # if the user is deleted , the post will be deleted too
            "user.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )
