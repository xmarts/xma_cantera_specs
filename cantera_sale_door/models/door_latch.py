from odoo import _, api, fields, models

class DoorLatch(models.Model):
    _name = 'door.latch'
    
    name = fields.Char(
        string='Nombre'
    )
    price = fields.Float(
        string='Precio'
    )