from odoo import fields, models, api

class School_Properties(models.Model):
    _name = 'property.detail'
    _description = 'School Properties'
    _rec_name='name'

    name = fields.Char(string="Name")
    qty = fields.Float(string='Quantity')
    price = fields.Float(string='Unit Price')
    total = fields.Float(compute= "get_total", string='Total')
   
    @api.depends('qty', 'price')
    def get_total(self):
        for rec in self:
            rec.total=rec.qty * rec.price
            
class record_property(models.Model):
    _name = "property.record"
    _description = "Record Property"
    
    student_id=fields.Many2one("student.info")
    sale_id=fields.Many2one("sale.order")
    property_ids=fields.Many2one("property.detail",string='Name')
    qty_id=fields.Float(related='property_ids.qty' , string='Qty')
    price_id=fields.Float(related='property_ids.price' , string='Unit Price')
    total_id=fields.Float(related= 'property_ids.total', string = 'Total')