# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/17 15:19
"""
from flask import jsonify, request

from app import db
from app.models import User
from . import api
from .forms import RegistrationForm


@api.route('/')
def index():
    return 'hello'


@api.route('/reg_old', methods=['POST'])
def register_old():
    # old
    data = request.json
    user = User(email=data.get('email').lower(),
                name=data.get('username'),
                password=data.get('password'))
    db.session.add(user)
    db.session.commit()

    return jsonify(data)


@api.route('/register', methods=['POST'])
def register():
    form = RegistrationForm()
    if form.validate_for_api():
        user = User(name=form.username.data,
                    email=form.email.data,
                    password=form.password.data
                    )
        db.session.add(user)
        db.session.commit()
        return jsonify(msg='success!')
    return jsonify(msg='error')
