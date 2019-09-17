# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/17 17:21
"""

from flask import jsonify
from flask.debughelpers import FormDataRoutingRedirect

from app.exceptions import ValidationError
from . import api


def bad_request(message):
    response = jsonify({'error': 'bad request', 'message': message})
    response.status_code = 400
    return response


def unauthorized(message):
    response = jsonify({'error': 'unauthorized', 'message': message})
    response.status_code = 401
    return response


def forbidden(message):
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = 403
    return response


@api.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])


# 这个属于系统类错误，不用自定义
@api.app_errorhandler(404)
def page_not_found(e):
    response = jsonify(msg=str(e))
    response.status_code = 404
    return response


@api.app_errorhandler(405)
def method_not_allow(e):
    response = jsonify(msg=str(e))
    response.status_code = 405
    return response


@api.app_errorhandler(500)
def interval_error(e):
    response = jsonify(msg=str(e))
    response.status_code = 500
    return response


# 路由错误处理
@api.app_errorhandler(FormDataRoutingRedirect)
def route_error(e):
    response = jsonify(msg=str(e))
    response.status_code = 500
    return response
