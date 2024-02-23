{
    'name': 'Filtro por Fecha en Existencias a la Fecha',
    'version': '1.0',
    'category': 'Inventario',
    'author': 'Antonio Queb',
    'website': 'https://www.odoo.com/',
    'license': 'LGPL-3',
    'depends': ['stock'],
    'data': [
        'views/filtro_fecha_existencias_view.xml',
        'models/filtro_fecha_existencias_model.py',
    ],
    'installable': True,
    'auto_install': False,
}

