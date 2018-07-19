# -*- coding: utf-8 -*-

from odoo import models, fields


class FilterNewWareHouses(models.Model):
    _name = "new.warehouses"
    _description = "filter on warehouses"
    name = fields.Char("Name")
    location = fields.Char("Location")
    is_done = fields.Boolean("Done?")