# -*- coding: utf-8 -*-

from odoo import _, api, fields, models

import logging

_logger =logging.getLogger(__name__)

class SpecsSale(models.Model):
	_name = 'specs.sale'
	_inherit = ['mail.thread', 'mail.activity.mixin']
	_rec_name = 'name_specs'


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
		'door.family',
		string='Familia de producto'
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
		'door.molding',
		string='Moldura Interna'
	)
	specs_molding_ext_id = fields.Many2one(
		'door.molding',
		string='Moldura Externa'
	)
	specs_traslape_int_id = fields.Many2one(
		'door.traslape',
		string='Traslape Externa'
	)
	specs_traslape_ext_id = fields.Many2one(
		'door.traslape',
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
	specs_cls = fields.Integer(
    	string='Cantidad Picaporte Superior'
    )
	specs_cli = fields.Integer(
    	string='Cantidad Picaporte Inferior'
    )
	name_specs = fields.Char(
		compute='name_create'
	)
	railing_id = fields.Many2one(
		'railing',
		string='Railing'
	)
 
	@api.constrains(
		'specs_ant', 'specs_alt','specs_product_id','specs_dc_id','specs_molding_ext_id',
		'specs_molding_int_id','specs_flashing_id','specs_typeguar_id','specs_latchsup_id',
		'specs_latchin_id','specs_jac_id','specs_jacin_id','specs_jin_id','specs_jinin_id',
		'specs_cls','specs_cli','specs_tramrec','specs_traminc','specs_tramcurniv',
  		'specs_tramcurin','specs_pasrec','specs_newdec','specs_type_arc_id','specs_tyarct_id'

	)
	def square_feet(self):
		for rec in self:
			ant = rec.specs_ant * 0.0254
			alt = rec.specs_alt * 0.0254
			total = ant * alt
			rec.specs_mtrs = total
			price_family = rec.specs_product_id.price * total
			if rec.specs_type == 'door' or rec.specs_type == 'windows':
				if str(rec.specs_dc_id.name)[:2] == 'SD':
					flashing = rec.specs_flashing_id.price_sd
					smock = rec.specs_typeguar_id.price_sd
				if str(rec.specs_dc_id.name)[:2] == "Fixed" or str(rec.specs_dc_id.name)[:2] == "Casement" or str(rec.specs_dc_id.name)[:2] == "Awning":
					flashing = rec.specs_flashing_id.price_dd
				if str(rec.specs_dc_id.name)[:2] == 'DD':
					flashing = rec.specs_flashing_id.price_dd
					smock = rec.specs_typeguar_id.price_dd
				if str(rec.specs_dc_id.name)[:2] == 'SD' or str(rec.specs_dc_id.name)[:4] == 'SDSL' or str(rec.specs_dc_id.name)[:2] == 'DD' or str(rec.specs_dc_id.name)[:4] == 'DDSL':
					if str(rec.specs_type_arc_id.name)=='None' or str(rec.specs_type_arc_id.name)=='Simulated Eyebrow arch':
						configuration = rec.specs_molding_int_id.price_sd + rec.specs_molding_ext_id.price_sd
				if str(rec.specs_dc_id.name) == 'SDFS' or str(rec.specs_dc_id.name) == 'SDT' or str(rec.specs_dc_id.name) == 'SDTCP' or str(rec.specs_dc_id.name) == 'SDTCPSL' or str(rec.specs_dc_id.name) == 'SDTSL' or str(rec.specs_dc_id.name) == 'DDFS' or str(rec.specs_dc_id.name) == 'DDT' or str(rec.specs_dc_id.name) == 'DDTCP' or str(rec.specs_dc_id.name) == 'DDTCPSL' or str(rec.specs_dc_id.name) == 'DDTSL':
					if str(rec.specs_tyarct_id.name)=='Custom' or str(rec.specs_tyarct_id.name)=='Darla' or str(rec.specs_tyarct_id.name)=='Eliptical' or str(rec.specs_tyarct_id.name)=='Eyebrow' or str(rec.specs_tyarct_id.name)=='Full' or str(rec.specs_tyarct_id.name)=='Gothic' or str(rec.specs_tyarct_id.name)=='Provenzal':
						configuration = rec.specs_molding_int_id.price_dd + rec.specs_molding_ext_id.price_dd
						_logger.info(configuration,'################################################################################333')
				else:
					configuration = 0
					flashing = 0
					smock = 0
			if rec.specs_type == 'railing':
				if rec.specs_tramrec:
					linea = self.env['railing'].search([('name', '=', 'Straight')])
					tramo_recto = rec.specs_tramrec * linea.price 
				if rec.specs_traminc:
					inclinado = self.env['railing'].search([('name', '=', 'Raked')])
					tramo_inclinado = rec.specs_traminc * inclinado.price 
				if rec.specs_tramcurniv:
					curv_niv = self.env['railing'].search([('name', '=', 'Curved')])
					curvo_nivel = rec.specs_tramcurniv * curv_niv.price 
				if rec.specs_tramcurin:
					curv_inc = self.env['railing'].search([('name', '=', 'Curved Raked')])
					curvo_inclin = rec.specs_tramcurin * curv_inc.price 
				if rec.specs_pasrec:
					pas_rec_inc = self.env['railing'].search([('name', '=', 'Handrail S o R')])
					pass_rec_inc = rec.specs_pasrec * pas_rec_inc.price
				if rec.specs_newdec:
					pas_cur = self.env['railing'].search([('name', '=', 'Handrail C o CR')])
					pass_cur = rec.specs_newdec * pas_cur.price 
				else:	
					tramo_recto = 0.00
					tramo_inclinado = 0.00
					curvo_nivel = 0.00
					curvo_inclin = 0.00
					pass_rec_inc = 0.00
					pass_cur = 0.00
			else:
				continue
			_logger.info(tramo_recto,'################################################################################333')
			_logger.info(tramo_inclinado,'################################################################################333')
			_logger.info(curvo_nivel,'################################################################################333')
			_logger.info(curvo_inclin,'################################################################################333')
			_logger.info(pass_rec_inc,'################################################################################333')
			_logger.info(pass_cur,'################################################################################333')
			# total_railing = tramo_recto + tramo_inclinado + curvo_nivel + curvo_inclin + pass_rec_inc + pass_cur
			latch = (rec.specs_latchsup_id.price * rec.specs_cls) + (rec.specs_latchin_id.price * rec.specs_cli)
			handled = rec.specs_jac_id.price + rec.specs_jacin_id.price + rec.specs_jin_id.price + rec.specs_jinin_id.price
			family_conf = price_family + configuration + flashing + smock + latch + handled
			rec.specs_amount_total = family_conf
   
	def name_create(self):
		for rec in self:
			rec.name_specs=''
			if rec.specs_type == 'door':
				value = 'Puerta'
			if rec.specs_type == 'windows':
				value = 'Ventana'
			if rec.specs_type == 'railing':
				value = 'Barandal'
			nombre =value+' '+str(rec.specs_dc_id.name)+' '+str(rec.specs_product_id.name)
			if rec.specs_type:
				rec.name_specs=nombre
	
