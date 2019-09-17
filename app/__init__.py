# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/17 11:06
"""
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from config import config


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # api = Api(app)
    #
    # from app.api.routes import HelloWorld
    # api.add_resource(HelloWorld, '/')

    from app.api2 import api2 as api2_bp
    app.register_blueprint(api2_bp)

    # register plugins
    db.init_app(app=app)

    return app
