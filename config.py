# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/17 11:20
"""
import os


class Config:

    @staticmethod
    def init_app(app):
        pass
    pass


class DevConfig(Config):
    DEBUG = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'postgresql://postgres:123456@localhost/dev'

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)
        pass
    pass


class ProdConfig(Config):
    pass


config = dict(prod=ProdConfig, dev=DevConfig, default=DevConfig)
