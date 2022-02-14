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

    # Campos calculados
    total_horas = fields.Float(string="Total horas", compute="_calcular_total_horas")
    total_coste = fields.Float(string="Total coste", compute="_calcular_total_coste")

    # Relaciones
    tareas_ids = fields.One2many(string="Tareas", comodel_name="miplanificador.tarea", inverse_name="proyecto_id")

    _sql_constraints = [
        ('nombre_unico', 'unique(name))',
         'El nombre del proyecto debe ser único'),
        ('check_fechas_estimadas', 'CHECK(fecha_inicio_estimada > fecha_fin_estimada',
         'La fecha de inicio estimada de la tarea no puede ser superior a la fecha de fin'),
        ('check_fechas_reales', 'CHECK(fecha_inicio_real > fecha_fin_real',
         'La fecha de inicio real de la tarea no puede ser superior a la fecha de fin')
    ]

    # Funciones
    @api.depends("tareas_ids.trabajo_ids")
    def _calcular_total_horas(self):
        for proyecto in self:
            horas = 0
            for tarea in proyecto.tareas_ids:
                horas += tarea.total_horas
            proyecto.total_horas = horas

    @api.depends("tareas_ids")
    def _calcular_total_coste(self):
        for proyecto in self:
            horas = 0
            precio = 0
            for tarea in proyecto.tareas_ids:
                horas += tarea.total_horas
                precio = tarea.precio_hora
            proyecto.total_coste = horas * precio

    @api.onchange("fecha_inicio_estimada", "fecha_fin_estimada")
    def _comprobar_fechas_estimadas(self):
        res = {}
        if self.fecha_inicio_estimada and self.fecha_fin_estimada:
            if self.fecha_inicio_estimada > self.fecha_fin_estimada:
                self.fecha_fin_estimada = False
                res['warning'] = {'title': ('Advertencia'),
                                  'message': (
                                      'La fecha de inicio estimada del proyecto no puede ser superior a la fecha de fin')
                                  }
        return res

    @api.onchange("fecha_inicio_real", "fecha_fin_real")
    def _comprobar_fechas_reals(self):
        res = {}
        if self.fecha_inicio_real and self.fecha_fin_real:
            if self.fecha_inicio_real > self.fecha_fin_real:
                self.fecha_fin_real = False
                res['warning'] = {'title': ('Advertencia'),
                                  'message': (
                                      'La fecha de inicio real del proyecto no puede ser superior a la fecha de fin')
                                  }
        return res
