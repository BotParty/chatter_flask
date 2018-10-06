import logging

from flask import request
from flask_restplus import Resource
from api.restplus import api
from api.model.speech import speech as speech_model
from chatter import chatter

log = logging.getLogger(__name__)

ns = api.namespace('speech', description='get speech response')


@api.route('/speech')  # Create a URL route to this resource
class Speech(Resource):  # Create a RESTful resource


    @api.expect(speech_model)
    def post(self):
        """
        Creates a new blog category.
        """
        data = request.json
        text = data.get('text')
        response = chatter.chatbot.get_response(text)
        return {'output':response.text}
