class CalculationType:
    def __init__(self, to_total, to_gross, to_discounted):
        self.to_discounted = to_discounted
        self.to_gross = to_gross
        self.to_total = to_total

    def get_quantitative(self):
        return 'unit' if self.to_total else 'total'

    def get_tax(self):
        return 'net' if self.to_gross else 'gross'

    def get_discount(self):
        return 'original' if self.to_discounted else 'discounted'

    def get_opposite_quantitative(self):
        return 'total' if self.to_total else 'unit'

    def get_opposite_tax(self):
        return 'gross' if self.to_gross else 'net'

    def get_opposite_discount(self):
        return 'discounted' if self.to_discounted else 'original'

CalculationTypes = {
    'FROM_ITEM_NET_ORIGINAL': CalculationType(True, True, True),
    'FROM_ITEM_GROSS_ORIGINAL': CalculationType(True, False, True),

    'FROM_TOTAL_NET_ORIGINAL': CalculationType(False, True, True),
    'FROM_TOTAL_GROSS_ORIGINAL': CalculationType(False, False, True),

    'FROM_ITEM_NET_DISCOUNT': CalculationType(True, True, False),
    'FROM_ITEM_GROSS_DISCOUNT': CalculationType(True, False, False),

    'FROM_TOTAL_NET_DISCOUNT': CalculationType(False, True, False),
    'FROM_TOTAL_GROSS_DISCOUNT': CalculationType(False, False, False)
}
