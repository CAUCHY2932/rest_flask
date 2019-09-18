# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/17 20:37
"""
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, LoginManager, current_user, logout_user, login_user
from sqlalchemy.sql.functions import user


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)
login = LoginManager(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))


class MyModelView(ModelView):

    def is_accessible(self):

        return current_user.if_authenticated


admin = Admin(app)
admin.add_view(MyModelView(User, db.session))


@app.route("/login")
def login_f():
    user = User.query.get(1)
    login_user(user)
    return "logged in!"


@app.route("/logout")
def logout():
    logout_user()

    return "log out!"


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


if __name__ == "__main__":
    app.run(debug=True)
