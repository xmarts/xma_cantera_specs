from odoo import _, api, fields, models

class DoorLock(models.Model):
    _name = 'door.lock'
    
    name = fields.Char(
        string='Nombre'
    )
    price = fields.Float(
        string='Precio'
    )