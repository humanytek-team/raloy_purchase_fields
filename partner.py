# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from openerp import api
import pytz
from datetime import datetime, timedelta
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT

class ResPartner(models.Model):
    _inherit = 'res.partner'



    # @api.one
    # @api.depends('amount_total','currency_id')
    # def _get_amount_to_text(self):
    #     self.amount_to_text = amount_to_text_es_MX.get_amount_to_text(self, self.amount_total, self.currency_id.name)

    # @api.depends('amount_total')
    # def compute_written_amount(self):
    #     print 'compute_written_amount'
    #     self.amount_to_text = amount_to_text_es_MX.get_amount_to_text(self.amount_total, self.currency_id.name)



    banking_instructions = fields.Text('Banking Instructions')
    shipping_instructions = fields.Text('Shipping Instructions')
    # border_custom_service = fields.Text('Border Custom Service')
    # mexican_customs = fields.Text('Mexican Customs')
    # contact_details = fields.Text('Contact Details')

    #amount_to_text = fields.Char('Written Amount', compute='compute_written_amount')