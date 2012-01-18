import os
from gevent.wsgi import WSGIServer
from views import app
import settings_run
app.debug = settings_run.DEBUG
app.secret_key = os.urandom(24)
from flaskext.mako import init_mako
app.config.from_object('settings_run')
init_mako(app)
if __name__ ==  '__main__':
   http_server = WSGIServer(('', 8080), app)
   http_server.serve_forever()
