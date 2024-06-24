from odoo import models, fields


class wizard(models.TransientModel):
    _name = "student.wizard"
    _description = "This is a student fees wizard"
    
    fee= fields.Float(string = "Fees")
    
    
    def update_fees(self):
        print(" ############## context>>>>>>.", self._context)
        student_id = self.env['standard.detail'].browse(self._context.get('active_ids'))
        print(" @@@@@@@@@ student_id >>>>>>>>>>>>", student_id)
        student_id.fee = self.fee