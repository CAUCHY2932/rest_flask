# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/17 21:12
"""
from flask_admin import BaseView

from app import admin


class MyView(BaseView):
    def __init__(self, *args, **kwargs):
        self._default_view = True
        super(MyView, self).__init__(*args, **kwargs)
        self.admin = admin


# 解决不能extend admin的问题
render = MyView().render
