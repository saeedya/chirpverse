from ccs.model import ExchangeRate
from ccs.util import jsonify

class CurrencyConversionController:
    
    def convert_currency():
        return jsonify(status=501, code=107) #Not Implemented