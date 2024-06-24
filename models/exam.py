from odoo import models, fields, api # type: ignore

class exam(models.Model):
    _name = "exam.detail"
    _description = "This is exam model"
    _rec_name = "exam_type"
    
    start_date = fields.Date(string = "Exam Start", required = True)
    end_date = fields.Date(string = "Exam End", required = True)
    pass_mark = fields.Float(string = "Passing Marks")
    exam_type = fields.Selection([('theory','Theory'),('practical','Practical')])
    subject_ids=fields.Many2many("subject.detail", string = "Subject")
    standard_ids=fields.Many2one("standard.detail", string= "Standard")
    student_id = fields.Many2one("student.info", string = "Student")
    

class exam_rec(models.Model):
    _name = "exam.record"
    _description = "exam record"
    
    
    exam_type = fields.Many2one("exam.detail", string = "Exam Type")
    start_date = fields.Date(related = "exam_type.start_date",string = "Exam Start")
    end_date = fields.Date(related = "exam_type.end_date", string = "Exam End")
    subject_ids=fields.Many2many("subject.detail", related = "exam_type.subject_ids", string = "Subject")
    student_rec = fields.Many2one("student.info", string = "Student")
    standard_rec=fields.Many2one(related="exam_type.standard_ids" , string="Student Standard")