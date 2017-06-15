import logging
import sys


FORMAT = u"[%(asctime)s | %(levelname)s | %(name)s | %(filename)s:%(lineno)s] %(message)s"

logger = logging.getLogger('glowing-journey')
loggers = [
    logger,
    logging.getLogger("tornado.access"),  # per-request logging for Tornado's HTTP Servers
    logging.getLogger("tornado.application"),  # errors from application code
    logging.getLogger("tornado.general"),  # general-purpose logging from Tornado itself
]

formatter = logging.Formatter(FORMAT)

handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(formatter)
handler.setLevel("DEBUG")

for each_logger in loggers:
    each_logger.addHandler(handler)
    each_logger.propagate = False
    each_logger.setLevel("DEBUG")
