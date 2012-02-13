#!/usr/bin/python
import os
import settings_run
from flask import Flask
from flaskext.mako import init_mako
from views.views import app
from views.sell_view import sell
from views.account_view import account
from views.news_view import news
from meinheld import patch 

patch.patch_all() 

from meinheld import server 
web = Flask(__name__)
web.register_blueprint(app)
web.register_blueprint(sell)
web.register_blueprint(account)
web.register_blueprint(news)
web.debug = settings_run.DEBUG
web.secret_key = os.urandom(24)
web.config.from_object('settings_run')
init_mako(web)

