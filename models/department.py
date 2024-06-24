from odoo import models, fields, api


class department(models.Model):
    _name= "department.detail"
    _description = "This is an school department"
    
    depart = fields.Selection([('primary','Primary'),('secondary','Secondary'),('higher','Higher')],string = "Department")	
    incharge = fields.Char(string = "Incharge Name")
    member= fields.Many2many('teacher.info', string= "Teachers")
    