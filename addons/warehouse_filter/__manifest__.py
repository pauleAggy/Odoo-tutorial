# -*- coding: utf-8 -*-
{
    'name': "warehouse_filter",

    'summary': """
        This module helps to apply a warehouse selection to a user
    """,

    'description': """
        On each user it is now possible to set a specific warehouse
        very simple way to configure and unlimited number od users
    """,

    'author': "Presprint PLC",
    'website': "https://www.presprint.cm",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'warehouse',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/warehouseFilterNew.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}