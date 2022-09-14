# -*- coding: utf-8 -*-
# from odoo import http


# class HospitalManagement(http.Controller):
#     @http.route('/hospital_management/hospital_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospital_management/hospital_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital_management.listing', {
#             'root': '/hospital_management/hospital_management',
#             'objects': http.request.env['hospital_management.hospital_management'].search([]),
#         })

#     @http.route('/hospital_management/hospital_management/objects/<model("hospital_management.hospital_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital_management.object', {
#             'object': obj
#         })
