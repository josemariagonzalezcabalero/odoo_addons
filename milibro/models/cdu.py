from odoo import fields, models, api


class CDU(models.Model):
    _name = 'milibro.cdu'
    _description = 'Codificacion Decimal Universal'

    name = fields.Char(string="Código", required=True)
    description = fields.Char(string="Descripción", required=True)

    # libro_ids = fields.One2many(comodel_name="milibro.libro", inverse_name="cdu_libro")

    @api.model
    def name_get(self):
        lista = []
        for registro in self:
            lista.append((registro.name,'-',registro.description))
        return lista

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        if args is None:
            args = []
        domain = args + [('name', operator, name),('description',operator, name)]
        return super(CDU,self).search(domain, limit=limit).name_get()