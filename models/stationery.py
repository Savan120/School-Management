from odoo import models, fields, api


class stationery(models.Model):
    _name = "stationery.detail"
    _description = "This is an stationery model"
    _rec_name="product_name"
    
    product_name = fields.Char(string = "Product Name")
    product_price= fields.Float(string="Product Price")
    product_qty = fields.Float(string="Product Quantity")
    total_price = fields.Float(compute="get_total",string="Total Price")
    product_brand=fields.Char(string="Product Brand")
    
    @api.depends('product_qty', 'product_price')
    def get_total(self):
        for rec in self:
            rec.total_price=rec.product_qty * rec.product_price