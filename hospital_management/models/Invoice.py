from unicodedata import name
from odoo import api, fields, models


class Invoice(models.Model):
    _name = 'hospital.invoice'
    _description = 'New Description'

    name = fields.Many2one(comodel_name='hospital.patient', string='Customer')
    prescription_invoice_ids = fields.One2many(comodel_name='hospital.prescription_detail', inverse_name='invoice_id', string='Detail')
    

    # @api.onchange('name')
    # def _onchange_(self):
    #     for rec in self:
    #         a = self.env['hospital.prescription_detail'].search([('prescription_invoice_ids', '=', rec.name)])
    #         print(a)
