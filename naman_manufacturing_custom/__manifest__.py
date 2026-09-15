{
    'name': 'Naman Manufacturing Customizations',
    'version': '1.0',
    'category': 'Manufacturing',
    'summary': 'Add custom fields and automatic inventory UoM weight conversions matching NPW production sheets.',
    'depends': ['product', 'stock', 'mrp'],
    'data': [
        'views/product_views.xml',
        'views/mrp_production_views.xml',
        'views/mrp_bom_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
