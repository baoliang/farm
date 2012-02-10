#!/usr/bin/python
import os
from views import app
import settings_run
app.debug = settings_run.DEBUG
app.secret_key = os.urandom(24)
from flaskext.mako import init_mako
app.config.from_object('settings_run')
init_mako(app)
if __name__ ==  '__main__':
    app.run('192.168.1.254',5000)
