from odoo import models, fields, api
from datetime import datetime
from . import jdatetime

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    jalali_date = fields.Char(string='Jalali Date', compute='_compute_jalali_date', store=True)

    @api.depends('create_date')
    def _compute_jalali_date(self):
        for record in self:
            if record.create_date:
                gregorian_date = fields.Datetime.from_string(record.create_date)
                jalali_date = jdatetime.date.fromgregorian(date=gregorian_date.date())
                record.jalali_date = jalali_date.strftime('%Y/%m/%d')
