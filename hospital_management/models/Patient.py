from odoo import api, fields, models
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError


class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'New Description'

    name = fields.Char(string='Patient')
    patient_ID = fields.Char(string='Patient ID', required=False)
    patient_DoB = fields.Date(string='Date of Birth')
    patient_maritalStatus = fields.Selection([
        ('Not married', 'Not married'),
        ('Married', 'Married'),
        ('Divorce', 'Divorce'),
    ], string='Marital Status')
    patient_sex = fields.Selection([
        ('Male', 'Male'),
        ('Female', 'Female')
    ], string='Sex')
    patient_age = fields.Char(string='Patient Age')
    patient_address = fields.Char(string='Address')


    #critical information
    patient_bloodType = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O')
    ], string='Blood Type')
    patient_Rh = fields.Selection([
        ('Positive', '+'),
        ('Negative', '-')
    ], string='Patient Rh')
    patient_insurance = fields.Char(string='Insurance')
    patient_disease = fields.Char(string='Disease')

    
    @api.constrains('name', 'patient_ID', 'patient_DoB', 'patient_sex', 'patient_maritalStatus', 'patient_address', 'patient_bloodType', 'patient_disease')
    def check_form(self):
        for rec in self:
            if rec.name == 0:
                raise ValidationError("Please complete the form")
            if rec.patient_ID == 0:
                raise ValidationError("Please complete the form")
            if rec.patient_DoB == 0:
                raise ValidationError("Please complete the form")
            if rec.patient_sex == 0:
                raise ValidationError("Please complete the form")
            if rec.patient_maritalStatus == 0:
                raise ValidationError("Please complete the form")
            if rec.patient_address == 0:
                raise ValidationError("Please complete the form")
            if rec.patient_bloodType == 0:
                raise ValidationError("Please complete the form")
            if rec.patient_disease == 0:
                raise ValidationError("Please complete the form")    
            

    
    

    
    # @api.depends('patient_DoB')
    # def _compute_patient_age(self):
    #     years = relativedelta(date.today(), self.patient_DoB).years
    #     months = relativedelta(date.today(), self.patient_DoB).months
    #     day = relativedelta(date.today(), self.patient_DoB).days

    #     self.patient_age = str(int(years)) + ' Year/s ' + str(int(months)) + ' Month/s ' + str(day) + ' Day/s'

