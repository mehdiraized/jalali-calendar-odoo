# -*- coding: utf-8 -*-
{
    'name': 'Jalali Calendar for Odoo CRM',
    'version': '0.1',
    'summary': 'Adds Jalali (Persian) calendar to Odoo CRM',
    'description': """
        This module adds Jalali (Persian) calendar functionality to all sections of Odoo CRM.
        Users can use the Jalali calendar throughout the Odoo CRM application.
    """,
    'category': 'CRM',
    'author': 'Mehdi Rezaei',
    'website': 'https://mehd.ir',
    'depends': ['crm'],
    'data': [
        'views/crm_views.xml',
    ],
    'qweb': ['static/src/xml/jalali_calendar.xml'],
    'assets': {
        'web.assets_backend': [
            'jalali_calendar_crm/static/src/js/jalali_calendar.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}