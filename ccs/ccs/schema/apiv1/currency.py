from ccs.ccs import ma
from ccs.model import ExchangeRate

class ExchangeRateSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ExchangeRate

class CurrencyConversionSchema(ma.Schema):
    amount = ma.Float(required=True)
    from_currency = ma.String(required=True)
    to_currency = ma.String(required=True)

class CurrencyConversionResultSchema(ma.Schema):
    amount = ma.Float()
    from_currency = ma.String()
    to_currency = ma.String()
    result = ma.Float()