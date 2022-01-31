from odoo import fields, models, api


class Proyecto(models.Model):
    _name = 'miplanificador.proyecto'
    _description = 'Proyectos'

    name = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="Descripción")
    fecha_inicio_estimada = fields.Date(string="Fecha de inicio estimada")
    fecha_fin_estimada = fields.Date(string="Fecha de fin estimada")
    fecha_inicio_real = fields.Date(string="Fecha de inicio real")
    fecha_fin_real = fields.Date(string="Fecha de fin real")
