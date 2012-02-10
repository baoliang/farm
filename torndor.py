import tornado.ioloop
import tornado.web
import app import app
if __name__ == "__main__":
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
