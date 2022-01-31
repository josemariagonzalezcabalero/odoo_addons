# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Persona(models.Model):
    _name = 'mimodulo.persona'
    _description = 'Descripción del modelo persona'


    name = fields.Char(string="Nombre", required=True, help="El nombre de la persona.")
    apellidos = fields.Char(string="Apellidos", required=True, help="Escribe los apellidos.")
    fecha_nacimiento= fields.Date(string="Fecha de nacimiento")
    observaciones = fields.Text(string="Observaciones")

#    @api.depends('value')
#    def _value_pc(self):
#        for record in self:
#            record.value2 = float(record.value) / 100
