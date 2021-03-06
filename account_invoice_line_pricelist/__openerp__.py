# -*- coding: utf-8 -*-
# © 2016 ONESTEiN BV (<http://www.onestein.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Account Invoice Line Pricelist',
    'images': [],
    'summary': """Prices on invoice products based on partner pricelists""",
    'version': '9.0.1.0.0',
    'category': 'Accounting & Finance',
    'author': 'ONESTEiN BV',
    'website': 'http://www.onestein.eu',
    'license': 'AGPL-3',
    'depends': [
        'account',
        'product',
    ],
    'data': [
        'views/account_invoice.xml',
    ],
}
