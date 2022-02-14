# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Libro(models.Model):
     _name = 'milibro.libro'
     _description = 'Pequeña descripción de mi libro'

     name = fields.Char(string="Titulo", required=True, help="El nombre del libro.")
     descripcion = fields.Text(string="Descripción", required=True, help="Descripción del libro.")
     isbn = fields.Char(string="ISBN", help="Identificador único del libro.")

     num_paginas = fields.Integer(string="Número de páginas", compute="_validar_num_paginas")

     tejuelo = fields.Char(string="Tejuelo", compute="_calcular_tejuelo")

     imagen = fields.Image(string="Imagen", max_width=425, max_height=640, store=True)

     numejemplares = fields.Integer(string="Nº de ejemplares", compute="_calcular_ejemplares")
     numejemplares_disponibles = fields.Integer(string="Nº disponibles", compute="_calcular_ejemplares")

     _sql_constraints = [
          ('isbn','unique(isbn)','El ISBN debe ser único')
     ]

     # Relaciones
     autor_id = fields.Many2one(comodel_name="milibro.autor", string="Autor", required=True)
     editorial_id = fields.Many2one(comodel_name="milibro.editorial", string="Editorial", required=True)
     categoria_ids = fields.Many2many(comodel_name="milibro.categoria", string="Categorias")
     cdu_id = fields.Many2one(comodel_name="milibro.cdu", string="CDU")
     ejemplar_id = fields.One2many(comodel_name="milibro.ejemplar", inverse_name="libro_id")


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

     @api.depends("name","autor_id","cdu_id")
     def _calcular_tejuelo(self):
          for libro in self:
               if libro.name and libro.cdu_id and libro.autor_id:
                    libro.tejuelo = f'{libro.cdu_id.name}-{libro.name[0:3].upper()}-{libro.autor_id.name[0:3].lower()}'
               else:
                    libro.tejuelo = ""

     @api.depends("ejemplar_id")
     def _calcular_ejemplares(self):
          n_ejemplares = 0
          n_disponibles = 0
          for ejemplar in self:
               n_ejemplares += 1
               if ejemplar.situacion:
                    n_disponibles += 1

          self.numejemplares = n_ejemplares
          self.numejemplares_disponibles = n_disponibles