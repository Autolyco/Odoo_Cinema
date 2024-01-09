from odoo import fields, models

class Memberships(models.Model):
    _name="cinema.membership"
    
    state = fields.Char(string="State", required=True)
    expiration_date = fields.Date(string="Expiration date", required=True)