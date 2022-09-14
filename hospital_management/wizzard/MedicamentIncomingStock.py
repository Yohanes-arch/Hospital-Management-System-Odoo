from odoo import api, fields, models


class IncomingStock(models.TransientModel):
    _name = 'hospital.incomingstock'
    _description = 'New Description'

    medicament_id = fields.Many2one(comodel_name='hospital.medicament', string='Medicament', required=True)
    qty = fields.Integer(string='Quantity', required=False)

    def button_incomingstock(self):
        for rec in self:
            self.env['hospital.medicament'].search([('id', '=', rec.medicament_id.id)]).write({'medicament_stock': rec.medicament_id.medicament_stock + rec.qty})
    
    
