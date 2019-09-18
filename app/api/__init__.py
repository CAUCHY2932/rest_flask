# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/17 15:19
"""
from flask import Blueprint

api = Blueprint('api', __name__)

# from . import user, errors
from . import user, errors, authentication
