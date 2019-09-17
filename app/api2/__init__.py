# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/17 15:19
"""
from flask import Blueprint

api2 = Blueprint('api2', __name__)

from . import views
