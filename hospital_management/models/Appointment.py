from unicodedata import name
from odoo import api, fields, models


class Appointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'New Description'

    name = fields.Char(string='Appointment Type')
    appoint_patient = fields.Many2one(comodel_name='hospital.patient', string='Patient Name')
    appoint_duration = fields.Float(string='Appointment Duration')
    appoint_date = fields.Datetime(string='Appintment Date')

    employee_id = fields.Many2one('res.partner', string='Doctor')
    
    
    
    
