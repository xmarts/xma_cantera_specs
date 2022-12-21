from odoo import _, api, fields, models

class DoorColor(models.Model):
    _name = 'door.color'
    
    name = fields.Char(
        string='Nombre'
    )
    price = fields.Float(
        string='Precio'
    )