from odoo import fields, models


class Actors(models.Model):
    _name="cinema.actors"
    
    name = fields.Char(string="Name",required=True)
    firstname = fields.Char(string="Firstname",required=True)
    