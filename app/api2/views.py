# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/17 15:19
"""
from . import api2


@api2.route('/')
def index():
    return 'hello'


