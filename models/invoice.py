from odoo import models, fields, api


class stationery(models.Model):
   _name = "invoice.detail"
   _description = "This is an Invoice model"
   _rec_name="student_ids"
   
   sequence = fields.Char(string = "Invoice Id", readonly = True, store = True)
   std_ids=fields.Many2one("standard.detail", string="Standard")
   student_ids=fields.Many2many("student.info", string="Customer Name", readonly = True, store = True)
   
   
   
   
   
   
   
   
   
   @api.model_create_multi
   def create(self, vals_list):
      """For Create sequence"""
      for vals in vals_list:
         print('vals >>>>>>>>>>>>>>>>>', vals)
         seq = self.env['ir.sequence'].next_by_code('invoice') or ("New")
         print('seq >>>>>>>>>>>>>>>>>>', seq)
         vals['sequence'] = seq
      return super().create(vals_list)

    
    
