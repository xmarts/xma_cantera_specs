from odoo import _, api, fields, models

class DoorPullHandles(models.Model):
    _name = 'door.pull.handles'
    
    name = fields.Char(
        string='Nombre'
    )
    price = fields.Float(
        string='Precio'
    )