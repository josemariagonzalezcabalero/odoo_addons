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

    # Campos calculados
    total_horas = fields.Float(string="Total horas", compute="_calcular_total_horas")
    total_coste = fields.Float(string="Total coste", compute="_calcular_total_coste")

    # Relaciones
    proyecto_id = fields.Many2one(string="Proyecto", comodel_name="miplanificador.proyecto")
    trabajo_ids = fields.One2many(string="Trabajos", comodel_name="miplanificador.trabajo", inverse_name="tarea_id")
    categoria_ids = fields.Many2many(string="Categorias", comodel_name="miplanificador.categoria")

    _sql_constraints = [
        ('check_precio_hora', 'CHECK(precio_hora >= 0)',
         'El precio/hora de la tarea no puede ser inferior a cero'),
        ('check_fechas', 'CHECK(fecha_inicio <= fecha_fin)',
         'La fecha de inicio de la tarea no puede ser superior a la fecha de fin')
    ]

    # Funciones

    @api.depends("trabajo_ids")
    def _calcular_total_horas(self):
        for tarea in self:
            horas = 0
            for trabajo in self.trabajo_ids:
                horas += trabajo.horas
            tarea.total_horas = horas

    @api.onchange("fecha_inicio", "fecha_fin")
    def _comprobar_fechas(self):
        res = {}
        if self.fecha_inicio and self.fecha_fin:
            if self.fecha_inicio > self.fecha_fin:
                self.fecha_fin = self.fecha_inicio
                res['warning'] = {'title': 'Advertencia',
                                  'message': 'La fecha de inicio de la tarea no puede ser superior a la fecha de fin'
                                  }
        return res

    @api.onchange("precio_hora")
    def _comprobar_precio_hora(self):
        res = {}
        if self.precio_hora and self.precio_hora < 0:
            self.precio_hora = 0
            res['warning'] = {'title': 'Advertencia',
                              'message': 'El precio/hora de la tarea no puede ser inferior a cero'
                              }
        return res

    @api.depends("total_horas","precio_hora")
    def _calcular_total_coste(self):
        for tarea in self:
            if tarea.total_horas != 0 and tarea.precio_hora != 0:
                tarea.total_coste = tarea.total_horas * tarea.precio_hora
            else:
                tarea.total_coste = 0