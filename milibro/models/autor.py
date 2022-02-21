from odoo import fields, models, api


class Autor(models.Model):
    _name = 'milibro.autor'
    _description = 'Pequeña descripcion del autor'

    nombre = fields.Char(string="Nombre", required=True, help="Nombre del autor.")
    apellidos = fields.Char(string="Apellidos", required=True, help="Apellidos del autor.")

    cantidad_libros_escritos = fields.Integer(string="Cantidad de libros escritos", compute="_cantidad_libros", store=True)
    name = fields.Char(string="Nombre comleto", compute="_nombre_completo")

    # Relaciones
    libro_ids = fields.One2many(comodel_name="milibro.libro", inverse_name="autor_id")

    # Métodos
    @api.depends("libro_ids")
    def _cantidad_libros(self):
        for libro in self:
            libro.cantidad_libros_escritos =  len(libro.libro_ids)

    @api.depends("nombre","apellidos")
    def _nombre_completo(self):
        for autor in self:
            autor.name = f'{autor.apellidos}, {autor.nombre}'

