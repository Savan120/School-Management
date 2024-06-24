from odoo import models


class product(models.Model):
    _inherit="product.product"
    
    
    def action_purchase_order(self):
        # x = self.browse(self._context.get("params").get("id"))
        # print("@@@@@@@@@@@@@@@@@",x.seller_ids.partner_id)
        vals_list = {
            "partner_id":self.seller_ids[0].partner_id.id,
        }
        
        y= self.env["purchase.order"].create(vals_list)
        line_order = []
        for line in self:
            line_order.append((0, 0, {
                "product_id": line.id,
            }))
            y.order_line = line_order
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>",y.order_line)
        