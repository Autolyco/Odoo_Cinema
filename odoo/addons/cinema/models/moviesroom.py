from odoo import fields, models

class Moviesroom(models.Model):
    _name="cinema.moviesroom"
    
    name = fields.Char(string="Name",required=True)
    date = fields.Date(String="Date",required=True)
    realisator = fields.Char(String="Realisator",required=True)
    rating = fields.Integer(string="Rating")
    begin_on = fields.Datetime(string="Begin on",required=True)
    end_on = fields.Datetime(string="End on",required=True)