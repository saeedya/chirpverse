from ccs.ccs import apiv1 as api
from ccs.resource.apiv1.currency import CurrencyConversionResource

api.add_resource(
    CurrencyConversionResource,
    "/currencies/convert",
    methods=["GET"],
    endpoint="currencies_convert"
)