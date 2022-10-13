# -*- coding: utf-8 -*-
{
    'name': "nahe_replenishment_cost_button",

    'summary': """
        Boton para correr el cron de costo de reposicion""",

    'description': """
        1º Boton para correr el cron de costo de reposicion en la vista de las tasas de una moneda. 
        2º Se puede agregar el mismo boton donde lo necesiten.
    """,

    'author': "Nähe Consulting Group",
    'website': "http://www.nahe.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
