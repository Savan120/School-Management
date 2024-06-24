from odoo import models, fields



class book(models.Model):
    _name = "hobby.detail"
    _description = "Hobby Detail"
    
    name = fields.Char(string = "Hobby Name")
    custom_hobbies_ids = fields.Many2many('hobby.detail', 'custom_hobby_schooo_rel', 'hobby_id', 'student_id', string="Custom Table Hobby")
    
    _sql_constraints = [('hobby_detail', 'unique(name)', 'Name must be unique!')]