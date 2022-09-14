from odoo import fields, models


class PartnerXlsx(models.AbstractModel):
    _name = 'report.hospital.report_prescription_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    report_date = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, prescription):
        sheet = workbook.add_worksheet('Daftar Penjualan')
        bold = workbook.add_format({'bold': True})
        row = 2
        col = 0

        sheet.write(0, 0, str(self.report_date))
        sheet.write(1, 0, 'Patient Name')
        sheet.write(1, 1, 'Pharmacy')
        sheet.write(1, 2, 'Total')
        sheet.write(1, 3, 'Medicament')
        # sheet.write(1, 3, 'Medicament List')

        for obj in prescription:
            col = 0
            patient = str(obj.name.name)
            sheet.write(row, col, patient, bold)
            sheet.write(row, col+1, obj.prescription_pharmacy, bold)
            sheet.write(row, col+2, obj.prescription_total, bold)
            # sheet.write(row, col+3, obj.prescription_total, bold)
            
            for xxx in obj.presc_ids.medicament_id:
                sheet.write(row, col+3, xxx.name, bold)
                col += 1

            row += 1