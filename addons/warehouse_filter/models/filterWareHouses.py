from odoo import models , fields , api


class FilterWareHouses(models.Model):
    _name = 'filter.warehouses'
    _description = "filter on warehouses"

   # name = fields.Char(string =_"Name", required_=_True)
    #related_partner = fields.Many2one('res.partner', string_=_"Related Partner")
    # #date_of_joining = fields.Date(string_=_"Date of joining")
    #def print_record(self):
        #print(" name of the record : %s"%self.name)
        #return True