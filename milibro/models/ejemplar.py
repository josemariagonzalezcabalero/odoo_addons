from odoo import fields, models, api


class Ejemplar(models.Model):
    _name = 'milibro.ejemplar'
    _description = 'Pequeña descripcion del ejemplar'

    name = fields.Char(string="Código", compute="_calcular_codigo")

    situacion = fields.Boolean(string="Disponible", default=True)

    estado = fields.Selection([('1', 'Bueno'), ('2', 'Regular'), ('3', 'Malo')], string="Estado de conservación",
                              required=True, default='1')

    # Relaciones
    libro_id = fields.Many2one(comodel_name="milibro.libro", string="Libro")

    # Métodos
    @api.depends("create_date")
    def _calcular_codigo(self):
        for ejemplar in self:
            ejemplar.name = ejemplar.id
            ejemplar.name = ejemplar.name.zfill(13)


