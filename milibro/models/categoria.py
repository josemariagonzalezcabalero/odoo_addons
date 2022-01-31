from odoo import fields, models, api


class Categoria(models.Model):
    _name = 'milibro.categoria'
    _description = 'Pequeña descripción de categoría'

    name = fields.Char(string="Nombre", required=True, help="Nombre de la categoría")

    #Relaciones

