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

    @api.multi
    def get_contact(self):
        for rec in self:
            found = False
            if rec.partner_id and rec.partner_id.child_ids:
                for child in rec.partner_id.child_ids:
                    if child.category_id:
                        for tag in child.category_id:
                            if tag.name == 'Ejecutivo de cuenta':
                                found = True
                                rec.default_contact = child.name
                if found == False: #SI NO ENCUENTRA ALGUNO CON LA ETIQUETA, SE UTILIZA EL PRIMERO QUE ENCUENTRA
                    rec.default_contact = rec.partner_id.child_ids[0].name
            else:
                rec.default_contact = rec.partner_id.name



    @api.multi
    @api.depends('amount_total')
    def compute_written_amount(self):
        #print 'CONTEXT: ',self._context
        #print 'compute_written_amount'
        #print 'self.amount_total: ',self.amount_total
        #print 'self.currency_id.name: ',self.currency_id.name
        for rec in self:
            lang = rec._context.get('lang',False)
            
            if lang == 'en_US':
                #EN (en_US)
                rec.amount_to_text = amount_to_text_en.amount_to_text(rec.amount_total, 'en', rec.currency_id.name)
                
            else:
                #ES_MX (es_MX)
                rec.amount_to_text = amount_to_text_es_MX.get_amount_to_text(rec,rec.amount_total, rec.currency_id.name)

    amount_to_text = fields.Char('Written Amount', compute='compute_written_amount')
    default_contact = fields.Char('Default Contact', compute='get_contact')