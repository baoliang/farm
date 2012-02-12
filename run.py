#!/usr/bin/python
import os
import settings_run
from flask import Flask
from flaskext.mako import init_mako
from views.views import app
from views.sell_view import sell
from views.account_view import account
from views.news_view import news
from views import bp
web = Flask(__name__)
web.register_blueprint(bp)
web.register_blueprint(app)
web.register_blueprint(sell)
web.register_blueprint(account)
web.register_blueprint(news)
web.debug = settings_run.DEBUG
web.secret_key = os.urandom(24)
web.config.from_object('settings_run')
init_mako(web)
if __name__ ==  '__main__':
    web.run('192.168.1.254',5000)
