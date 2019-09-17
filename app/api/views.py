# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/17 15:19
"""
from . import api


@api.route('/')
def index():
    return 'hello'
