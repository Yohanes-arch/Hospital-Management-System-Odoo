from odoo import fields, models, api

class ModelName(models.TransientModel):
    _name = 'hospital.prescriptionreport'
    _description = 'ModelName'

    prescription_id = fields.Many2one(comodel_name='hospital.prescription', string='Patient', required=False)


    def prescription_report(self):
        filter = []
        prescription_id = self.prescription_id
        if prescription_id:
            filter += [('name', '=', prescription_id.id_member)]
        sale = self.env['hospital.prescription'].search_read(filter)
        print(sale)
        data = {
            'form': self.read()[0],
            'sale': sale
        }

        return self.env.ref('hospital_management.invoice_prescriptionreport_wizzard_pdf').report_action(self, data = data)  
        
