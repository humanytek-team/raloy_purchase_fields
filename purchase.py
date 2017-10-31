# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from openerp import api
import pytz
from datetime import datetime, timedelta
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
import amount_to_text_es_MX
from odoo.tools import amount_to_text_en


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.depends('amount_total')
    def compute_written_amount(self):
        #print 'CONTEXT: ',self._context
        #print 'compute_written_amount'
        #print 'self.amount_total: ',self.amount_total
        #print 'self.currency_id.name: ',self.currency_id.name
        lang = self._context.get('lang',False)
        
        if lang == 'en_US':
            #EN (en_US)
            self.amount_to_text = amount_to_text_en.amount_to_text(self.amount_total, 'en', self.currency_id.name)
            
        else:
            #ES_MX (es_MX)
            self.amount_to_text = amount_to_text_es_MX.get_amount_to_text(self,self.amount_total, self.currency_id.name)

    amount_to_text = fields.Char('Written Amount', compute='compute_written_amount')