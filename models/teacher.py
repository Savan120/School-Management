from odoo import models , fields, api    
from datetime import date

class teacher_detail(models.Model):
    _name = "teacher.info"
    _description="teacher detail"
    _rec_name = "standard"
    
    
    teacher_name   = fields.Char(string = "Name" )
    campus = fields.Char(string = "Campus", default= "Ved International School")
    subject = fields.Char(string = "Subject")
    add    = fields.Text(string = "Work Address")
    phone  = fields.Char(string = "Phone Number")
    mail   = fields.Char(string = "Work E-Mail Id")
    location= fields.Char(string = "Work Location")
    parent = fields.Boolean(string = "Is parent")
    depart = fields.Selection(related = "standard.depart",string = "Department")	
    job    = fields.Char(string = "Job Position")	
    manager= fields.Char(string = "Manager")
    country1 = fields.Many2one('res.country',string = "Country")
    passport = fields.Char(string = "Passport No.")
    bank = fields.Char(string = "Bank Account No.")
    address = fields.Text(string = "Address")
    gender = fields.Selection([("male" , "Male"), ("female" , "Female"), ("other" , "Other")],string = "Gender")
    marital = fields.Selection([('single','Single'),('married','Married')],string = "Marital Status")
    dob    = fields.Date(string = "Date of birth", default = date.today())
    image = fields.Image(string = "image")
    standard =  fields.Many2one("standard.detail", string = "Responsibility of")
    student_name=fields.Many2one("student.info", string = "Student Name")
    salary= fields.Float(string = "Salary")
    all_student = fields.Integer(compute ="compute_student_count", string = "Student Count" )
    reject_student = fields.Integer(compute ="compute_student_count", string = "Rejected Student" )
    # student_present=fields.Integer(compute ="compute_student_attendence", string = "Is present")
     
    
    
#----------------------------------------------------------------------------------------------------------




    def student_count(self):
        return {
            'name': 'Students',
            'res_model': 'student.info',  
            'view_mode': "tree",
            'type': 'ir.actions.act_window',
            'domain': [("standard_id","=",self.standard.id),'|',("state",'=','set_to_application'),("state",'=','reject')],
            'context':{"create":False,"delete":False,"edit":False}
        }
    
    @api.depends('standard')
    def compute_student_count(self):
        for record in self:
            students = self.env['student.info'].search_count([('standard_id','=', record.standard.id),("state",'=','set_to_application')])
            record.all_student = students
            
            student_reject = self.env['student.info'].search_count([('standard_id','=', record.standard.id),("state",'=','reject')])
            record.reject_student = student_reject
            
            
            
    # def student_parents(self):
    #     view_id = self.env.ref('School_management_system.student_tree_view')
    #     return {
    #         'name': 'Attendence',
    #         'res_model': 'student.info',  
    #         'view_mode': "tree",
    #         'type': 'ir.actions.act_window',
    #         'views':[[view_id.id,'tree']],
    #         'context':{"create":False,"delete":False,"edit":False},
    #     }            
        
    # @api.depends('standard')
    # def compute_student_attendence(self):
    #     for record in self:
    #         attendence = self.env['student.info'].search_count([('standard_id','=', record.standard.id)])
    #         print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",attendence)
    #         record.student_present = attendence
            
           
    
    
    
