from odoo import fields, models


class Studio(models.Model):
    _name="cinema.studio"
    
    name=fields.Char(string="Name",required=True)