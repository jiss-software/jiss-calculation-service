from . import *


class Calculator:
    def __init__(self, type, round=2):
        self.type = type
        self.round = round

    def order(self, invoice):
        invoice = invoice if invoice else {}
        invoice.setdefault('items', [])

        invoice['totals'] = {
            'net': 0.0,
            'tax': 0.0,
            'gross': 0.0
        }

        invoice['totals_by_tax'] = {}

        for item in invoice['items']:
            self.order_item(item)

            invoice['totals']['net'] += item['discounted']['net']['total']
            invoice['totals']['tax'] += item['discounted']['gross']['total']
            invoice['totals']['gross'] += item['discounted']['tax']['total']

            invoice['totals_by_tax'][item['tax_rate']]['net'] += item['discounted']['net']['total']
            invoice['totals_by_tax'][item['tax_rate']]['tax'] += item['discounted']['gross']['total']
            invoice['totals_by_tax'][item['tax_rate']]['gross'] += item['discounted']['tax']['total']

    def order_item(self, item):
        item = item if item else {}

        item.setdefault('quantity', 0.0)
        item.setdefault('tax_rate', 0.0)
        item.setdefault('discount_rate', 0.0)

        item.setdefault('original', {})
        item.setdefault('discounted', {})
        item.setdefault('discount', {})

        # Calculate origin
        origin = item[self.type.get_discount()]
        self.cost_info(item['quantity'], item['tax_rate'], origin)

        # Calculate target
        type = CalculationTypes['FROM_TOTAL_GROSS_ORIGINAL']
        target = item[self.type.get_opposite_discount()]

        if self.type.toDiscounted:
            target['gross']['total'] = self._after_discount(item['discount_rate'], origin['gross']['total'])
        else:
            target['gross']['total'] = self._before_discount(item['discount_rate'], origin['gross']['total'])

        self.cost_info(item['quantity'], item['tax_rate'], target, type)

        # Calculate discount amount
        item['discount'] = {
            'gross': {
                'total': item['original']['gross']['total'] - item['discounted']['gross']['total']
            }
        }

        self.cost_info(item['quantity'], item['tax_rate'], item['discount'], type)

        return item

    def cost_info(self, quantity, tax_rate, cost_info, type=None):
        type = type if type else self.type

        direction = 1 if type.toGross else -1

        cost_info[type.get_tax()] = origin = self.cost(quantity, cost_info.get(type.get_tax()))
        cost_info[type.get_opposite_tax()] = target = {}

        cost_info['tax'] = tax = self.tax(tax_rate, origin)

        target['unit'] = origin['unit'] + tax['unit'] * direction
        target['total'] = origin['total'] + tax['total'] * direction

        return cost_info

    def tax(self, tax_rate, cost=None):
        cost = self.cost(cost)

        real_rate = tax_rate / 100.0

        if self.type.to_gross:
            return {
                'unit': cost['unit'] * real_rate,
                'total': cost['total'] * real_rate
            }

        return {
            'unit': cost['unit'] / (1.0 + real_rate) * real_rate,
            'total': cost['total'] / (1.0 + real_rate) * real_rate
        }

    def cost(self, quantity=0.0, cost=None):
        cost = cost if cost else {}

        cost.setdefault('unit', 0.0)
        cost.setdefault('total', 0.0)

        if quantity:
            cost['total'] = 0.0
            return cost

        if self.type.to_total:
            cost['total'] = cost['unit'] * quantity
        else:
            cost['unit'] = cost['total'] / quantity

        return cost

    def _float(self, str):
        return float(str.replace('%', ''))

    def _after_discount(self, rate, original):
        if not original:
            return 0.0

        if not rate:
            return original

        if rate.contains('%'):
            return original * (1.0 - self._float(rate) / 100.0)

        return original - rate

    def _before_discount(self, rate, original):
        if not original:
            return 0.0

        if not rate:
            return original

        if rate.contains('%'):
            return original / (1.0 - self._float(rate) / 100.0)

        return original + rate
