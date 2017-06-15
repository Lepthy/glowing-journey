import json

from handlers.exceptions import HandlerError
from handlers.base import BaseHandler

from models.users import ContactModel


class Contacts(BaseHandler):
    model = ContactModel()

    def post(self):
        try:
            search_payload = json.loads(self.request.body) if self.request.body else None
            size = self.get_argument("size", default_value=10, argument_type=int)
            data = self.model.match(search_payload=search_payload, size=size)
        except HandlerError as e:
            self.set_error(e.message)
            self.set_status(e.code)
        except KeyError as e:
            self.set_error(str(e))
            self.set_status(400)
        else:
            self.set_data(data)

        self.write_response()
