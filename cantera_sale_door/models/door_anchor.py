from odoo import _, api, fields, models

class DoorAnchor(models.Model):
    _name = 'door.anchor'
    
    name = fields.Char(
        string='Nombre'
    )
    price = fields.Float(
        string='Precio'
    )