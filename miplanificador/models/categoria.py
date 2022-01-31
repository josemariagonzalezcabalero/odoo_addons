# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Categoria(models.Model):
     _name = 'miplanificador.categoria'
     _description = 'Categorías'

     name = fields.Char(string="Nombre", required=True)

     # Relaciones


     # Métodos
     # @api.onchange("num_paginas")
     # def _validar_num_paginas_onchange(self):
     #      res = {}
     #      if self.num_paginas < 0:
     #           res['warning'] = {'title': ('Advertencia'),
     #                             'message': ('El número de páginas no puede ser negativo (onchange)')
     #                             }
     #      return res
     #
     # @api.constrains("num_paginas")
     # def _validar_num_paginas(self):
     #      if self.num_paginas < 0:
     #           raise ValidationError("El número de páginas no puede ser negativo (constrains)")
     #
     # @api.depends("name","autor_id","cdu_id")
     # def _calcular_tejuelo(self):
     #      for libro in self:
     #           if libro.name and libro.cdu_id and libro.autor_id:
     #                libro.tejuelo = f'{libro.cdu_id.name}-{libro.name[0:3].upper()}-{libro.autor_id.name[0:3].lower()}'
     #           else:
     #                libro.tejuelo = ""