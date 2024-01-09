from odoo import fields, models

class Realisators(models.Model):
    _name="cinema.realisators"
    
    name = fields.Char(string="Name", required=True)
    firstname = fields.Char(string="Firstname", required=True)