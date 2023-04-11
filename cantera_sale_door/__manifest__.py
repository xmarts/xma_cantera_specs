# -*- coding: utf-8 -*-
{
    'name': "Especificaciones Canteras",

    'summary': """ """,

    'description': """
        
    """,

    'author': "Xmarts",
    'collaborators': "Cesar Noriega",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'sale_management',
                'sale',
                'crm',
                'sale_crm',
                'product',
                'mail',
                'mrp',
            ],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/stage_cantera_type_data.xml',
        'views/specs_sale.xml',
        'views/door_configuration_views.xml',
        'views/door_design_views.xml',
        'views/door_level_views.xml',
        'views/door_suffix_views.xml',
        'views/door_handing_views.xml',
        'views/door_type_arc_views.xml',
        'views/door_type_glass_views.xml',
        'views/door_traslape_views.xml',
        'views/door_metal_views.xml',
        'views/door_board_type_views.xml',
        'views/door_position_views.xml',
        'views/door_accessories_list_views.xml',
        'views/door_accessories_views.xml',
        'views/door_assembly_views.xml',
        'views/door_special_preparations_views.xml',
        'views/door_glass_piece_views.xml',
        'views/door_handing_glass_views.xml',
        'views/door_radius_views.xml',
        'views/door_glass_specs_views.xml',
        'views/door_family_views.xml',
        'views/railing_views.xml',
        'views/sale_order_views.xml',
        'views/mrp_bom_views.xml',
        'views/product_template_attribute_value_views.xml',
        'report/report_cantera_specs.xml', 
    ],
    # only loaded in demonstration mode
    'demo': [
        
    ],
}