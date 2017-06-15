import tornado.web

from handlers.base import BaseHandler

class ErrorHandler(tornado.web.ErrorHandler, BaseHandler):
    """
    Generic error handler
    """
    pass
