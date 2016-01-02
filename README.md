Calculation Service
===================

Service for calculations.

Types of Calculations
---------------------

Codes:

* FROM_ITEM_NET_ORIGINAL
* FROM_ITEM_GROSS_ORIGINAL
* FROM_TOTAL_NET_ORIGINAL
* FROM_TOTAL_GROSS_ORIGINAL
* FROM_ITEM_NET_DISCOUNT
* FROM_ITEM_GROSS_DISCOUNT
* FROM_TOTAL_NET_DISCOUNT
* FROM_TOTAL_GROSS_DISCOUNT

ITEM - Means that base for all calculations will be Unit price, TOTAL is opposite.

NET - Means that base for all calculations will be tax before tax, GROSS is opposite.

ORIGINAL - Means that base for all calculations will be price before discount, DISCOUNT is opposite.

For all types of calculations using algorithms which apply discount on total amount.

Data Format
-----------

Structure of order:

    {
        'items': [
            <order_item>,
            <order_item>,
            <order_item>
        ],

        'totals': {
            'net': <float>,
            'tax': <float>,
            'gross': <float>
        }

        'totals_by_tax': {
            '<rate_1: float>': {
                'net': <float>,
                'tax': <float>,
                'total': <float>
            },
            '<rate_2: float>': {
                'net': <float>,
                'tax': <float>,
                'total': <float>
            }
            '<rate_3: float>': {
                'net': <float>,
                'tax': <float>,
                'total': <float>
            }
        }
    }

Structure of order_item:

    {
        'quantity': <float>,

        'tax_rate': <float>,
        'discount': <float/string>,

        'original': <cost_info>,
        'discounted': <cost_info>
    }

Structure of cost_info

    {
        'net': <cost>,
        'tax': <cost>,
        'gross': <cost>
    }


Structure of cost

    {
        'unit': <float>
        'total' <float>
    }
