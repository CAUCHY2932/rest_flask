# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/18 15:24
"""
from flask import Blueprint

authen = Blueprint('authen', __name__)

from . import views


