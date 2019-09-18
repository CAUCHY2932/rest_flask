# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/17 11:20
"""
import os


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 生成token，要用
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    @staticmethod
    def init_app(app):
        pass
    pass


class DevConfig(Config):
    DEBUG = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'postgresql://postgres:123456@localhost/rest'

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)
        pass
    pass


class ProdConfig(Config):
    pass


config = dict(prod=ProdConfig, dev=DevConfig, default=DevConfig)
