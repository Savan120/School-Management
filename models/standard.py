from odoo import models , fields, api # type: ignore
from odoo.exceptions import ValidationError # type: ignore

class standard_detail(models.Model):
    _name = "standard.detail"
    _description = "standard detail"
    _rec_name = "std"
    
    
    teacher = fields.Char(string = "Teacher name")
    std = fields.Char(string = "standard", required = True)
    fee = fields.Float(string = "Fees", required = True)
    medium = fields.Selection([('english' , "English"),('gujarati','Gujarati'),('hindi','Hindi')],string= "Medium", required = True)
    standard_id= fields.Many2many("subject.detail", string = "Subjects", required = True)
    depart = fields.Selection([('primary','Primary'),('secondary','Secondary'),('higher','Higher')],string = "Department")	
    student_ids=fields.One2many("student.info",'standard_id', string="Student", readonly = "1")

    
    @api.constrains("fee")
    def fee_validation(self):
        for rec in self:
            if rec.fee <= 0:
                raise ValidationError("Invalid Fees")
            
    
    # # THIS IS AN NAME GET METHOD
    @api.model
    def name_get(self):
        res = []
        for th in self:
            name = th.std
            if th.depart:
                name = name + ' - ' + th.depart
            res.append((th.id, name))
        print("//////////////////////////////////////////",res)
        return res 
            
    # def name_get(self):
    #     res=[] 
    #     for rec in self:
    #         x=f"{rec.std} [{rec.medium}]"
    #         res.append((rec.id,x))
    #     return res
    
    # def duplicate(self, defalut= None):
    #     self.copy(default= {"std" : "10"})

    
    
    