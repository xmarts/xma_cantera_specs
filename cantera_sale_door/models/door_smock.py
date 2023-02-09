from odoo import _, api, fields, models

class DoorSmock(models.Model):
    _name = 'door.smock'
    
    name = fields.Char(
        string='Nombre'
    )
    price_sd = fields.Float(
        string='Precio Single Door'
    )
    price_dd = fields.Float(
        string='Precio Double Door'
    )