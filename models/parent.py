from odoo import models , fields , api

class parent_detail(models.Model):
    _name = "parent.info"
    _description = "parent detail"
    _rec_name = "father_name"

    standard_id = fields.Many2one("standard.detail", string = "Standard", required = True)
    stud_ids = fields.Many2many("student.info", string = "Students Name")
    father_name= fields.Char(related = "stud_ids.father_name", string = "Father Name")
    parent_no = fields.Char(related = "stud_ids.parent_no", string = "Mobile No.")
    parent_mail=fields.Char(related = "stud_ids.parent_mail", string="Parent E-mail")
    mother_name = fields.Char(related = "stud_ids.mother_name",string = "Mother name")
    mother_occ = fields.Char(related="stud_ids.mother_occ", string = "Mother Occupation")
    father_occ = fields.Char(related="stud_ids.father_occ", string = "Father Occupation")
    marksheet_ids = fields.One2many(related = "stud_ids.marksheet_ids", readonly="1")
    exam_ids = fields.One2many(related = "stud_ids.exam_ids", string = "Exam", readonly= True)
    student_name=fields.Many2one("student.info", string = "Student Name")
    # user_id = fields.Many2one('res.users', string="Relational User", default= lambda self  : self.env.user)
    # exam_ids = fields.One2many('exam.record', 'student_rec', string = "Exam")
    
    @api.model_create_multi
    def create(self, vals):
        print(">>>>>>>>>>>>>CREATE METHOD>>>>>>>>>>>>>>")
        hey=super().create(vals)
        print("""""""""""""""""""""""""""""""""""""""""""""""",hey)
        return hey
    
    def write(self, vals):
        print(">>>>>>>>>>>>>WRITE METHOD>>>>>>>>>>>>>>")
        hey=super().write(vals)
        print("""""""""""""""""""""""""""""""""""""""""""""""",vals)
        print("""""""""""""""""""""""""""""""""""""""""""""""",hey)
        return hey
    
    def read(self, vals):
        print(">>>>>>>>>>>>>READ METHOD>>>>>>>>>>>>>>")
        hey=super().read(vals)
        print("""""""""""""""""""""""""""""""""""""""""""""""",vals)
        print("""""""""""""""""""""""""""""""""""""""""""""""",hey)
        return hey
    
    def unlink(self):
        print(">>>>>>>>>>>>>DELETE METHOD>>>>>>>>>>>>>>")
        hey=super().unlink()
        print("""""""""""""""""""""""""""""""""""""""""""""""",hey)
        return hey
