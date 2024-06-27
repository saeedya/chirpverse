from flask_restful import Resource
from ccs.controller.apiv1 import CurrencyConversionController

class CurrencyConversionResource(Resource):

    def get(self):
        return CurrencyConversionController.convert_currency()