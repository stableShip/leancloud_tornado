# coding=utf-8
__author__ = 'JIE'

import tornado.ioloop
import tornado.web
import tornado.wsgi
import os


class TestHander(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("index.html")


settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "public"),
    "template_path": os.path.join(os.path.dirname(__file__), "views"),
    "gzip": True,
    "debug": True,
}

app = tornado.wsgi.WSGIApplication([
    ("/", TestHander),
], **settings)




# if __name__ == "__main__":
#     app.listen(8888)
#     print 'server start'
#     tornado.ioloop.IOLoop.current().start()
