import tornado.ioloop
import tornado.web

from handlers.error import ErrorHandler

from routes import routes

import settings
from log import logger

class Application(tornado.web.Application):
    
    def __init__(self, routes, port):
        super().__init__(
            routes,
            default_handler_class=ErrorHandler,
            default_handler_args=dict(status_code=404),
        )
        self.listen(port)

    def run(self, ):
        logger.info("Starting server with settings: {}".format(settings.api))
        tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    app = Application(routes, settings.api.port)
    app.run()

