# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/17 20:29
"""
from flask_admin import BaseView

from app.home.render_html import render
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
