from odoo import _, api, fields, models

class DoorFlashing(models.Model):
    _name = 'door.flashing'
    
    name = fields.Char(
        string='Nombre'
    )
    price_sd = fields.Float(
        string='Precio Single Door'
    )
    price_dd = fields.Float(
        string='Precio Doble Door'
    )
    price_bifolds = fields.Float(
        string='Precio Bifolds'
    )