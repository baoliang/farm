#!/usr/bin/python
import os
import settings_run
import bjoern
from flask import Flask
from flaskext.mako import init_mako
from views.views import app
from views.account_view import account
from meinheld import patch
patch.patch_all()
web = Flask(__name__)
web.register_blueprint(app)
web.register_blueprint(account)
web.secret_key = os.urandom(24)
web.config.from_object('settings_run')
init_mako(web)
