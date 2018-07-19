# -*- coding: utf-8 -*-
from odoo import http

# class WarehouseFilter(http.Controller):
#     @http.route('/warehouse_filter/warehouse_filter/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/warehouse_filter/warehouse_filter/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('warehouse_filter.listing', {
#             'root': '/warehouse_filter/warehouse_filter',
#             'objects': http.request.env['warehouse_filter.warehouse_filter'].search([]),
#         })

#     @http.route('/warehouse_filter/warehouse_filter/objects/<model("warehouse_filter.warehouse_filter"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('warehouse_filter.object', {
#             'object': obj
#         })