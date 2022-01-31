# -*- coding: utf-8 -*-
{
    'name': "mimodulo",

    # Para que aparezca el primero
    'sequence': 0,
    # Para que entre en el filtro de aplicaciones
    'application': True,

    'summary': """
        Es mi primerito módulo.""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Jose Maria Gonzalez Caballero",
    'website': "http://www.ieschirinos.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/persona.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
