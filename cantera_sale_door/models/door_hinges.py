from odoo import _, api, fields, models

class DoorHinges(models.Model):
    _name = 'door.hinges'
    
    name = fields.Char(
        string='Nombre'
    )
    price = fields.Float(
        string='Precio'
    )