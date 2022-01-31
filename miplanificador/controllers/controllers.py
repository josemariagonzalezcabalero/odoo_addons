# -*- coding: utf-8 -*-
# from odoo import http


# class Miplanificador(http.Controller):
#     @http.route('/miplanificador/miplanificador/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/miplanificador/miplanificador/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('miplanificador.listing', {
#             'root': '/miplanificador/miplanificador',
#             'objects': http.request.env['miplanificador.miplanificador'].search([]),
#         })

#     @http.route('/miplanificador/miplanificador/objects/<model("miplanificador.miplanificador"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('miplanificador.object', {
#             'object': obj
#         })
