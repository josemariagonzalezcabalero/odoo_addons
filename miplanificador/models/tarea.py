from odoo import fields, models, api


class Tarea(models.Model):
    _name = 'miplanificador.tarea'
    _description = 'Tareas'

    name = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="Descripción", required=True)
    precio_hora = fields.Float(string="Precio hora", required=True)
    fecha_inicio = fields.Date(string="Fecha de inicio")
    fecha_fin = fields.Date(string="Fecha de fin")
    estado = fields.Selection([('0', 'No iniciada'), ('1', 'Iniciada'), ('2', 'Aparcada'), ('3', 'Finalizada')])
