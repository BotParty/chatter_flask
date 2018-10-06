from flask_restplus import fields
from api.restplus import api

speech = api.model('Speech input', {
    'text': fields.String(required=True, description='Input text'),
})