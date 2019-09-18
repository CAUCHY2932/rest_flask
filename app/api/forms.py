# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/18 10:27
"""
from flask import request
from wtforms import PasswordField, StringField
from wtforms.form import Form
from wtforms.validators import DataRequired, Length, Email, Regexp

from app.api.errors import parameter_exception


class BaseForm(Form):
    def __init__(self):
        data = request.get_json(silent=True)
        args = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **args)

    # 自定义校验器，并处理错误
    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            # form errors
            return parameter_exception(message=self.errors)
        return self


# class BaseClientForm(Form):
#     secretkey = PasswordField(validators=[validators.DataRequired("秘钥不能为空..."),
#                                           validators.Length(min=6, max=16, message="密码长度必须为6-16位")])
#
#     def __init__(self, formdata=None, obj=None, prefix='', data=None, meta=None, **kwargs):
#         super().__init__(formdata=formdata, obj=obj, prefix=prefix, data=data, meta=meta, **kwargs)
#
#     # 自定义校验器，并处理异常！
#     def validate_for_api(self):
#         if not super().validate():
#             raise FromsParameterException(self.errors)

class RegisterForm(BaseForm):
    pass


class RegistrationForm(BaseForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    username = StringField('Username', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Usernames must have only letters, numbers, dots or '
               'underscores')])
    password = PasswordField('Password', validators=[
        DataRequired()])
