# -*- coding: utf-8 -*-

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    banking_instructions = fields.Text('Banking Instructions')
    shipping_instructions = fields.Text('Shipping Instructions')
