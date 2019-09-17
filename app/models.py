# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/17 15:21
"""
from flask import current_app
from flask_admin.contrib.sqla import ModelView
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from flask_login import UserMixin
from app import admin


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    # __table_args__ = {
    #     'schema': 'dev'
    # }
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password_hash = db.Column(db.String(128))
    addr = db.Column(db.String(50))
    gender = db.Column(db.SmallInteger, default=0)

    def __repr__(self):
        return '<User %r>' % self.name

    def gen_auth_token(self, expire):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expire)
        return s.dumps(dict(id=self.id))

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except Exception as e:
            print('[error]-%s' % e)
            return None
        return User.query.get(data['id'])

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


