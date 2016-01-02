import core
import domain
import tornado
from bson.json_util import loads


class CalculateOrderHandler(core.BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def put(self):
        self.logger.info('Request to calculate order')

        default_type = domain.CalculationTypes['FROM_ITEM_NET_ORIGINAL']
        type = domain.CalculationTypes.get(self.request.headers.get('X-JISS-CALCULATION-TYPE'), default_type)

        self.response_json(domain.Calculator(type).order(loads(self.request.body)))
