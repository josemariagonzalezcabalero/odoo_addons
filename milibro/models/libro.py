# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Libro(models.Model):
     _name = 'milibro.libro'
     _description = 'Pequeña descripción de mi libro'

     nombre = fields.Char(string="Titulo", required=True, help="El nombre del libro.")
     descripcion = fields.Text(string="Descripción", required=True, help="Descripción del libro.")
     isbn = fields.Char(string="ISBN", help="Identificador único del libro.")

     num_paginas = fields.Integer(string="Número de páginas", compute="_validar_num_paginas")

     tejuelo = fields.Char(string="Tejuelo", compute="_calcular_tejuelo")

     _sql_constraints = [
          ('isbn','unique(isbn)','El ISBN debe ser único')
     ]

     # Relaciones
     autor_id = fields.Many2one(comodel_name="milibro.autor", string="Autor", required=True)
     editorial_id = fields.Many2one(comodel_name="milibro.editorial", string="Editorial", required=True)
     categoria_ids = fields.Many2many(comodel_name="milibro.categoria", string="Categorias")

     cdu = fields.Many2one(comodel_name="milibro.cdu", string="CDU")

     # Métodos
     @api.onchange("num_paginas")
     def _validar_num_paginas_onchange(self):
          res = {}
          if self.num_paginas < 0:
               res['warning'] = {'title': ('Advertencia'),
                                 'message': ('El número de páginas no puede ser negativo (onchange)')
                                 }
          return res

     @api.constrains("num_paginas")
     def _validar_num_paginas(self):
          if self.num_paginas < 0:
               raise ValidationError("El número de páginas no puede ser negativo (constrains)")

     @api.onchange("nombre","autor_id","cdu")