from odoo import fields, models, api


class Trabajo(models.Model):
    _name = 'miplanificador.trabajo'
    _description = 'Trabajos'

    name = fields.Char(string="Trabajo realizado", required=True)
    horas = fields.Float(string="Horas dedicadas", required=True)

    # Relaciones
    tarea_id = fields.Many2one(string="Tarea", comodel_name="miplanificador.tarea")


