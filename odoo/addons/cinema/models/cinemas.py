from odoo import fields, models

class Cinemas(models.Model):
    _name="cinema.cinemas"
    
    name = fields.Char(string="Name" ,required=True)
    address = fields.Char(string="Address" ,required=True)
    mail = fields.Char(string="Mail" ,required=True)
    tel = fields.Char(string="Telephone" ,required=True)
    city = fields.Char(string="City" ,required=True) 