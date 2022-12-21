from odoo import _, api, fields, models

class DoorTraslapeInt(models.Model):
    _name = 'door.traslape.int'
    
    name = fields.Char(
        string='Nombre'
    )
    price = fields.Float(
        string='Precio'
    )
    
class DoorTraslapeExt(models.Model):
    _name = 'door.traslape.ext'
    
    name = fields.Char(
        string='Nombre'
    )
    price = fields.Float(
        string='Precio'
    )