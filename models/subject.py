from odoo import models , fields

class subject_detail(models.Model):
    _name = "subject.detail"
    _description = "subject detail"
    _rec_name = "sub"
    
    sub = fields.Char(string = "Subject Name", required = True)
    code = fields.Char(string = "Subject Code", required = True)

    
    