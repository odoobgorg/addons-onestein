# -*- coding: utf-8 -*-
# © 2016 ONESTEiN BV (<http://www.onestein.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class hr_employee_related(models.Model):
    _name = 'hr.employee.related'
    _description = 'Employee related'

    employee_id = fields.Many2one('hr.employee', string='Employee')
    name = fields.Char("First name")
    last_name = fields.Char("Last name")
    birth_name = fields.Char("Birth name")
    gender = fields.Selection(
        [('male', 'Male'),
         ('female', 'Female')],
        string='Gender')
    relation = fields.Char("Employee relation")
    bsn_number = fields.Char("BSN")
    birth_date = fields.Date(string="Birth date")
    telephone = fields.Char("Telephone")
    note = fields.Text("Note")
