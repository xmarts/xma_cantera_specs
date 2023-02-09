from odoo import _, api, fields, models

class DoorMoldingInt(models.Model):
    _name = 'door.molding'
    
    name = fields.Char(
        string='Nombre'
    )
    price_sd = fields.Float(
        string='Precio Single Door'
    )
    price_dd = fields.Float(
        string='Precio Double Door'
    )
    price_bifolds = fields.Float(
        string='Precio Bifolds'
    )