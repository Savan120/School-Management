from odoo import models, fields, api
from datetime import date

class library_detail(models.Model):
    _name = "library.detail"
    _description = "This is a library"
    # _rec_name = "student"
     
    student_id= fields.Many2many("student.info", string = "Student Name", required = True)

    # name=fields.Many2many("student.info", string ="Student Name")
    purchase = fields.Date(string="Purchase Date", required = True, default = date.today(), readonly = True)
    due = fields.Date(string = "Due Date", required = True, default = date.today())
    standard_id = fields.Many2one("standard.detail", string="Standard", required = True)
    # student=fields.Char(related="std.name")
    book = fields.Many2one("book.detail", string = "Book Name")
    price = fields.Float(related ="book.price",string = "Price")
    partner = fields.Many2one("res.partner", string = "Res Parthner")