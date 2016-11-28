import loom.routing
import loom.database

import tornado.ioloop
import tornado.web

from tornado.options import define as define_option, options, parse_command_line as parse_options

define_option('port', default=8080, help='run on the given port', type=int)
define_option('db-host', default='localhost', help='address of the MongoDB server')
define_option('db-port', default=27017, help='MongoDB connection port', type=int)


def start_server(port, routes):
    app = tornado.web.Application(routes)
    app.listen(port)
    print("Starting server at {}:{}".format('localhost', port))
    print("Press ^C to quit.")
    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        print("\b\bQuitting...")
    finally:
        tornado.ioloop.IOLoop.current().stop()


if __name__ == '__main__':
    parse_options()

    loom.database.set_db_host(options.db_host)
    loom.database.set_db_port(options.db_port)

    start_server(options.port, loom.routing.ROUTES)
