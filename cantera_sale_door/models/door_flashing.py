from odoo import _, api, fields, models

class DoorFlashing(models.Model):
    _name = 'door.flashing'
    
    name = fields.Char(
        string='Nombre'
    )
    price = fields.Float(
        string='Precio'
    )