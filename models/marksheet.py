from odoo import models, fields, api
from odoo.exceptions import ValidationError


class marksheet(models.Model):
    _name = "marksheet.detail"
    _description= "Marksheet details"
    _rec_name = "stud_name"
    
    stud_name =fields.Many2one("student.info", string= 'Student Name', required = True)
    stud_roll=fields.Integer(related = "stud_name.roll", string="Student Roll")
    standard_id = fields.Many2one(related = "stud_name.standard_id",string = "Standard")
    # by default compute field is radonly, value not store in database
    # If you want to store compute fields value in database add attributes store=True
    marks= fields.Integer(compute="_compute_get_marks", string = "Marks Obtained")
    total_marks=fields.Integer(string= "Total Makrs", default = 400 , readonly = True)
    per=fields.Float(compute = "get_per", string= "Percentage %")
    grade = fields.Char(compute = "get_grade", string = "Grade")
    maths=fields.Integer(string="Maths", required = True)
    sci=fields.Integer(string = "Science", required = True)
    hindi=fields.Integer(string="Hindi")
    eng=fields.Integer(string= "English")
    year=fields.Char(string="Year")
   
    
    @api.constrains('maths', 'sci', 'hindi', 'eng')
    def marks_validation(self):
        for rec in self:
            if rec.maths <= 0 or rec.maths > 100:
                raise ValidationError('Please Enter Valid Marks!')
            elif rec.sci <= 0 or rec.sci > 100:
                raise ValidationError('Please Enter Valid Marks!')
            elif rec.hindi <= 0 or rec.hindi > 100:
                raise ValidationError('Please Enter Valid Marks!')
            elif rec.eng <= 0 or rec.eng > 100:
                raise ValidationError('Please Enter Valid Marks!')
                
    
    @api.depends("maths","sci","hindi","eng")
    def _compute_get_marks(self):
        for rec in self:
            rec.marks =(rec.maths + rec.sci + rec.hindi + rec.eng)

    @api.depends('marks', 'total_marks')
    def get_per(self):
        for record in self:
            record.per = 0.0
            if record.marks:
                record.per = (record.marks/record.total_marks* 100)
                
    @api.depends("per")
    def get_grade(self):
        for rec in self:
            if rec.per > 90:
                rec.grade = "A+"
                
            elif rec.per > 80:
                rec.grade = "A"
                
            elif rec.per > 70:
                rec.grade = "B+"
                
            elif rec.per > 60:
                rec.grade = "B" 
                 
            elif rec.per > 40:
                rec.grade = "C"
                
            elif rec.per > 25:
                rec.grade = "D"
            else:
                rec.grade = "F"
                
    @api.onchange("stud_name")
    def get_std(self):
        if self.stud_name:
            self.standard_id = self.stud_name.standard_id
            
    
    
            
            

        
    
    
    