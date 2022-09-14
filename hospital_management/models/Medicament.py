from unicodedata import name
from odoo import api, fields, models


class Medicament(models.Model):
    _name = 'hospital.medicament'
    _description = 'New Description'

    name = fields.Char(string='Medicament')
    medicament_price = fields.Integer(string='Price')
    medicament_stock = fields.Integer(string='')
    prescription_id = fields.Many2one('hospital.prescription', string='Prescription Detail')

    currency_id = fields.Many2one('res.currency', string='Account Currency',
        help="Forces all moves for this account to have this account currency.", required=True)
    

    
    
