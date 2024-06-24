from odoo import models, fields, api

class sale_order(models.Model):
    _inherit="sale.order"
    
    student_id = fields.Many2one("student.info",string="Student Name")
    
    hobby_ids=fields.Many2many("hobby.detail", string="Hobby")
    properties_ids= fields.One2many("property.record", 'sale_id', string = "Property detail")
    ispresent=fields.Boolean(string="Is Present")
    total = fields.Float(compute = "get_total",string = "Totals")

    
             
    @api.depends('properties_ids.total_id')
    def get_total(self):
        for rec in self:
            rec.total = sum(rec.properties_ids.mapped('total_id'))
    
    
class sale_order_line(models.Model):
    _inherit="sale.order.line"


    dic_type=fields.Selection([('fix','Fix'),('per','Percentage')], string="Discount") 
    sale_discount=fields.Float(string="Discounts")
    
    @api.depends('dic_type','sale_discount')
    def _compute_amount(self):
        super()._compute_amount()
        for rec in self:
            if rec.dic_type == 'fix':
                rec.price_subtotal -= (rec.sale_discount)
            elif rec.dic_type == 'per':
                percentage = (rec.price_subtotal *rec.sale_discount / 100)
                total = rec.price_subtotal - percentage
                rec.price_subtotal = total
    