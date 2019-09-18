# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/17 17:14
"""
from flask import g, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_login import current_user

from ..models import User
from . import api
from .errors import unauthorized, forbidden

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(email_or_token, password):
    if email_or_token == '':
        return False
    if password == '':
        g.current_user = User.verify_auth_token(email_or_token)
        g.token_used = True
        return g.current_user is not None
    user = User.query.filter_by(email=email_or_token.lower()).first()
    print(user)
    print(user.id)
    if not user:
        return False
    g.current_user = user
    g.token_used = False
    print(g)
    return user.verify_password(password)


@auth.error_handler
def auth_error():
    return unauthorized('Invalid credentials')


@api.before_request
@auth.login_required
def before_request():
    # g.current_user = current_user
    print('before req is_an', g.current_user.is_anonymous)
    print('before req confirm', g.current_user.confirmed)
    if not g.current_user.is_anonymous and \
            not g.current_user.confirmed:
        return forbidden('Unconfirmed account')


@api.route('/tokens', methods=['POST'])
def get_token():
    # return jsonify(msg='success!')
    print(g.current_user.is_anonymous)
    print(g.token_used)
    if g.current_user.is_anonymous or g.token_used:
        return unauthorized('Invalid credentials')
    print(g.current_user)
    return jsonify({'token': g.current_user.gen_auth_token(
        expire=3600), 'expiration': 3600})
