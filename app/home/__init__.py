# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/17 18:12
"""
from flask import Blueprint

home = Blueprint('home', __name__)

from . import views
