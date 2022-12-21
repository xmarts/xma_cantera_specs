from odoo import _, api, fields, models

class DoorBoard(models.Model):
    _name = 'door.board'
    
    name = fields.Char(
        string='Nombre'
    )
    price = fields.Float(
        string='Precio'
    )