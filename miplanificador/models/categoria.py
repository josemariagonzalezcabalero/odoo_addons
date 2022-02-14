# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Categoria(models.Model):
     _name = 'miplanificador.categoria'
     _description = 'Categorías'

     name = fields.Char(string="Nombre", required=True)