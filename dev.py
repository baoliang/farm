#!/usr/bin/python
import os
import settings_run
from flask import Flask
from flaskext.mako import init_mako
from views.views import app
from views.account_view import account

web = Flask(__name__)

web.register_blueprint(app)
web.register_blueprint(account)
web.debug = settings_run.DEBUG
web.secret_key = os.urandom(24)
web.config.from_object('settings_run')
init_mako(web)

if __name__ ==  '__main__':
    web.run('127.0.0.1',8000)
