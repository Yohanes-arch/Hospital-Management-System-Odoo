from email.policy import default
from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from datetime import datetime



class Prescription(models.Model):
    _name = 'hospital.prescription'
    _description = 'New Description'

    # name = fields.Char(string='Patient')
    name = fields.Many2one(comodel_name='hospital.patient', string='Patient')
    
    id_member = fields.Char(compute="compute_id", string='ID Patient', required=False)
    

    prescription_date = fields.Datetime(string='Prescription Date')
    prescription_pharmacy = fields.Char(string='Pharmacy')
    presc_ids = fields.One2many(comodel_name='hospital.prescription_detail', inverse_name='prescription_id', string='Prescription Detail')
    
    prescription_total = fields.Integer(compute='_compute_prescription_total', string='Prescription Total')
    state = fields.Selection(
    string='Status',
    selection=[('draft', 'Draft'), 
                ('confirm', 'Confirm'),
                ('done', 'Done'),
                ('cancelled', 'Cancelled'),
                ],
    required=True,
    readonly=True,
    default='draft'
    )
    @api.depends('prescription_total')
    def _compute_prescription_total(self):
        for rec in self:
            a = sum(self.env['hospital.prescription_detail'].search([('prescription_id', '=', rec.id)]).mapped('presc_total'))
            rec.prescription_total = a

    # @api.ondelete(at_uninstall=False)
    # def __ondelete_penjualan(self):
    #     if self.presc_ids:
    #         a=[]
    #         for rec in self: 
    #             a = self.env['hospital.prescription_detail'].search([('prescription_id', '=', rec.id)])
    #             print(a)
    #         for obj in a:
    #             print(str(obj.medicament_id.name) + ' ' + str(obj.presc_qty))
    #             obj.medicament_id.medicament_stock += obj.presc_qty

    @api.model
    def default_get(self, fields):
        res = super(Prescription, self).default_get(fields)
        res.update({'prescription_date': datetime.now()})
        return res


    def unlink(self):
        for rec in self:
            if self.filtered(lambda line: line.state != 'draft'):
                raise ValidationError("Cannot delete because the item is not on 'draft' state")

            if rec.presc_ids:
                for data in rec.presc_ids:
                    data.medicament_id.medicament_stock = data.medicament_id.medicament_stock + data.presc_qty
        

        record = super(Prescription,self).unlink()
        return record
        # return super(Prescription, self).unlink()

        

    def write(self, vals):
        for rec in self:
            a = self.env['hospital.prescription_detail'].search([('prescription_id', '=', rec.id)])
            print(a)
            for data in a:
                print(str(data.medicament_id.name)+' '+str(data.presc_qty)+' '+str(data.medicament_id.medicament_stock))
                data.medicament_id.medicament_stock += data.presc_qty
        record =  super(Prescription, self).write(vals)
        
        for rec in self:
            b = self.env['hospital.prescription_detail'].search([('prescription_id', '=', rec.id)])
            print(b)
            for newdata in b:
                if newdata in a:
                    print(str(newdata.medicament_id.name)+' '+str(newdata.presc_qty)+' '+str(newdata.medicament_id.medicament_stock))
                    newdata.medicament_id.medicament_stock -= newdata.presc_qty
                else:
                    pass
        return record

    def action_confirm(self):
        self.write({'state': 'confirm'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})

    def action_draft(self):
        self.write({'state': 'draft'})


    @api.depends('name')
    def compute_id(self):
        for rec in self:
            rec.id_member = rec.name.name




class PrescriptionDetail(models.Model):
    _name = 'hospital.prescription_detail'
    _description = 'New Description'

    medicament_id = fields.Many2one(comodel_name='hospital.medicament', string='Medicament')
    presc_dose = fields.Char(string='Dose')
    presc_doseUnit = fields.Selection([
        ('Milligram', 'Milligram'),
        ('Gram', 'Gram')
    ], string='Dose Unit')
    presc_form = fields.Selection([
        ('Pills', 'Pills'),
        ('Syrup', 'Syrup'),
        ('Tablets', 'Tablets'),
    ], string='Form')
    presc_frequency = fields.Selection([
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
        ('Afternoon', 'Afternoon')
    ], string='Frequency')
    presc_treatmentDuration = fields.Integer(string='Treatment Duration')
    presc_treatmentPeriod = fields.Selection([
        ('Days', 'Days'),
        ('Months', 'Months'),
        ('Years', 'Years')
    ], string='Treatment Period')

    presc_qty = fields.Integer(string='Quantity', default='1')
    
    med_price = fields.Integer(string='Price')
    presc_total = fields.Integer(compute='_compute_field_name', string='Total')
    
    
    prescription_id = fields.Many2one('hospital.prescription', string='Prescription Detail')
    invoice_id = fields.Many2one('hospital.invoice', string='invoice')

    

    
    
    #to perform finding the price
    @api.onchange('medicament_id')
    def _onchange_(self):
        if(self.medicament_id.medicament_price):
            self.med_price = self.medicament_id.medicament_price

    # to perform finding total price
    @api.depends('med_price', 'presc_qty')
    def _compute_field_name(self):
            for rec in self:
                rec.presc_total = rec.presc_qty * rec.med_price
    
    # to perform subtraction whenever the stock is taken
    @api.model
    def create(self, vals):
        record = super(PrescriptionDetail, self).create(vals)
        if (record.presc_qty):
            self.env['hospital.medicament'].search([('id','=',record.medicament_id.id)]).write({'medicament_stock' : record.medicament_id.medicament_stock - record.presc_qty})
        return record