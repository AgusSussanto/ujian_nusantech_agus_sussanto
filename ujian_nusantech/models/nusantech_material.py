# -*- coding : utf-8 -*-
# Author => Agus Sussanto
# email  => agus.sussanto23@gmail.com

from odoo import api, models, fields, _
from odoo.exceptions import ValidationError

class nusantech_material(models.Model):
    _name = 'nusantech.material'

    @api.model
    def create(self, vals):
        res = super(nusantech_material, self).create(vals)
        for rec in res:
            if rec.material_buy_price < 100:
                raise ValidationError(_("Material Buy Price tidak boleh kurang dari 100"))
            else:
                seq = self.env['ir.sequence'].next_by_code('nusantech.material', sequence_date=rec.create_date) or '/'
                rec.name = seq
        return res

    def write(self, vals):
        res = super(nusantech_material, self).write(vals)
        if 'material_buy_price' in vals:
            if self.material_buy_price < 100:
                raise ValidationError(_("Material Buy Price tidak boleh kurang dari 100"))
        return res

    name = fields.Char(string="Material Name", default="New")
    material_code = fields.Char(string="Material Code")
    material_type = fields.Selection([('fabric','Fabric'),('jeans','Jeans'),('cotton','Cotton')], string="Material Type")
    material_buy_price = fields.Float(string="Material Buy Price", default=0.0)
    supplier_id = fields.Many2one('res.partner', string="Supplier")

