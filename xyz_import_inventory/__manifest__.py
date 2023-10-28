# -*- coding: utf-8 -*-
{
    'name': "XYZ Module - Import Product Custom",
    'summary': """XYZ Module - Import Product Custom""",
    'description': """
        XYZ Module - Import Product Custom
        Insert / Update the product based on Internal Reference (default_code) when importing the product file.
        The products will be updated if default_code already exists, otherwise will insert the products.
    """,
    'author': "Ogas",
    'website': "https://github.com/iogias",
    'category': 'Inventory',
    'version': '1.0',
    'depends': ['stock'],
    'data': [],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
