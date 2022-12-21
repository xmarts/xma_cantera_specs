from odoo import _, api, fields, models

class DoorSpecialPreparationsList(models.Model):
    _name = 'door.special.preparations.list'
    
    name = fields.Char(
        string='Nombre'
    )
    price = fields.Float(
        string='Precio'
    )