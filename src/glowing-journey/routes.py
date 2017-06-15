"""
Add routes here in logical subgroups and merge theme with
routes = A + B + C
"""

from tornado.web import StaticFileHandler
from handlers.users import Contacts


static = [
    ('/static/(.*)', StaticFileHandler, {'path': "src/glowing-journey/static"}),
]

users = [
    (r"/contacts", Contacts),
]

routes = static + users
