import tornado.ioloop
import tornado.web
import tornado.httpserver
from tornado.options import options, parse_command_line

from settings import settings
from urls import url_pattern


class TornadoBoilerplate(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, url_pattern, **settings)


if __name__ == '__main__':
    parse_command_line()
    app = TornadoBoilerplate()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(options.port)
    print('Server is listening at {port}...'.format(port=options.port))
    tornado.ioloop.IOLoop.instance().start()

