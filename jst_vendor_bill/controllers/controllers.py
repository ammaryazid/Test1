# -*- coding: utf-8 -*-
# from odoo import http


# class JstVendorBill(http.Controller):
#     @http.route('/jst_vendor_bill/jst_vendor_bill', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/jst_vendor_bill/jst_vendor_bill/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('jst_vendor_bill.listing', {
#             'root': '/jst_vendor_bill/jst_vendor_bill',
#             'objects': http.request.env['jst_vendor_bill.jst_vendor_bill'].search([]),
#         })

#     @http.route('/jst_vendor_bill/jst_vendor_bill/objects/<model("jst_vendor_bill.jst_vendor_bill"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('jst_vendor_bill.object', {
#             'object': obj
#         })

