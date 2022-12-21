from odoo import _, api, fields, models

class DoorForging(models.Model):
    _name = 'door.forging'
    
    name = fields.Char(
        string='Nombre'
    )
    price = fields.Float(
        string='Precio'
    )