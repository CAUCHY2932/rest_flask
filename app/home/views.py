# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/17 20:29
"""
from flask_admin import BaseView
from flask import request, jsonify

from app import db
from app.home.render_html import render
from app.models import User
from . import home
from flask import render_template


# @home.route('/')
# def index_home():
#     return render_template('admin/base.html')
#
#
# @home.route('/form')
# def form():
#     return render('login.html')
