# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/9/17 11:06
"""
import os
from app import create_app


manager = create_app(os.getenv('FLASK_CONFIG') or 'default')


if __name__ == '__main__':
    manager.run(debug=True, port=5008)
