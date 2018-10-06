import logging

from flask_restplus import Api

log = logging.getLogger(__name__)

api = Api(version='1.0', title='Chatterbot API',
          description='Using Chatterbot with Flask')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

