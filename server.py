from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from views import app

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(8080)
if __name__ ==  '__main__':
    IOLoop.instance().start()
