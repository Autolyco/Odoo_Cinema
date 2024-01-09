from odoo import fields, models

class Clients(models.Model):
    _name="cinema.clients"
    
    name = fields.Char(string="Name" ,required=True)
    firstname = fields.Char(string="Firstname",required=True)
    age = fields.Integer(string="Age",required=True)
    address = fields.Char(string="Address" ,required=True)
    tel = fields.Char(string="Telephone",required=True)
    gender = fields.Char(string="Gender", required=True)
    membership = fields.Char(string="Membership", required=True)