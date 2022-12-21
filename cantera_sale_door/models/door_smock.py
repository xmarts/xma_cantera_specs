from odoo import _, api, fields, models

class DoorSmock(models.Model):
    _name = 'door.smock'
    
    name = fields.Char(
        string='Nombre'
    )
    price = fields.Float(
        string='Precio'
    )