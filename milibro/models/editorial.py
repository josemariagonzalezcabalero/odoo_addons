from odoo import fields, models, api


class Editorial(models.Model):
    _name = 'milibro.editorial'
    _description = 'Pequeña descripcion de la editorial'

    nombre = fields.Char(string="Nombre", required=True, help="Nombre de la editorial.")
    direccion = fields.Char(string="Dirección", help="Direccion de la editorial.")
    poblacion = fields.Char(string="Población", help="Poblacioón de la editorial.")

    cantidad_libros = fields.Integer(string="Cantidad de libros", compute="_num_libros", store=True)

    # Relaciones
    libro_ids = fields.One2many(comodel_name="milibro.libro", inverse_name="editorial_id")

    # Métodos

    @api.depends("libro_ids")
    def _num_libros(self):
        for libro in self:
             libro.cantidad_libros = len(libro.libro_ids)

