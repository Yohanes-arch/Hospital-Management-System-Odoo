from odoo import models, api, fields


class Employee(models.Model):
    _inherit = 'res.partner'

    is_doctor = fields.Boolean(string='Is doctor')

    employee_role = fields.Selection([
        ('Manager', 'Manager'),
        ('Doctor', 'Doctor'),
        ('Nurse', 'Nurse'),
        ('Front Office', 'Front Office'),
        ('IT Support', 'IT Support')
    ], string='Job Role')
    

    
    @api.onchange('employee_role')
    def bool_doctor(self):
        for rec in self:
            if (rec.employee_role):
                if rec.employee_role == 'Doctor':
                    rec.is_doctor = True
                else:
                    rec.is_doctor = False

        # if self.employee_role == 'Doctor':
        #     self.bool_doctor = True

    
