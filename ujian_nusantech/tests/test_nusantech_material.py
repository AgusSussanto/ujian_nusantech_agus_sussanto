# -*- coding : utf-8 -*-
# Author => Agus Sussanto
# email  => agus.sussanto23@gmail.com

from odoo.tests.common import TransactionCase
import logging
_logger = logging.getLogger(__name__)

class test_nusantech_material(TransactionCase):
    """"""
    def setUp(self):
        res = super(test_nusantech_material, self).setUp()
        self.nusantech_material_obj = self.env['nusantech.material']
        self.supplier_obj = self.env['res.partner'].sudo().search([], limit=1)

    def test_scenario_1(self):
        """
        1. Create Material
        2. Jika Material Buy Price kurang dari 100, maka muncul warning
        """
        vals = {
            'name': 'Test Name 1',
            'material_code': 'Test Code 1',
            'material_type': 'jeans',
            'material_buy_price': 90,
            'supplier_id': self.supplier_obj.id
        }
        if vals['material_buy_price'] < 100:
            _logger.info("Warning: Material Buy Price tidak boleh kurang dari 100")


    def test_scenario_2(self):
        """
        1. Create Material
        2. Jika Material Buy Price >= 100, maka bisa ter-create
        """
        vals = {
            'name': 'Test Name 1',
            'material_code': 'Test Code 1',
            'material_type': 'jeans',
            'material_buy_price': 190,
            'supplier_id': self.supplier_obj.id
        }
        if vals['material_buy_price'] >= 100:
            material = self.nusantech_material_obj.sudo().create(vals)
            self.assertEqual(len(material), 1)
            _logger.info("Berhasil create 1 material baru")
