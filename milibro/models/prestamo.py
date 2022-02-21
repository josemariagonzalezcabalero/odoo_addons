from datetime import datetime

from odoo import fields, models, api


class Prestamo(models.Model):
    _name = 'milibro.prestamo'
    _description = 'Pequeña descripcion del préstamo'

    name = fields.Char(string="Num. Préstamo", compute="_calcular_num_prestamo")
    fecha_ini_prestamo = fields.Date(string="Fecha de préstamo", required=True, default=datetime.now())
    fecha_devolucion = fields.Date(string="Fecha de devolución")
    fecha_fin_prestamo = fields.Date(string="Fecha fin préstamo", stored=True, compute="_calcular_fecha_fin_prestamo")
    estado = fields.Selection([('1', 'Creando'), ('2', 'Prestado'), ('3', 'Devuelto')], required=True, default='1')

    # Relaciones
    libro_id = fields.Many2one(comodel_name="milibro.libro", string="Libro")
    autor_id = fields.Many2one(comodel_name="milibro.autor", string="Autor")
    ejemplar_id = fields.Many2one(comodel_name="milibro.ejemplar", string="Ejemplar", required=True)
    usuario_id = fields.Many2one(comodel_name="res.partner", string="Usuario")

    @api.depends("create_date")
    def _calcular_num_prestamo(self):
        for prestamo in self:
            prestamo.name = str(prestamo.create_date) \
                .replace(":", "") \
                .replace("/", "") \
                .replace(".", "") \
                .replace(" ", "") \
                .replace("-", "")

    @api.depends("fecha_ini_prestamo")
    def _calcular_fecha_fin_prestamo(self):
        for prestamo in self:
            fecha = prestamo.fecha_ini_prestamo + (datetime.day * 15)
            datetime.timedelta(1)
            fechaF = fecha + datetime.timedelta(days=15)
            if datetime.isoweekday(fechaF) == 6: #Sabado
                fechaF = fecha + datetime.timedelta(days=16)
            elif datetime.isoweekday(fechaF) == 7: #Domingo
                fechaF = fecha + datetime.timedelta(days=17)
            prestamo.fecha_fin_prestamo = fechaF
