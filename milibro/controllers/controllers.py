# -*- coding: utf-8 -*-
# from odoo import http


# class Milibro(http.Controller):
#     @http.route('/milibro/milibro/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/milibro/milibro/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('milibro.listing', {
#             'root': '/milibro/milibro',
#             'objects': http.request.env['milibro.milibro'].search([]),
#         })

#     @http.route('/milibro/milibro/objects/<model("milibro.milibro"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('milibro.object', {
#             'object': obj
#         })
