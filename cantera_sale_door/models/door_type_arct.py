from odoo import _, api, fields, models

class DoorTypeArcT(models.Model):
    _name = 'door.type.arct'
    
    name = fields.Char(
        string='Nombre'
    )
    price = fields.Float(
        string='Precio'
    )