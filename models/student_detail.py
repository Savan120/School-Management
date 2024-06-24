from odoo import models , fields, api
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError




class student_form(models.Model):
    _name = "student.info"
    _description="This class contains student detail"
    _inherit = ['mail.thread','mail.activity.mixin']
    
    roll   = fields.Integer(string = "Roll No.", required = True)
    name   = fields.Char(string = "Name", required = True)
    school = fields.Char(string = "School", default= "Ved International School", readonly = True)
    add    = fields.Text(string = "Address")
    dob    = fields.Date(string = "Date of birth", required = True, default = datetime.today())
    gender = fields.Selection([("male" , "Male"), ("female" , "Female"), ("other" , "Other")],string = "Gender", required = True)
    age    = fields.Char(string = "Age", compute = "get_age", required = True)
    lang   = fields.Selection([("h","Hindi"),('e',"English"),("g","Gujarati"),('m',"Marathi"),('marwadi',"Marwadi")],string =  "Mother Tongue")
    admission = fields.Date(string = "Admission Date",default = datetime.today())
    blood_grp = fields.Selection([('a+', 'A+'),('b+', 'B+'),('ab+', 'AB+'),('ab-', 'AB-'),('o+', 'O+'),('o-', 'O-')], string="Blood Group")
    image = fields.Binary(string = "image")
    parent_no=fields.Char(string="Parent No")
    parent_mail=fields.Char(string="Parent E-mail")
    father_name = fields.Char(string = "Father name")
    mother_name = fields.Char(string = "Mother name")
    mother_occ = fields.Char(string = "Mother Occupation")
    father_occ = fields.Char(string = "Father Occupation")
    standard_id = fields.Many2one("standard.detail", string = "Standard", required = True)
    medium_id = fields.Selection(related="standard_id.medium", string="Medium")
    fee_id = fields.Float(related = "standard_id.fee" , string= "Fees", store=True)
    subject = fields.Many2many(related = "standard_id.standard_id")
    teacher = fields.Char(related = "standard_id.teacher")
    state = fields.Selection([('application','Application'),('confirm','Confirm'),("approve", "Approve"),("reject",'Reject'),('set_to_application','Set To Application')], default="application",string="state")
    previous_sch= fields.Char(string= "School Name")
    previous_std= fields.Char(string= "Previous Standard")
    marksheet_ids = fields.One2many("marksheet.detail",'stud_name', string = "Marksheet", readonly="1")
    sequence = fields.Char(string = "Student Id", readonly = True, store = True)
    hobby_ids=fields.Many2many("hobby.detail", string="Hobby")
    properties_ids= fields.One2many("property.record", 'student_id', string = "Property detail")
    terms = fields.Char(string = "Terms & Conditions")
    total = fields.Float(compute = "get_total",string = "Total")
    exam_ids = fields.One2many('exam.record', 'student_rec', string = "Exam")
    ispresent=fields.Boolean(string="Is Present")
    user_id=fields.Many2one('res.users', string="Relation User", default = lambda self : self.env.user)
    
    
    # def action_share_whatsapp(self):
    #     if not self.name.parent_no:
    #         raise ValidationError("Missing mobile no or invalid phone number")
    #     whatsapp_api_url = "http://api.whatsapp.com/send?parent_no=%s&text=%s"%(self.name.parent_no,msg)
    #     msg="Hi %s" % self.name.parent_no
    #     return {
    #         "type":"ir.action.act_url",
    #         "target":'new',
    #         "url":whatsapp_api_url
    #     }
    
    def action_send_mail_fees(self):
        for rec in self:
            send_data = rec.env.ref('School_management_system.email_template_student')
            send_data.send_mail(rec.id, force_send= True)
            
    def action_send_mail_marksheet(self):
        for rec in self:
            send_data = rec.env.ref('School_management_system.email_student_marksheet')
            send_data.send_mail(rec.id, force_send= True)
    
    def action_send_mail_property(self):
        for rec in self:
            send_data = rec.env.ref('School_management_system.email_school_property')
            send_data.send_mail(rec.id, force_send= True)
            
    @api.depends('properties_ids.total_id')
    def get_total(self):
        for rec in self:
            rec.total = sum(rec.properties_ids.mapped('total_id'))
            

    @api.depends("dob")  
    def get_age(self):
        self.age= 0
        for rec in self:
            rec.age = relativedelta(date.today(),rec.dob).years
               
               
    def action_confirm1(self):
        for rec in self:
            rec.state = "confirm"
    
    def action_reject1(self):
        for rec in self:
            rec.state = "reject"
            
    def action_approve1(self):
        for rec in self:
            rec.state = "approve"
    
    def action_application1(self):
        for rec in self:
            rec.state = "application"
    
    def action_review1(self):
        for rec in self:
            rec.state = "review"
    
    def action_set_to_app(self):
        for rec in self:
            rec.state = "set_to_application"
    
            
    @api.model_create_multi
    def create(self, vals_list):
      """For Create sequence"""
      for vals in vals_list:
         print('vals >>>>>>>>>>>>>>>>>', vals)
         seq = self.env['ir.sequence'].next_by_code('student') or ("New")
         print('seq >>>>>>>>>>>>>>>>>>', seq)
         vals['sequence'] = seq
      return super().create(vals_list)
  
    
    
# ----------------------------------------------------------------------------------------------------------    

    # THIS IS A SEARCH COUNT THAT COUNT AS PER FILTER
    def count_search(self):
        for rec in self:
            hey = rec.search_count([('gender', '=','female')])
            print("??????????????????????????????",hey)
            print("??????????????????????????????",type(hey))
            
    
               
    # THIS IS A NAME SEARCH METHOD

    def _name_search(self, name, args=None, operator='ilike', limit=100):
        if name:
            args=['|',('name', operator, name)]
            print("'''''''''''''''''''''''''''''''''''''''''''''''''''''", args)
        return super()._name_search(name, args, operator, limit)

# ----------------------------------------------------------------------------------------------------------   
               
#     # THIS IS A NAME SEARCH METHOD
    @api.model
    def search(self, domain=None, offset=0, limit=None, order=None, count=False):
        print(' Search call 8888888888888888>>>>>>', self._context, '\n')
        if self._context.get('call_from_student'):
            domain = [('gender','=','female')]
        return super().search(domain, offset=0, limit=None, order=None, count=False)
    
    

#THIS IS AN CODY METHOD
    # def duplicate(self, defalut= None):
    #     hey = self.copy(default= {"parent_no" : "1234567890"})
    #     print("'''''''''''''''''''''''''''''''''''''''''''''''''''",hey)
# ----------------------------------------------------------------------------------------------------------    

    # def add_o2m(self):
    #     #[(0,0 {})] -- this is to create record in O2m
    #     vals1 = {
    #         'property_ids': 'Icard',
    #         'qty_id': 1.0,
    #         'price_id':600.00,
    #     }
 
    #     vals2 = {
    #         'property_ids': 'Tie',
    #         'qty_id': 1,
    #         'price_id':200,
    #     }
    #     self.properties_ids = [(0,0, vals1), (0,0, vals2)]
        
        
    # def add_hobbies(self):
    #     hobby_list = [3,4]
    #     for hobby in hobby_list:
    #         self.hobby_ids = [(4,hobby)]
    #     # res = self.env['hobby.detail'].search([('name','=','Football')])
    #     # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",res)
    #     # for hobby in res:
    #     #     self.hobby_ids(4,hobby)
    
    
    # def update_value(self):
    #     # (1, ID, { values }) update the linked record with id = ID (write values on it)
    #     property=self.env["property.record"].search([('property_ids','=','Books')])
    #     for rec in self:
    #         rec.properties_ids=[{1, property.id, {'price_id': 3000, 'qty_id': 3}}]
            
            
    # def unlink_record(self):
    #     hobby_id=[3,4]
    #     # hobby_id = self.env["hobby.detail"].search([('name', '=','Football'),('name', '=','Cricket')])
    #     for rec in hobby_id:
    #         self.hobby_ids = [(2,rec)]
            
            
    # # def default_get(self, fields):
    # #     res= super().default_get(fields)
    # #     print("??????????????????????????????????????",res)
    # #     res.update({'hobby_ids': [(6,0,[4,5])]})
    # #     return res
    
    
    # def delete_record(self):
    #     rec_id=[23,22]
    #     for rec in rec_id:
    #         self.hobby_ids=[(3,rec)]
    
    
    # def student_count(self):
    #     return {
    #         'name': 'Students',
    #         'res_model': 'student.info',  
    #         'view_mode': "tree,form",
    #         'type': 'ir.actions.act_window',
    #         'domain': [],
    #         'context':{"create":False,"delete":False,"edit":False}
    #     }
    
    # @api.depends('standard')
    # def compute_student_count(self):
    #     for record in self:
    #         students = self.env['student.info'].search_count([('standard_id','=', record.standard.id),("state",'=','set_to_application')])
    #         record.all_student = students
            
    #         student_reject = self.env['student.info'].search_count([('standard_id','=', record.standard.id),("state",'=','reject')])
    #         record.reject_student = student_reject
    

    
# ----------------------------------------------------------------------------------------------------------
    
    # def do_search(self):
    #     hey = self.search([('teachers', '=' ,'male')])
    #     print(">>>>>>>>>>>>>>>>>>>>>>>>>",hey)
    #     for rec in hey:
    #         print("@@@@@@@@@@@@@@@@@@@@",rec.name)
    #     return True
    
# ----------------------------------------------------------------------------------------------------------
    # THIS IS AN SEARCH METHOD USING IN RELATION FIELD
    # def do_search(self):
    #     hey = self.search([('gender', '=' ,'female')])
    #     print(">>>>>>>>>>>>>>>>>>>>>>>>>",hey)
    #     for rec in hey:
    #         record= rec.teachers.name
    #         print("@@@@@@@@@@@@@@@@@@@@",record)
    #     return True

# ----------------------------------------------------------------------------------------------------------
    # # THIS IS AN SEARCH COUNT METHOD USING IN RELATION FIELD
    # def count_search(self):
    #     for record in self:
    #         hey = rec.search_count([('gender', '=','female')])
    #         print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",hey)
    #         for rec in hey:
    #             record=rec.teachers.name
    #             print("??????????????????????????????",record)

# ----------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------    

    # THIS IS A SEARCH ORM BUT PARAM OFFSET
    # def do_search(self):
    #     hey = self.search([], offset= 3)
    #     print(">>>>>>>>>>>>>>>>>>>>>>>>>",hey)
    #     for rec in hey:
    #         record = rec.name
    #         print("@@@@@@@@@@@@@@@@@@@@",record)
    #     return True
    
# ----------------------------------------------------------------------------------------------------------    

    # THIS IS A SEARCH ORM BUT PARAM LIMIT
    # def do_search(self):
    #     hey = self.search([], limit=2)
    #     print(">>>>>>>>>>>>>>>>>>>>>>>>>",hey)
    #     for rec in hey:
    #         record = rec.name
    #         print("@@@@@@@@@@@@@@@@@@@@",record)
    #     return True
    
    
# ----------------------------------------------------------------------------------------------------------    

    # THIS IS A SEARCH ORM BUT ORDER
    # def do_search(self):
    #     hey = self.search([], order= "name")
    #     print(">>>>>>>>>>>>>>>>>>>>>>>>>",hey)
    #     for rec in hey:
    #         record = rec.name
    #         print("@@@@@@@@@@@@@@@@@@@@",record)
    #     return True
    
    
    
# ----------------------------------------------------------------------------------------------------------   
 
    # THIS IS A SEARCH COUNT PARAMETER LIMIT
    # def do_search(self):
    #     hey = self.search_count([], limit= 2)
    #     print("??????????????????????????????",hey)
    #     for rec in self:
    #         record = rec.name
    #         print(">>>>>>>>>>>>>>>>>>>>>>>>",record)
    #     return True
    
    
    #  # THIS IS A SEARCH COUNT PARAMETER LIMIT
# ----------------------------------------------------------------------------------------------------------   

    # def do_search(self):
    #     hey = self.name_search([], operator= "name ilike ")
    #     print("??????????????????????????????",hey)
    #     for rec in self:
    #         record = rec.name
    #         print(">>>>>>>>>>>>>>>>>>>>>>>>",record)
    #     return True

# # ----------------------------------------------------------------------------------------------------------   
# ----------------------------------------------------------------------------------------------------------    

    # def do_search(self):
    #     hey = self.search([('gender', '=' ,'female')])
    #     print(">>>>>>>>>>>>>>>>>>>>>>>>>",hey)
    #     for rec in hey:
    #         print("@@@@@@@@@@@@@@@@@@@@",rec.name)
# ----------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------          