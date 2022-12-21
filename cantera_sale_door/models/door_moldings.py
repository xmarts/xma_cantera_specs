from odoo import _, api, fields, models

class DoorMoldingInt(models.Model):
    _name = 'door.molding.int'
    
    name = fields.Char(
        string='Nombre'
    )
    price = fields.Float(
        string='Precio'
    )
    
class DoorMoldingExt(models.Model):
    _name = 'door.molding.ext'
    
    name = fields.Char(
        string='Nombre'
    )
    price = fields.Float(
        string='Precio'
    )