from odoo import _, api, fields, models

class DoorSpecialPreparations(models.Model):
    _name = 'door.special.preparations'
    
    preparations_id = fields.One2many(
		'product.template',
		'attribute_line_ids',
        string='Preparaciones Especiales',
		domain=[('name', '=', 'Preparaciones Especiales')]
    )
    amount_preparations = fields.Integer(
        string='Cantidad'
    )
    sequence = fields.Integer()
    prep_id = fields.Many2one(
        'specs.sale',
        string='Preparaciones Especiales'
    )