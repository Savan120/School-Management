from odoo import models, fields, api


class salary_wizard(models.TransientModel):
    _name = "salary.wizard"
    _description = "This is a student fees wizard"
    
    name= fields.Char(string = "Name" )
    phone  = fields.Char(string = "Phone Number")
    mail   = fields.Char(string = "Work E-Mail Id")
    marital = fields.Selection([('single','Single'),('married','Married')],string = "Marital Status")
    salary= fields.Float(string = "Salary")

    
    def update_salary(self):
        print(" ############## context>>>>>>.", self._context)
        teacher_id= self.env['teacher.info'].browse(self._context.get('active_ids'))
        teacher_id.salary = self.salary
        teacher_id= self.env['teacher.info'].browse(self._context.get('active_ids'))
        teacher_id.name = self.name
        teacher_id= self.env['teacher.info'].browse(self._context.get('active_ids'))
        teacher_id.phone = self.phone
        teacher_id= self.env['teacher.info'].browse(self._context.get('active_ids'))
        teacher_id.mail = self.mail
        teacher_id= self.env['teacher.info'].browse(self._context.get('active_ids'))
        teacher_id.marital = self.marital
        
    @api.model
    def default_get(self, fields):
        name = super('update_salary', self).default_get(fields)
        get_name = self.env.context.get('active_id')
        if get_name:
            teach_name = self.env['teacher.info'].browse(get_name)
            name['name'] = teach_name.teacher_name
        return name