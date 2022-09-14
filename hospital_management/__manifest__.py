# -*- coding: utf-8 -*-
{
    'name': "HospitalManagement",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/hospital_patient.xml',
        'views/hospital_prescription.xml',
        'views/hospital_appointment.xml',
        'views/hospital_employee.xml',
        'views/hospital_doctor.xml',
        'views/hospital_medicament.xml',
        'report/report.xml',
        'report/hospital_invoice.xml',
        'report/hospital_prescription.xml',
        'report/hospital_patient_pdf.xml',
        'report/prescriptionreport_invoice.xml',
        'wizzard/incomingstock_wizzard.xml',
        'wizzard/prescriptionreport_wizzard.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
