class HandlerError(Exception):
    code = 500
    message = "Uncaught Exception"
    def __init__(self, message=None, code=None):
        self.code = code or self.code
        self.message = message or self.message
        super().__init__(message)


class BadRequestError(HandlerError):
    code = 400
    message = "400 Bad Request"


class UnauthorizedError(HandlerError):
    code = 401
    message = "401 Unauthorized"


class ForbiddenError(HandlerError):
    code = 403
    message = "403 Forbidden"


class NotFoundError(HandlerError):
    code = 404
    message = "404 Not Found"
