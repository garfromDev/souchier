# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': u"""
        prototype souchier
        poc simplifié""",

    'description': u"""
        test souchier simplifié
    """,

    'author': "S. FROMONT",
    'website': "http://www.yourcompany.com",
    'installable': True
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
        'views/souchier.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
