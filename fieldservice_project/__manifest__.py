
# Copyright (C) 2019 - TODAY, Patrick Wilson
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Field Service - Project',
    'summary': 'Create field service orders from a project or project task',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Pavlov Media, Odoo Community Association (OCA)',
    'category': 'Project',
    'website': 'https://github.com/OCA/field-service',
    'depends': [
        'fieldservice',
        'project',
    ],
    'data': [
        'views/project_views.xml',
        'views/project_task_views.xml',
        'views/fsm_location_views.xml',
        'views/fsm_order_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
}
