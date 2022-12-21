# -*- coding: utf-8 -*-

from odoo import _, api, fields, models

class SpecsSale(models.Model):
	_name = 'specs.sale'
	_inherit = ['mail.thread', 'mail.activity.mixin']

	specs_type = fields.Selection(
		[('door', 'Puerta'),
		('windows', 'Ventana'),
		('railing', 'Barandal')],
		string='Tipo de Specs',
		default='door'
	)
	specs_sale_id = fields.Many2one(
		'sale.order',
		string='Cotización'
	)
	specs_amount_total = fields.Float(
    	string='Precio Total',
    )
	specs_leads_id = fields.Many2one(
		'crm.lead',
		string='guia'
	)
	specs_product_id = fields.Many2one(
		'product.category',
		string='Familia de producto'
	)
	specs_sd = fields.Boolean(
		string='single door'
	)
	specs_dd = fields.Boolean(
		string='Double Door'
	)
	specs_dc_id = fields.Many2one(
		'door.configuration',
		string='Configuración de Producto'
	)
	specs_design_id = fields.Many2one(
		'door.design',
		string='Diseño'
	)
	specs_color_id = fields.Many2one(
		'door.color',
		string='Color'
	)
	specs_level_id = fields.Many2one(
		'door.level',
		string='Nivel de Complejidad'
	)
	specs_mtrs = fields.Float(
    	string='Metros Cuadrados',
     	digits=(12, 4)
    )
	specs_suffix_id = fields.Many2one(
		'door.suffix',
		string='Sufijo'
	)
	specs_ant = fields.Float(
    	string='Ancho Total',
     	digits=(12, 4)
    )
	specs_alt = fields.Float(
    	string='Altura Total',
     	digits=(12, 4)
    )
	specs_antmarc = fields.Float(
    	string='Ancho con Marco',
     	digits=(12, 4)
    )
	specs_altmarc = fields.Float(
    	string='Altura con Marco',
     	digits=(12, 4)
    )
	specs_bast = fields.Float(
    	string='Ancho de Bastidor',
     	digits=(12, 4)
    )
	specs_porfbast = fields.Float(
    	string='Profundidad de Bastidor',
     	digits=(12, 4)
    )
	specs_antleaft = fields.Float(
    	string='Ancho de la Hoja',
     	digits=(12, 4)
    )
	specs_altleaft = fields.Float(
    	string='Altura de la Hoja',
     	digits=(12, 4)
    )
	specs_board_id = fields.Many2one(
		'door.board',
		string='Tablero'
	)
	specs_altboard = fields.Float(
    	string='Altura de Tablero',
     	digits=(12, 4)
    )
	specs_huacal = fields.Selection(
		[('yes', 'Yes'),
		('No', 'No')],
		string='Huecal',
	)
	specs_handing_id = fields.Many2one(
		'door.handing',
		string='Tablero'
	)
	specs_forging_id = fields.Many2one(
		'door.forging',
		string='Forja'
	)
	specs_operable = fields.Selection(
		[('yes', 'Yes'),
		('No', 'No')],
		string='Operable',
	)
	specs_type_arc_id = fields.Many2one(
		'door.type.arc',
		string='Tipo de Arco'
	)
	specs_altarc = fields.Float(
    	string='Altura de Arco',
     	digits=(12, 4)
    )
	specs_tolsup = fields.Float(
    	string='Tolerancia Superior (hoja y marco sup)',
     	digits=(12, 4)
    )
	specs_tolcen = fields.Float(
    	string='Tolerancia Central (entre hoja y hoja)',
     	digits=(12, 4)
    )
	specs_tollat = fields.Float(
    	string='Tolerancia de los Lados (entre hoja y marco izq y der)',
     	digits=(12, 4)
    )
	specs_glass = fields.Selection(
		[('yes', 'Yes'),
		('No', 'No')],
		string='Vidrio Fijo',
	)
	specs_type_glass_id = fields.Many2one(
		'door.type.glass',
		string='Tipo de Vidrio'
	)
	specs_ancmarc = fields.Float(
    	string='Ancho de Marco',
     	digits=(12, 4)
    )
	specs_profmarc = fields.Float(
    	string='Profundidad de Marco',
     	digits=(12, 4)
    )
	specs_anchor_id = fields.Many2one(
		'door.anchor',
		string='Ancla'
	)
	specs_hinges_id = fields.Many2one(
		'door.hinges',
		string='Bisagras'
	)
	specs_amount_hinges = fields.Integer(
    	string='Cantidad de Bisagras'
    )
	specs_molding_int_id = fields.Many2one(
		'door.molding.int',
		string='Moldura Interna'
	)
	specs_molding_ext_id = fields.Many2one(
		'door.molding.ext',
		string='Moldura Externa'
	)
	specs_traslape_int_id = fields.Many2one(
		'door.traslape.int',
		string='Traslape Externa'
	)
	specs_traslape_ext_id = fields.Many2one(
		'door.traslape.ext',
		string='Traslape Externa'
	)
	specs_jac_id = fields.Many2one(
		'door.pull.handles',
		string='Jaladera Activa Exterior'
	)
	specs_jacin_id = fields.Many2one(
		'door.pull.handles',
		string='Jaladera Activa Interior'
	)
	specs_jin_id = fields.Many2one(
		'door.pull.handles',
		string='Jaladera Intiva Exterior'
	)
	specs_jinin_id = fields.Many2one(
		'door.pull.handles',
		string='Jaladera Intiva Interior'
	)
	specs_pch_id = fields.Many2one(
		'door.metal',
		string='Preparacion de Chapa'
	)
	specs_moce_id = fields.Many2one(
		'door.lock',
		string='Modelo de Cerradura'
	)
	specs_altce = fields.Float(
    	string='Altura de Cerradura',
     	digits=(12, 4)
    )
	specs_mbas = fields.Float(
    	string='Medidas Bastidor Superior',
     	digits=(12, 4)
    )
	specs_mbai = fields.Float(
    	string='Medidas Bastidor Interior',
     	digits=(12, 4)
    )
	specs_rlat = fields.Integer(
    	string='Roller Latches'
    )
	specs_bac = fields.Integer(
    	string='Ball Catch'
    )
	specs_tyarct_id = fields.Many2one(
		'door.type.arct',
		string='Tipo de Arco en Transom'
	)
	specs_altarct = fields.Float(
    	string='Altura del Arco de Transom',
     	digits=(12, 4)
    )
	specs_antra = fields.Float(
    	string='Ancho de Transom',
     	digits=(12, 4)
    )
	specs_altra = fields.Float(
    	string='Altura de Transom',
     	digits=(12, 4)
    )
	specs_ddm = fields.Selection(
		[('yes', 'Yes'),
		('no', 'No')],
		string='Doble Marco',
	)
	specs_altpc = fields.Float(
    	string='Altura Panel Central',
     	digits=(12, 4)
    )
	specs_anpc = fields.Float(
    	string='Ancho Panel Central',
     	digits=(12, 4)
    )
	specs_anfi = fields.Float(
    	string='Ancho de Fijos',
     	digits=(12, 4)
    )
	specs_alfi = fields.Float(
    	string='Altura de Fijos',
     	digits=(12, 4)
    )
	specs_board_type_id = fields.Many2one(
		'door.board.type',
		string='Tipo de Tablero de Fijos'
	)
	specs_altboard_type = fields.Float(
    	string='Altura de Tablero de Fijoss',
     	digits=(12, 4)
    )
	specs_posfi_id = fields.Many2one(
		'door.position',
		string='Posicion del Fijo'
	)
	specs_line_ids = fields.One2many(
		'door.accessories',
		'acc_id'
	)
	specs_latchsup_id = fields.Many2one(
		'door.latch',
		string='Picaporte Superior'
	)
	specs_latchin_id = fields.Many2one(
		'door.latch',
		string='Picaporte Inferior'
	)
	specs_tolerance = fields.Float(
    	string='Tolerancia Guardapolvo',
     	digits=(12, 4)
    )
	specs_typeguar_id = fields.Many2one(
		'door.smock',
		string='Tipo de Guardapolvo'
	)
	specs_flashing_id = fields.Many2one(
		'door.flashing',
		string='Tipo de Flashing'
	)
	specs_assembly_id = fields.Many2one(
		'door.assembly',
		string='Preparación de Ensamble'
	)
	specs_sp_line_ids = fields.One2many(
		'door.special.preparations',
		'prep_id'
	)
	description = fields.Text(
		string='Comentarios'
	)
	specs_glass_line_ids = fields.One2many(
		'door.glass.specs',
		'glass_id'
	)
	specs_tramrec = fields.Float(
    	string='Tramo Recto (pulg lineales)',
     	digits=(12, 4)
    )
	specs_traminc = fields.Float(
    	string='Tramo Inclinado (pulg lineales)',
     	digits=(12, 4)
    )
	specs_tramcurniv = fields.Float(
    	string='Tramo Curvo a nivel (pulg lineales)',
     	digits=(12, 4)
    )
	specs_tramcurin = fields.Float(
    	string='Tramo Curvo inclinado (pulg lineales)',
     	digits=(12, 4)
    )
	specs_pasrec = fields.Float(
    	string='Pasamanos recto o inclinado (pulg lineales)',
     	digits=(12, 4)
    )
	specs_newdec = fields.Float(
    	string='Pasamanos curvos a nivel o curvo inclinado (pulg lineales)',
     	digits=(12, 4)
    )
 
	@api.onchange('specs_ant', 'specs_alt')
	def square_feet(self):
		for rec in self:
			ant = rec.specs_ant * 0.0254
			alt = rec.specs_alt * 0.0254
			rec.specs_mtrs = ant * alt
   
	@api.onchange('specs_sd')
	def sd_change(self):
		for rec in self:
			if rec.specs_sd == True:
				rec.specs_dd = False
	
	@api.onchange('specs_dd')	
	def dd_change(self):
		for rec in self:
			if rec.specs_dd == True:
				rec.specs_sd = False