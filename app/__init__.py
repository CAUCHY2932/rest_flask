# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/17 11:06
"""
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_script import Manager


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from app.api import api as api_bp
    app.register_blueprint(api_bp)

    db.init_app(app=app)
    migrate = Migrate(app=app, db=db)

    manager = Manager(app=app)
    manager.add_command('db', MigrateCommand)

    from app.models import User

    return app
