from odoo import fields, models

class Movies(models.Model):
    _name="cinema.movies"
    
    name = fields.Char(string="Name", required=True)
    date = fields.Date(string="Date",required=True)
