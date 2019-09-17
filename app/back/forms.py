# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/17 22:58
"""
from flask_wtf import FlaskForm
from werkzeug.security import check_password_hash
from wtforms import StringField, validators, PasswordField


class LoginForm(FlaskForm):
    login = StringField(validators=[validators.required()])
    password = PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('Invalid user')

        # we're comparing the plaintext pw with the the hash from the db
        if not check_password_hash(user.password, self.password.data):
            # to compare plain text passwords use
            # if user.password != self.password.data:
            raise validators.ValidationError('Invalid password')

    # def get_user(self):
    #     return db.session.query(User).filter_by(login=self.login.data).first()


class RegistrationForm(FlaskForm):
    login = StringField(validators=[validators.required()])
    email = StringField()
    password = PasswordField(validators=[validators.required()])

    # def validate_login(self, field):
    #     if db.session.query(User).filter_by(login=self.login.data).count() > 0:
    #         raise validators.ValidationError('Duplicate username')

