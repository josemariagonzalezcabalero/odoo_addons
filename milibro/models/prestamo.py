from datetime import datetime, timedelta

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Prestamo(models.Model):
    _name = 'milibro.prestamo'
    _description = 'Pequeña descripcion del préstamo'

    name = fields.Char(string="Num. Préstamo", compute="_calcular_num_prestamo")
    fecha_ini_prestamo = fields.Date(string="Fecha de préstamo", required=True, default=datetime.now())
    fecha_devolucion = fields.Date(string="Fecha de devolución")
    fecha_fin_prestamo = fields.Date(string="Fecha fin préstamo", stored=True, compute="_calcular_fecha_fin_prestamo")
    estado = fields.Selection([('1', 'Creando'), ('2', 'Prestado'), ('3', 'Devuelto')], required=True, default='1')

    @api.model
    def create(self, data_list):
        res = super(Prestamo, self).create(data_list)
        res.estado = '2'
        res.ejemplar_id.situacion = False
        res.autor_id = res.ejemplar_id.libro_id.autor_id
        res.libro_id = res.ejemplar_id.libro_id
        return res

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

    @api.constrains("fecha_ini_prestamo")
    def _comprobar_fecha_ini(self):
        if self.fecha_ini_prestamo > fields.Date.today():
            raise ValidationError("La fecha de inicio no puede ser superior a la fecha actual")

    @api.depends("fecha_ini_prestamo")
    def _calcular_fecha_fin_prestamo(self):
        for prestamo in self:
            fecha_sumada = prestamo.fecha_ini_prestamo + timedelta(days=15)
            if datetime.isoweekday(fecha_sumada) == 6:  # Sabado
                prestamo.fecha_fin_prestamo = prestamo.fecha_ini_prestamo + timedelta(days=17)
            elif datetime.isoweekday(fecha_sumada) == 7:  # Domingo
                prestamo.fecha_fin_prestamo = prestamo.fecha_ini_prestamo + timedelta(days=16)
            else:
                prestamo.fecha_fin_prestamo = fecha_sumada

    @api.onchange("fecha_ini_prestamo")
    def _comprobar_fecha_ini_prestamo(self):
        res = {}
        if self.fecha_ini_prestamo and self.fecha_ini_prestamo > fields.date.today():
            res['warning'] = {'title': 'Advertencia',
                              'message': 'La fecha de inicio tiene que ser inferior o igual a la actual'
                              }
        return res

    @api.onchange("autor_id")
    def _cambio_autor(self):
        for prestamo in self:
            if prestamo.libro_id:
                if prestamo.autor_id.libro_ids != prestamo.libro_id:
                    prestamo.libro_id = False

    @api.onchange("libro_id")
    def _cambio_libro(self):
        for prestamo in self:
            if prestamo.ejemplar_id:
                if prestamo.libro_id.ejemplar_id != prestamo.ejemplar_id:
                    prestamo.ejemplar_id = False

    def devolver_prestamo(self):
        self.estado = '3'
        self.fecha_devolucion = fields.datetime.now()
        self.ejemplar_id.situacion = True

    def ampliar_fecha_devolucion(self):
        if self.fecha_fin_prestamo:
            fecha_sumada = self.fecha_fin_prestamo + timedelta(days=15)
            if datetime.isoweekday(fecha_sumada) == 6:  # sabado
                self.fecha_fin_prestamo = self.fecha_fin_prestamo + timedelta(days=17)
            elif datetime.isoweekday(fecha_sumada) == 7:  # domingo
                self.fecha_fin_prestamo = self.fecha_fin_prestamo + timedelta(days=16)
            else:
                self.fecha_fin_prestamo = fecha_sumada
