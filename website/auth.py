from flask import Blueprint, render_template, redirect, url_for

auth = Blueprint("auth", __name__)


@auth.route("/login")
def home():
    return render_template("login.html")


@auth.route("/sign-up")
def sing_up():
    return render_template("singup.html")


@auth.route("/logout")
def logout():
    return redirect(url_for("views.home"))
