# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/17 15:21
"""
from app import db


class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50))
    addr = db.Column(db.String(50))
    gender = db.Column(db.SmallInteger, default=0)

    def __repr__(self):
        return '<User %r>' % self.name

#
#
# class Book(db.Model):
#     pass
