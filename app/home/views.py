# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/17 20:29
"""
from . import home


@home.route('/')
def index_home():
    return '<h1>welcome to my site!</h1>'
