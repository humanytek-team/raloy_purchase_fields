# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from openerp import api
import pytz
from datetime import datetime, timedelta
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
import amount_to_text_es_MX


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.depends('amount_total')
    def compute_written_amount(self):
        #print 'compute_written_amount'
        #print 'self.amount_total: ',self.amount_total
        #print 'self.currency_id.name: ',self.currency_id.name
        self.amount_to_text = amount_to_text_es_MX.get_amount_to_text(self,self.amount_total, self.currency_id.name)

    amount_to_text = fields.Char('Written Amount', compute='compute_written_amount')