# -*- coding: utf-8 -*-
# © 2016 ONESTEiN BV (<http://www.onestein.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class hr_employee(models.Model):
    _inherit = 'hr.employee'

    related_ids = fields.One2many(
        'hr.employee.related', 'employee_id', string='Related')
