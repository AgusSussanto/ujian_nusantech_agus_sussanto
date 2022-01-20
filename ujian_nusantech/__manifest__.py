# -*- coding: utf-8 -*-
# Author => Agus Sussanto
# email  => agus.sussanto23@gmail.com

{
    'name': 'Ujian Nusantech',
    'version': '14.0.1.0.0',
    'category': 'Inventory',
    'summary': 'Ujian Nusantech',
    'description': """
        Module ini adalah module ujian dari Nusantech
    """,
    'website': '',
    'author':'Agus Sussanto',
    'depends': ['base','web'],
    'data': [
                'security/ir.model.access.csv',
                'views/nusantech_material_view.xml',
                'views/nusantech_material_action.xml',
                'views/nusantech_material_menuitem.xml',
                'views/nusantech_material_sequence.xml',
            ],
    'qweb': [],
    'installable': True,
    'application': True,
    'license': 'OEEL-1',
}