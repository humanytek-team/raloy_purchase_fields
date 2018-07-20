# -*- coding: utf-8 -*-

from odoo import api, fields, models
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
                if found is False:  # SI NO ENCUENTRA ALGUNO CON LA ETIQUETA, SE UTILIZA EL PRIMERO QUE ENCUENTRA
                    rec.default_contact = rec.partner_id.child_ids[0].name
            else:
                rec.default_contact = rec.partner_id.name

    @api.multi
    @api.depends('amount_total')
    def compute_written_amount(self):
        for rec in self:
            lang = rec._context.get('lang', False)
            if lang == 'en_US':
                rec.amount_to_text = amount_to_text_en.amount_to_text(rec.amount_total, 'en', rec.currency_id.name)
            else:
                rec.amount_to_text = amount_to_text_es_MX.get_amount_to_text(rec, rec.amount_total, rec.currency_id.name)

    amount_to_text = fields.Char('Written Amount', compute='compute_written_amount')
    default_contact = fields.Char('Default Contact', compute='get_contact')
