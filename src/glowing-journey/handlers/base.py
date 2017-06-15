from decimal import Decimal

import json

import tornado.web
import handlers.exceptions


class BaseHandler(tornado.web.RequestHandler):

    def initialize(self):
        """
            RequestHandler default initialization method.
        """
        self.data = None
        self.errors = []

    def set_default_headers(self):
        """
            Make BaseHandler CORS capable.
        """
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')

    def set_data(self, data):
        self.data = data

    def set_error(self, error):
        self.errors.append(error)

    def get_argument(self, argument_name, default_value=None, argument_type=None):
        argument = super().get_argument(argument_name, default_value) 
        if argument_type != None and argument != None:
            argument = self.cast(argument, argument_name, argument_type)
        return argument

    def cast(self, variable, variable_name, variable_type):
        try:
            return variable_type(variable)
        except ValueError as e:
            raise handlers.exceptions.BadRequestError("Invalid type for `{}` (should be: {})".format(variable_name, variable_type.__name__))


    def options(self):
        """
            Used for OPTION queries
        """
        self.set_status(204)
        self.finish()

    def write_response(self):
        """
            Used for normal operation.
        """
        response = {
            "data": self.data,
            "errors": self.errors,
        }
        self.write(json.dumps(response))

    def write_error(self, status_code, exc_info, **kwargs):
        """
            Used for uncaught exception.
        """
        response = {
            "data": None,
            "errors": [ str(exc_info[1]) ]
        }

        self.set_status(status_code)
        self.write(json.dumps(response))
